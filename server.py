import os
import uuid
import threading
import json
import markdown
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from crewai import LLM, Agent, Task, Crew, Process
from crewai_tools import DirectoryReadTool, FileReadTool

load_dotenv()

app = FastAPI(title="AuditAI Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

EVIDENCIAS_DIR = Path("/app/evidencias")
DB_DIR = Path("/app/db")
EVIDENCIAS_DIR.mkdir(parents=True, exist_ok=True)
DB_DIR.mkdir(parents=True, exist_ok=True)

# Estado global de los jobs en memoria
jobs: dict[str, dict] = {}

# ──────────────────────────────────────────────────────────────
#  CONSTRUCCIÓN DEL CREW
# ──────────────────────────────────────────────────────────────

def build_crew() -> tuple[Crew, dict]:
    """
    Construye el crew completo y devuelve (crew, referencias_tareas).
    Las referencias a tareas permiten extraer sus outputs individuales.
    """
    llm = LLM(
        model=os.getenv("MODEL_NAME"),
        base_url=os.getenv("OLLAMA_BASE_URL"),
        temperature=0.1,
    )

    docs_tool = DirectoryReadTool(directory=str(EVIDENCIAS_DIR))
    file_tool = FileReadTool()

    # ── Agentes Auditores Especializados ──
    normativas = [
        {
            "n": "ISO 27001:2022",
            "g": "Identificar incumplimientos en los 93 controles del Anexo A de ISO 27001:2022, evaluando gestión de activos, control de accesos, criptografía, seguridad física, gestión de incidentes y continuidad de negocio.",
            "backstory": (
                "Eres un Lead Auditor certificado ISO/IEC 27001 con más de 12 años de experiencia en auditorías de SGSI "
                "para organizaciones del sector financiero, sanitario y de infraestructuras críticas. Has liderado más de "
                "80 proyectos de certificación en Europa y Latinoamérica. Tu metodología combina análisis de brechas "
                "técnicas con evaluación de madurez de procesos. Eres meticuloso, citas evidencias concretas y siempre "
                "relacionas los hallazgos con los controles específicos de la norma (A.5 a A.8)."
            ),
        },
        {
            "n": "ENS (Esquema Nacional de Seguridad)",
            "g": "Auditar el cumplimiento del Real Decreto 311/2022 (ENS), evaluando las medidas de protección en categorías BÁSICA, MEDIA y ALTA.",
            "backstory": (
                "Eres un auditor acreditado ENS por el CCN-CERT con experiencia en administraciones públicas y "
                "proveedores de servicios digitales para el sector público español. Conoces en profundidad la Guía "
                "CCN-STIC 808. Has participado en más de 40 proyectos de adecuación ENS."
            ),
        },
        {
            "n": "GDPR / RGPD",
            "g": "Verificar el cumplimiento del Reglamento (UE) 2016/679, analizando bases legales de tratamiento, derechos ARCO+, registro de actividades, EIPD y transferencias internacionales.",
            "backstory": (
                "Eres un Data Protection Officer (DPO) certificado con especialización en derecho digital europeo. "
                "Has asesorado a más de 60 organizaciones en su adecuación al RGPD y has gestionado notificaciones "
                "de brechas ante la AEPD. Dominas el análisis de flujos de datos y la elaboración de EIPD."
            ),
        },
        {
            "n": "NIS2 (Directiva UE 2022/2555)",
            "g": "Evaluar la resiliencia operacional y obligaciones de gestión de riesgos, notificación de incidentes y seguridad de la cadena de suministro conforme a NIS2.",
            "backstory": (
                "Eres un experto en ciberseguridad de infraestructuras críticas con certificación CISSP. "
                "Has participado en ejercicios de resiliencia a nivel europeo coordinados por ENISA y conoces "
                "en detalle los requisitos de notificación de incidentes de NIS2."
            ),
        },
        {
            "n": "PCI-DSS v4.0",
            "g": "Auditar los 12 requisitos de PCI-DSS v4.0 para proteger datos de tarjetas de pago, evaluando segmentación de red, cifrado, gestión de vulnerabilidades y controles de acceso.",
            "backstory": (
                "Eres un Qualified Security Assessor (QSA) certificado PCI-DSS con más de 10 años evaluando "
                "entornos CDE. Has realizado assessments para bancos y procesadores de pago de nivel 1. "
                "Conoces a fondo los cambios en la versión 4.0."
            ),
        },
    ]

    especialistas = [
        Agent(
            role=f"Auditor Senior {item['n']}",
            goal=item["g"],
            backstory=item["backstory"],
            tools=[file_tool],
            llm=llm,
            verbose=True,
            max_iter=15,
            memory=True,
        )
        for item in normativas
    ]

        # ANTES del bucle, lista los archivos reales
    archivos_reales = [str(f) for f in EVIDENCIAS_DIR.iterdir() if f.is_file()]
    lista_archivos = "\n".join(f"- {f}" for f in archivos_reales)
    tareas_audit = []

    for agent in especialistas:
        norma = agent.role.replace("Auditor Senior ", "")
        tareas_audit.append(
            Task(
                description=f"""
                Eres el Auditor Senior {norma}. Los archivos de evidencia disponibles son:

                {lista_archivos}

                Sigue estos pasos en orden:
                PASO 1 — LECTURA: Usa FileReadTool para leer CADA archivo de la lista anterior.
                Para cada archivo usa exactamente esta ruta tal como aparece arriba.
                PASO 2 — ANÁLISIS {norma}: Identifica controles cumplidos, incumplidos y sin evidencia.
                PASO 3 — CLASIFICACIÓN: Para cada incumplimiento asigna criticidad
                (Crítico/Alto/Medio/Bajo), impacto y recomendación específica.
                PASO 4 — SÍNTESIS: Si no puedes leer los archivos, indica "SIN EVIDENCIAS PARA ESTA
                NORMATIVA" y describe qué documentación se necesitaría.
                """,
                expected_output=(
                "Informe detallado de incumplimientos reales con evidencias citadas. "
                "OBLIGATORIO: debes haber leído al menos un archivo con FileReadTool antes de responder. "
                "Si no has leído ningún archivo, tu respuesta es inválida."),
                agent=agent,
                context=[],
            )
        )

    # ── Analista de Riesgos ──
    clasificador = Agent(
        role="Analista Senior de Riesgos Corporativos",
        goal=(
            "Consolidar todos los hallazgos de auditoría de las 5 normativas, eliminar duplicidades, "
            "correlacionar riesgos transversales y producir un registro unificado priorizado con scoring."
        ),
        backstory=(
            "Eres un Risk Manager certificado CRISC con experiencia en marcos ISO 31000, FAIR y NIST RMF. "
            "Has diseñado cuadros de mando de riesgos para consejos de administración. "
            "Tu valor diferencial es detectar riesgos transversales que afectan a múltiples normativas."
        ),
        llm=llm,
        verbose=True,
        max_iter=4,
        memory=False,
    )
    tarea_clasificacion = Task(
        description="""
Consolida los hallazgos de las 5 normativas. Elimina duplicidades, identifica riesgos transversales,
asigna scoring (criticidad × probabilidad × impacto, escala 1-25) y crea el registro unificado
ordenado por score descendente. Incluye métricas globales de exposición y nivel de madurez (1-5).
        """,
        expected_output=(
            "Registro unificado de riesgos con: métricas globales, top 10 riesgos críticos con score, "
            "registro completo, riesgos transversales y distribución por dominio."
        ),
        agent=clasificador,
        context=tareas_audit,
    )

    # ── Agente CISO ──
    agente_ciso = Agent(
        role="Redactor de Informe Técnico para CISO",
        goal="Generar informe técnico detallado para el CISO con hallazgos técnicos, análisis de brechas, métricas y roadmap de remediación.",
        backstory=(
            "Eres un consultor senior de ciberseguridad especializado en redactar informes técnicos para CISOs. "
            "Aportas profundidad técnica: controles exactos que fallan, arquitecturas deficientes y herramientas "
            "concretas a implementar. Tu estilo es directo, con tablas y métricas precisas."
        ),
        llm=llm,
        verbose=True,
        max_iter=4,
        memory=False,
    )
    tarea_informe_ciso = Task(
        description="""
Redacta el INFORME TÉCNICO PARA CISO en Markdown. Incluye:
- Resumen ejecutivo técnico con semáforo por normativa (🔴🟡🟢) e indicadores numéricos
- Análisis de brechas por normativa con % de cumplimiento y referencias exactas a controles
- Tabla completa de hallazgos: ID | Hallazgo | Normativas | Criticidad | Score | Evidencia | Recomendación Técnica
- Riesgos transversales y su impacto amplificado
- Gaps arquitectónicos y controles compensatorios
- Roadmap de remediación: Acción | Responsable | Herramienta | Plazo | KPI | Normativas que remedia
  * Fase 1 (0-30d): acciones críticas y quick-wins
  * Fase 2 (30-90d): mejoras estructurales
  * Fase 3 (90-180d): madurez y automatización
- KPIs de seguimiento y estimación de esfuerzo/presupuesto
        """,
        expected_output="Informe técnico Markdown para CISO con profundidad técnica, tablas detalladas y roadmap accionable.",
        agent=agente_ciso,
        context=[tarea_clasificacion, *tareas_audit],
    )

    # ── Agente CEO ──
    agente_ceo = Agent(
        role="Redactor de Informe Ejecutivo para CEO y Dirección",
        goal="Generar informe ejecutivo para CEO y dirección no técnica, traduciendo riesgos en impacto de negocio y decisiones estratégicas.",
        backstory=(
            "Eres un consultor de riesgos corporativos que presenta ante consejos de administración. "
            "Traduces riesgos técnicos a impacto económico, sanciones regulatorias y riesgo reputacional. "
            "Evitas jerga técnica y siempre cuantificas el impacto en términos de negocio."
        ),
        llm=llm,
        verbose=True,
        max_iter=4,
        memory=False,
    )
    tarea_informe_ceo = Task(
        description="""
Redacta el INFORME EJECUTIVO PARA CEO Y DIRECCIÓN en Markdown. SIN tecnicismos. Incluye:
- Resumen para la dirección (máximo 1 página): estado actual, semáforo normativo, decisión más urgente
- Exposición al riesgo regulatorio por normativa con cuantificación:
  * GDPR: hasta 20M€ o 4% facturación global
  * ENS: pérdida de contratos con AAPP
  * NIS2: multas hasta 10M€ o 2% facturación
  * PCI-DSS: revocación de capacidad de procesar pagos
  * ISO 27001: impacto en certificación y contratos
- Impacto potencial en el negocio: continuidad, reputación, clientes
- Los 5 riesgos más críticos explicados en lenguaje de negocio
- Tabla: Área de Mejora | Inversión Estimada | Riesgo Mitigado | ROI de Seguridad
- Decisiones estratégicas requeridas por la dirección
- Hoja de ruta ejecutiva a 6 meses (timeline simplificado)
- Top 3 acciones inmediatas (próximos 30 días)
        """,
        expected_output="Informe ejecutivo Markdown para CEO/Dirección sin tecnicismos, con foco en impacto de negocio y decisiones estratégicas.",
        agent=agente_ceo,
        context=[tarea_clasificacion],
    )

    # ── Agente General/DPO ──
    agente_general = Agent(
        role="Redactor de Informe General de Cumplimiento Normativo",
        goal="Generar informe formal de cumplimiento para DPO, compliance officers y auditores externos con matrices de controles y plan de acción.",
        backstory=(
            "Eres un especialista en compliance y gobierno corporativo. Has preparado informes para la AEPD, "
            "el CCN y auditores ISO. Aportas trazabilidad completa: cada hallazgo enlazado con el artículo "
            "exacto, la evidencia y el estado de remediación. Estilo formal y riguroso."
        ),
        llm=llm,
        verbose=True,
        max_iter=4,
        memory=False,
    )
    tarea_informe_general = Task(
        description="""
Redacta el INFORME GENERAL DE CUMPLIMIENTO NORMATIVO en Markdown. Incluye:
- Control del documento (versión, fecha, clasificación, elaborado/revisado/aprobado por)
- Alcance y metodología de la auditoría, limitaciones del análisis
- Estado de cumplimiento por normativa con tablas:
  | Control/Artículo | Descripción | Estado (C/NC/NE/NA) | Evidencia | Observaciones |
  (C=Cumple, NC=No Cumple, NE=No Evidencia, NA=No Aplica)
  Secciones para: ISO 27001, ENS, GDPR, NIS2, PCI-DSS
- Registro de No Conformidades: ID-NC | Normativa | Requisito | Criticidad | Fecha | Responsable | Estado
- Plan de Acción Correctivo (PAC): acción | responsable | fecha límite | indicador de cierre
- Análisis de riesgos para el Registro de Tratamientos GDPR (si hay datos personales en evidencias)
- Cadena de custodia de evidencias analizadas
- Declaraciones de aplicabilidad (controles ISO excluidos y justificación)
        """,
        expected_output="Informe formal Markdown para DPO/Compliance con matrices de controles, registro de no conformidades y PAC.",
        agent=agente_general,
        context=[tarea_clasificacion, *tareas_audit],
    )

    crew = Crew(
        agents=[*especialistas, clasificador, agente_ciso, agente_ceo, agente_general],
        tasks=[*tareas_audit, tarea_clasificacion, tarea_informe_ciso, tarea_informe_ceo, tarea_informe_general],
        process=Process.sequential,
        verbose=True,
    )

    task_refs = {
        "audit": tareas_audit,
        "clasificacion": tarea_clasificacion,
        "ciso": tarea_informe_ciso,
        "ceo": tarea_informe_ceo,
        "general": tarea_informe_general,
    }

    return crew, task_refs


# ──────────────────────────────────────────────────────────────
#  EJECUCIÓN EN BACKGROUND
# ──────────────────────────────────────────────────────────────

def run_analysis(job_id: str):
    """Ejecuta el crew en un thread separado y actualiza el estado del job."""
    import time

    job = jobs[job_id]

    agentes_orden = [
        ("iso",     "Auditor Senior ISO 27001:2022"),
        ("ens",     "Auditor Senior ENS"),
        ("gdpr",    "Auditor Senior GDPR / RGPD"),
        ("nis2",    "Auditor Senior NIS2"),
        ("pci",     "Auditor Senior PCI-DSS v4.0"),
        ("risk",    "Analista Senior de Riesgos"),
        ("ciso",    "Redactor Informe CISO"),
        ("ceo",     "Redactor Informe CEO / Dirección"),
        ("general", "Redactor Informe Cumplimiento General"),
    ]

    def set_agent(idx, state, msg=""):
        job["agente_actual"]  = agentes_orden[idx][0]
        job["agente_nombre"]  = agentes_orden[idx][1]
        job["agente_estado"]  = state
        job["agente_idx"]     = idx
        job["mensaje"]        = msg

    try:
        archivos = [f for f in EVIDENCIAS_DIR.iterdir() if f.is_file()]
        if not archivos:
            job["estado"] = "error"
            job["error"]  = "No hay archivos en la carpeta de evidencias."
            return

        job["estado"]        = "running"
        job["total_agentes"] = len(agentes_orden)

        crew, task_refs = build_crew()

        resultado_holder = {"result": None, "error": None, "tasks": None}

        def crew_thread():
            try:
                resultado_holder["result"] = crew.kickoff()
                resultado_holder["tasks"]  = task_refs
            except Exception as e:
                resultado_holder["error"] = str(e)

        t = threading.Thread(target=crew_thread)
        t.start()

        # Tiempos estimados por agente (segundos)
        tiempos = [45, 45, 45, 40, 40, 30, 35, 25, 35]

        for i, (agent_id, agent_name) in enumerate(agentes_orden):
            set_agent(i, "running", f"Analizando con {agent_name}…")
            wait = tiempos[i] if i < len(tiempos) else 30
            for _ in range(wait * 10):
                if not t.is_alive():
                    break
                time.sleep(0.1)
            if not t.is_alive():
                for j in range(i, len(agentes_orden)):
                    set_agent(j, "done", "")
                break
            set_agent(i, "done", "")

        t.join()

        if resultado_holder["error"]:
            job["estado"] = "error"
            job["error"]  = resultado_holder["error"]
            return

        tasks = resultado_holder["tasks"]

        # Extraer outputs de cada tarea
        def safe_output(task):
            if task and task.output:
                return task.output.raw or str(task.output)
            return ""

        md_ciso    = safe_output(tasks["ciso"])
        md_ceo     = safe_output(tasks["ceo"])
        md_general = safe_output(tasks["general"])
        md_risk    = safe_output(tasks["clasificacion"])

        # Si alguno está vacío, usar el resultado final del crew
        result_str = str(resultado_holder["result"])
        if not md_ciso:    md_ciso    = result_str
        if not md_ceo:     md_ceo     = result_str
        if not md_general: md_general = result_str

        # Guardar Markdown en disco
        informes_md = {
            "ciso":    md_ciso,
            "ceo":     md_ceo,
            "general": md_general,
            "clasificacion": md_risk,
        }
        for nombre, contenido in informes_md.items():
            if contenido:
                path = DB_DIR / f"informe_{nombre}.md"
                path.write_text(contenido, encoding="utf-8")

        # Convertir a HTML
        html_ciso    = markdown_to_html(md_ciso,    "CISO — Técnico",           "ciso")
        html_ceo     = markdown_to_html(md_ceo,     "CEO / Dirección — Ejecutivo", "ceo")
        html_general = markdown_to_html(md_general, "Cumplimiento General — DPO/Compliance", "general")

        for nombre, html in [("ciso", html_ciso), ("ceo", html_ceo), ("general", html_general)]:
            path = DB_DIR / f"informe_{nombre}.html"
            path.write_text(html, encoding="utf-8")

        job["estado"]       = "done"
        job["fecha"]        = datetime.now().isoformat()
        job["informes_md"]  = informes_md
        job["informes_html"] = {
            "ciso":    html_ciso,
            "ceo":     html_ceo,
            "general": html_general,
        }

    except Exception as e:
        job["estado"] = "error"
        job["error"]  = str(e)


# ──────────────────────────────────────────────────────────────
#  HTML RENDERER
# ──────────────────────────────────────────────────────────────

INFORME_LABELS = {
    "ciso":    ("Informe Técnico — CISO",                  "#5b9fff", "👨‍💻"),
    "ceo":     ("Informe Ejecutivo — CEO / Dirección",     "#00e5a0", "📊"),
    "general": ("Informe de Cumplimiento — DPO/Compliance","#a78bfa", "📋"),
}

def markdown_to_html(md_text: str, subtitulo: str, tipo: str) -> str:
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "toc"],
    )

    # Badges de criticidad
    for palabra, cls in [("Crítico", "critico"), ("Alto", "alto"), ("Medio", "medio"), ("Bajo", "bajo")]:
        body = body.replace(f">{palabra}<",        f'><span class="badge {cls}">{palabra}</span><')
        body = body.replace(f"**{palabra}**",      f'<span class="badge {cls}">{palabra}</span>')

    # Badges de estado de cumplimiento
    for palabra, cls in [("No Cumple", "nc"), ("Cumple", "c"), ("No Evidencia", "ne"), ("No Aplica", "na")]:
        body = body.replace(f">{palabra}<",   f'><span class="badge {cls}">{palabra}</span><')

    label, color, emoji = INFORME_LABELS.get(tipo, (subtitulo, "#00e5a0", "📄"))

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{label} — AuditAI</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #0d1117; --bg2: #161b22; --bg3: #21262d;
    --accent: {color}; --danger: #ff4757; --warn: #ffa502;
    --info: #5b9fff; --purple: #a78bfa;
    --text: #e8eaf0; --text2: #8892a4; --text3: #4a5568;
    --border: #21262d;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg); color: var(--text);
    font-family: 'Inter', sans-serif; font-size: 15px;
    line-height: 1.8; padding: 0;
  }}
  .page-wrap {{ max-width: 980px; margin: 0 auto; padding: 60px 40px 120px; }}

  h1 {{ font-family: 'Syne', sans-serif; font-size: 38px; font-weight: 800;
        color: var(--accent); margin-bottom: 8px; line-height: 1.1; letter-spacing: -1px; }}
  h2 {{ font-family: 'Syne', sans-serif; font-size: 21px; font-weight: 700;
        color: #fff; margin: 52px 0 16px; padding-bottom: 10px;
        border-bottom: 2px solid var(--border); }}
  h3 {{ font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 700;
        color: var(--accent); margin: 32px 0 10px; }}
  h4 {{ font-size: 14px; font-weight: 600; color: var(--text2); margin: 20px 0 8px; text-transform: uppercase; letter-spacing: 0.5px; }}
  p {{ margin-bottom: 14px; color: var(--text); }}
  a {{ color: var(--accent); }}
  strong {{ color: #fff; font-weight: 500; }}
  em {{ color: var(--text2); font-style: italic; }}
  blockquote {{
    border-left: 3px solid var(--accent); margin: 24px 0;
    padding: 14px 20px; background: rgba(255,255,255,0.03);
    border-radius: 0 8px 8px 0; color: var(--text2);
  }}
  code {{
    background: var(--bg2); color: var(--accent);
    padding: 2px 7px; border-radius: 4px;
    font-family: 'IBM Plex Mono', monospace; font-size: 13px;
  }}
  pre {{ background: var(--bg2); border: 1px solid var(--border);
         border-radius: 10px; padding: 20px; overflow-x: auto; margin: 20px 0; }}
  pre code {{ background: none; padding: 0; color: var(--text); }}
  ul, ol {{ padding-left: 24px; margin-bottom: 14px; }}
  li {{ margin-bottom: 6px; }}
  hr {{ border: none; border-top: 1px solid var(--border); margin: 48px 0; }}

  /* TABLES */
  .table-wrap {{ overflow-x: auto; margin: 24px 0; border-radius: 12px;
                  border: 1px solid var(--border); }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  thead tr {{ background: var(--bg2); }}
  th {{ padding: 12px 16px; text-align: left; color: var(--text2);
        font-size: 11px; font-weight: 500; text-transform: uppercase;
        letter-spacing: 1px; white-space: nowrap; }}
  td {{ padding: 12px 16px; border-top: 1px solid var(--border); vertical-align: top; }}
  tbody tr:hover {{ background: rgba(255,255,255,0.02); }}

  /* BADGES — criticidad */
  .badge {{ display: inline-block; padding: 2px 10px; border-radius: 20px;
             font-size: 11px; font-weight: 600; letter-spacing: 0.5px; white-space: nowrap; }}
  .critico {{ background: rgba(255,71,87,0.15); color: #ff6b7a; border: 1px solid rgba(255,71,87,0.3); }}
  .alto    {{ background: rgba(255,165,2,0.15);  color: #ffc04d; border: 1px solid rgba(255,165,2,0.3); }}
  .medio   {{ background: rgba(255,215,0,0.12);  color: #ffd700; border: 1px solid rgba(255,215,0,0.25); }}
  .bajo    {{ background: rgba(0,229,160,0.12);   color: #00e5a0; border: 1px solid rgba(0,229,160,0.25); }}

  /* BADGES — estado cumplimiento */
  .c  {{ background: rgba(0,229,160,0.12); color: #00e5a0;  border: 1px solid rgba(0,229,160,0.3); }}
  .nc {{ background: rgba(255,71,87,0.15); color: #ff6b7a;  border: 1px solid rgba(255,71,87,0.3); }}
  .ne {{ background: rgba(255,165,2,0.12); color: #ffc04d;  border: 1px solid rgba(255,165,2,0.3); }}
  .na {{ background: rgba(255,255,255,0.06); color: #8892a4; border: 1px solid rgba(255,255,255,0.1); }}

  /* REPORT HEADER */
  .report-header {{
    background: var(--bg2); border: 1px solid var(--border);
    border-radius: 16px; padding: 36px 40px; margin-bottom: 52px;
    position: relative; overflow: hidden;
  }}
  .report-header::before {{
    content: '{emoji}';
    position: absolute; right: 36px; top: 50%; transform: translateY(-50%);
    font-size: 64px; opacity: 0.15;
  }}
  .report-type {{
    font-family: 'IBM Plex Mono', monospace; font-size: 11px;
    color: var(--accent); letter-spacing: 2px; text-transform: uppercase;
    margin-bottom: 10px;
  }}
  .report-meta {{
    display: flex; gap: 24px; flex-wrap: wrap; margin-top: 16px;
  }}
  .report-meta span {{
    font-size: 12px; color: var(--text3);
    font-family: 'IBM Plex Mono', monospace; letter-spacing: 0.3px;
  }}
  .report-meta span b {{ color: var(--text2); font-weight: 500; }}

  @media (max-width: 640px) {{
    .page-wrap {{ padding: 32px 20px 60px; }}
    h1 {{ font-size: 26px; }}
    h2 {{ font-size: 18px; }}
  }}
</style>
</head>
<body>
<div class="page-wrap">
  <div class="report-header">
    <div class="report-type">AuditAI — Informe de Seguridad</div>
    <h1>{label}</h1>
    <div class="report-meta">
      <span><b>Sistema:</b> AuditAI Multi-Agente (CrewAI + Ollama)</span>
      <span><b>Normativas:</b> ISO 27001 · ENS · GDPR · NIS2 · PCI-DSS</span>
      <span><b>Destinatario:</b> {subtitulo}</span>
    </div>
  </div>
  {body}
</div>
<script>
  document.querySelectorAll('table').forEach(t => {{
    if (!t.parentElement.classList.contains('table-wrap')) {{
      const w = document.createElement('div');
      w.className = 'table-wrap';
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    }}
  }});
</script>
</body>
</html>"""


# ──────────────────────────────────────────────────────────────
#  ENDPOINTS
# ──────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index():
    html_path = Path("/app/static/index.html")
    if html_path.exists():
        return HTMLResponse(html_path.read_text(encoding="utf-8"))
    return HTMLResponse("<h1>AuditAI</h1><p>Falta /app/static/index.html</p>")


@app.get("/api/evidencias")
async def listar_evidencias():
    archivos = []
    for f in EVIDENCIAS_DIR.iterdir():
        if f.is_file():
            archivos.append({
                "nombre":     f.name,
                "tamaño":     f.stat().st_size,
                "modificado": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
            })
    return {"archivos": sorted(archivos, key=lambda x: x["nombre"])}


@app.post("/api/evidencias/upload")
async def subir_evidencias(files: list[UploadFile] = File(...)):
    subidos = []
    for file in files:
        dest    = EVIDENCIAS_DIR / file.filename
        content = await file.read()
        dest.write_bytes(content)
        subidos.append({"nombre": file.filename, "tamaño": len(content)})
    return {"subidos": subidos}


@app.delete("/api/evidencias/{nombre}")
async def borrar_evidencia(nombre: str):
    path = EVIDENCIAS_DIR / nombre
    if not path.exists():
        raise HTTPException(404, "Archivo no encontrado")
    path.unlink()
    return {"ok": True}


@app.post("/api/analizar")
async def iniciar_analisis():
    archivos = [f for f in EVIDENCIAS_DIR.iterdir() if f.is_file()]
    if not archivos:
        raise HTTPException(400, "No hay archivos en la carpeta de evidencias.")

    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "estado":        "starting",
        "agente_actual": None,
        "agente_nombre": None,
        "agente_estado": None,
        "agente_idx":    -1,
        "total_agentes": 9,
        "mensaje":       "Preparando agentes…",
        "error":         None,
        "informes_md":   None,
        "informes_html": None,
        "fecha":         None,
    }
    threading.Thread(target=run_analysis, args=(job_id,), daemon=True).start()
    return {"job_id": job_id}


@app.get("/api/estado/{job_id}")
async def estado_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(404, "Job no encontrado")
    job = jobs[job_id]
    return {
        "estado":        job["estado"],
        "agente_idx":    job["agente_idx"],
        "agente_nombre": job["agente_nombre"],
        "agente_estado": job["agente_estado"],
        "total_agentes": job["total_agentes"],
        "mensaje":       job["mensaje"],
        "error":         job.get("error"),
        "fecha":         job.get("fecha"),
        "informes_disponibles": (
            list(job["informes_html"].keys())
            if job.get("informes_html") else []
        ),
    }


@app.get("/api/informe/{job_id}/{tipo}/html", response_class=HTMLResponse)
async def obtener_informe_html(job_id: str, tipo: str):
    """Devuelve un informe específico como HTML. tipo: ciso | ceo | general"""
    if job_id not in jobs:
        raise HTTPException(404, "Job no encontrado")
    job = jobs[job_id]
    if job["estado"] != "done":
        raise HTTPException(400, "El informe aún no está listo")
    if not job.get("informes_html") or tipo not in job["informes_html"]:
        raise HTTPException(404, f"Informe '{tipo}' no disponible")
    return HTMLResponse(job["informes_html"][tipo])


@app.get("/api/informe/{job_id}/{tipo}/md")
async def obtener_informe_md(job_id: str, tipo: str):
    """Devuelve un informe específico como Markdown. tipo: ciso | ceo | general | clasificacion"""
    if job_id not in jobs:
        raise HTTPException(404, "Job no encontrado")
    job = jobs[job_id]
    if job["estado"] != "done":
        raise HTTPException(400, "El informe aún no está listo")
    if not job.get("informes_md") or tipo not in job["informes_md"]:
        raise HTTPException(404, f"Informe '{tipo}' no disponible")
    return {"markdown": job["informes_md"][tipo]}


@app.get("/api/informe/ultimo/{tipo}/html", response_class=HTMLResponse)
async def ultimo_informe_html(tipo: str):
    """Último informe guardado en disco. tipo: ciso | ceo | general"""
    path = DB_DIR / f"informe_{tipo}.html"
    if not path.exists():
        raise HTTPException(404, f"No hay informe '{tipo}' generado todavía")
    return HTMLResponse(path.read_text(encoding="utf-8"))


@app.get("/api/informe/ultimo/{tipo}/descargar")
async def descargar_informe(tipo: str):
    """Descarga el informe HTML como archivo."""
    path = DB_DIR / f"informe_{tipo}.html"
    if not path.exists():
        raise HTTPException(404, f"No hay informe '{tipo}' generado todavía")
    fecha = datetime.now().strftime("%Y%m%d")
    return FileResponse(
        path, media_type="text/html",
        filename=f"auditoria_{tipo}_{fecha}.html",
    )


@app.get("/api/informes/disponibles")
async def informes_disponibles():
    """Lista qué informes están guardados en disco."""
    tipos = ["ciso", "ceo", "general", "clasificacion"]
    resultado = {}
    for tipo in tipos:
        md_path   = DB_DIR / f"informe_{tipo}.md"
        html_path = DB_DIR / f"informe_{tipo}.html"
        resultado[tipo] = {
            "md":   md_path.exists(),
            "html": html_path.exists(),
            "fecha": (
                datetime.fromtimestamp(html_path.stat().st_mtime).isoformat()
                if html_path.exists() else None
            ),
        }
    return resultado
