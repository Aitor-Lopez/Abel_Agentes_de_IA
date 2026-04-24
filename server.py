import os
import uuid
import asyncio
import threading
import json
import markdown
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse, FileResponse
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


def build_crew() -> Crew:
    llm = LLM(
        model=os.getenv("MODEL_NAME"),
        base_url=os.getenv("OLLAMA_BASE_URL"),
        temperature=0.1,
    )

    docs_tool = DirectoryReadTool(directory=str(EVIDENCIAS_DIR))
    file_tool = FileReadTool()

    normativas = [
        {"n": "ISO 27001", "g": "Auditoría de controles SGSI."},
        {"n": "ENS",       "g": "Cumplimiento Esquema Nacional de Seguridad."},
        {"n": "GDPR",      "g": "Protección de datos y privacidad."},
        {"n": "NIS2",      "g": "Resiliencia infraestructuras críticas."},
        {"n": "PCI-DSS",   "g": "Seguridad en transacciones financieras."},
    ]

    especialistas = [
        Agent(
            role=f"Auditor Senior {item['n']}",
            goal=item["g"],
            backstory=f"Experto en {item['n']} con certificación internacional.",
            tools=[docs_tool, file_tool],
            llm=llm,
            verbose=True,
        )
        for item in normativas
    ]

    tareas_audit = []
    for agent in especialistas:
        norma = agent.role.replace("Auditor Senior ", "")
        tareas_audit.append(
            Task(
                description=f"""
                1. Usa DirectoryReadTool para ver qué hay en '{EVIDENCIAS_DIR}'.
                2. Usa FileReadTool para leer el contenido de los archivos encontrados.
                3. SI NO HAY ARCHIVOS, reporta 'Sin evidencias para auditar'.
                4. Analiza las evidencias reales para la normativa {norma}.
                """,
                expected_output="Informe detallado de incumplimientos reales.",
                agent=agent,
            )
        )

    clasificador = Agent(
        role="Analista de Riesgos",
        goal="Consolidar y priorizar hallazgos.",
        backstory="Responsable de triaje y criticidad de vulnerabilidades.",
        llm=llm,
        verbose=True,
    )
    tarea_clasificacion = Task(
        description="Unifica los informes y asigna criticidad (Crítico, Alto, Medio, Bajo).",
        expected_output="Lista unificada de riesgos priorizados.",
        agent=clasificador,
        context=tareas_audit,
    )

    reportero = Agent(
        role="Estratega de Ciberseguridad",
        goal="Generar informe para CISO, DPO y Dirección.",
        backstory="Especialista en comunicación de riesgos corporativos.",
        llm=llm,
        verbose=True,
    )
    tarea_reporte = Task(
        description="""
        Crea el reporte final ejecutivo en Markdown.
        Incluye: Resumen Ejecutivo, tabla de riesgos con criticidad,
        Plan de Acción priorizado (0-30d, 30-90d, 90-180d), KPIs y Conclusiones.
        Sé específico citando evidencias reales de los documentos analizados.
        """,
        expected_output="Documento Markdown estructurado y completo.",
        agent=reportero,
        context=[tarea_clasificacion],
    )

    return Crew(
        agents=[*especialistas, clasificador, reportero],
        tasks=[*tareas_audit, tarea_clasificacion, tarea_reporte],
        process=Process.sequential,
    )


def run_analysis(job_id: str):
    """Ejecuta el crew en un thread separado y va actualizando el estado."""
    job = jobs[job_id]

    agentes_orden = [
        ("iso",   "Auditor Senior ISO 27001"),
        ("ens",   "Auditor Senior ENS"),
        ("gdpr",  "Auditor Senior GDPR"),
        ("nis2",  "Auditor Senior NIS2"),
        ("pci",   "Auditor Senior PCI-DSS"),
        ("risk",  "Analista de Riesgos"),
        ("ciso",  "Estratega de Ciberseguridad"),
    ]

    def set_agent(idx, state, msg=""):
        job["agente_actual"] = agentes_orden[idx][0]
        job["agente_nombre"] = agentes_orden[idx][1]
        job["agente_estado"] = state
        job["agente_idx"] = idx
        job["mensaje"] = msg

    try:
        archivos = [f for f in EVIDENCIAS_DIR.iterdir() if f.is_file()]
        if not archivos:
            job["estado"] = "error"
            job["error"] = "No hay archivos en la carpeta de evidencias."
            return

        job["estado"] = "running"
        job["total_agentes"] = len(agentes_orden)

        # Simulamos progreso por agente usando callbacks de CrewAI
        # Arrancamos el crew en un sub-hilo y movemos el indicador de agente
        crew = build_crew()

        # Avanzamos el indicador visualmente mientras el crew trabaja
        import time

        resultado_holder = {"result": None, "error": None}

        def crew_thread():
            try:
                resultado_holder["result"] = crew.kickoff()
            except Exception as e:
                resultado_holder["error"] = str(e)

        t = threading.Thread(target=crew_thread)
        t.start()

        # Avanzamos el indicador de agente cada ~30s mientras el crew trabaja
        tiempos = [30, 30, 30, 30, 30, 20, 15]
        for i, (agent_id, agent_name) in enumerate(agentes_orden):
            set_agent(i, "running", f"Analizando con {agent_name}…")
            wait = tiempos[i] if i < len(tiempos) else 20
            for _ in range(wait * 10):
                if not t.is_alive():
                    break
                time.sleep(0.1)
            if not t.is_alive():
                # Crew terminó antes — marcar todos los restantes como done
                for j in range(i, len(agentes_orden)):
                    set_agent(j, "done", "")
                break
            set_agent(i, "done", "")

        t.join()

        if resultado_holder["error"]:
            job["estado"] = "error"
            job["error"] = resultado_holder["error"]
            return

        result_md = str(resultado_holder["result"])

        # Guardar Markdown
        md_path = DB_DIR / "informe_final.md"
        md_path.write_text(result_md, encoding="utf-8")

        # Convertir a HTML bonito
        html_report = markdown_to_html(result_md)
        html_path = DB_DIR / "informe_final.html"
        html_path.write_text(html_report, encoding="utf-8")

        job["estado"] = "done"
        job["informe_md"] = result_md
        job["informe_html"] = html_report
        job["fecha"] = datetime.now().isoformat()

    except Exception as e:
        job["estado"] = "error"
        job["error"] = str(e)


def markdown_to_html(md_text: str) -> str:
    """Convierte el Markdown del informe a un HTML ejecutivo con diseño oscuro."""
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "toc"],
    )
    # Colorear badges de criticidad
    body = body.replace(">Crítico<", '><span class="badge critico">Crítico</span><')
    body = body.replace(">Alto<",    '><span class="badge alto">Alto</span><')
    body = body.replace(">Medio<",   '><span class="badge medio">Medio</span><')
    body = body.replace(">Bajo<",    '><span class="badge bajo">Bajo</span><')
    body = body.replace("**Crítico**", '<span class="badge critico">Crítico</span>')
    body = body.replace("**Alto**",    '<span class="badge alto">Alto</span>')
    body = body.replace("**Medio**",   '<span class="badge medio">Medio</span>')
    body = body.replace("**Bajo**",    '<span class="badge bajo">Bajo</span>')

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Informe Ejecutivo de Ciberseguridad</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #0d1117; --bg2: #161b22; --bg3: #21262d;
    --accent: #00e5a0; --danger: #ff4757; --warn: #ffa502;
    --info: #5b9fff; --success: #00e5a0;
    --text: #e8eaf0; --text2: #8892a4; --text3: #4a5568;
    --border: #21262d;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg); color: var(--text);
    font-family: 'Inter', sans-serif; font-size: 15px;
    line-height: 1.75; padding: 0;
  }}
  .page-wrap {{ max-width: 960px; margin: 0 auto; padding: 60px 40px 100px; }}
  h1 {{ font-family: 'Syne', sans-serif; font-size: 40px; font-weight: 800;
        color: var(--accent); margin-bottom: 8px; line-height: 1.1; letter-spacing: -1px; }}
  h2 {{ font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 700;
        color: #fff; margin: 48px 0 16px; padding-bottom: 10px;
        border-bottom: 1px solid var(--border); }}
  h3 {{ font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 700;
        color: var(--info); margin: 28px 0 10px; }}
  p {{ margin-bottom: 14px; color: var(--text); }}
  a {{ color: var(--accent); }}
  strong {{ color: #fff; font-weight: 500; }}
  em {{ color: var(--text2); font-style: italic; }}
  blockquote {{
    border-left: 3px solid var(--accent); margin: 20px 0;
    padding: 12px 20px; background: rgba(0,229,160,0.05);
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
  hr {{ border: none; border-top: 1px solid var(--border); margin: 40px 0; }}

  /* TABLES */
  .table-wrap {{ overflow-x: auto; margin: 20px 0; border-radius: 12px;
                  border: 1px solid var(--border); }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  thead tr {{ background: var(--bg2); }}
  th {{ padding: 12px 16px; text-align: left; color: var(--text2);
        font-size: 11px; font-weight: 500; text-transform: uppercase;
        letter-spacing: 1px; white-space: nowrap; }}
  td {{ padding: 12px 16px; border-top: 1px solid var(--border);
        vertical-align: top; }}
  tbody tr:hover {{ background: rgba(255,255,255,0.02); }}

  /* BADGES */
  .badge {{ display: inline-block; padding: 2px 10px; border-radius: 20px;
             font-size: 11px; font-weight: 600; letter-spacing: 0.5px; white-space: nowrap; }}
  .critico {{ background: rgba(255,71,87,0.15); color: #ff6b7a;
               border: 1px solid rgba(255,71,87,0.3); }}
  .alto    {{ background: rgba(255,165,2,0.15); color: #ffc04d;
               border: 1px solid rgba(255,165,2,0.3); }}
  .medio   {{ background: rgba(255,215,0,0.12); color: #ffd700;
               border: 1px solid rgba(255,215,0,0.25); }}
  .bajo    {{ background: rgba(0,229,160,0.12); color: #00e5a0;
               border: 1px solid rgba(0,229,160,0.25); }}

  /* HEADER REPORT */
  .report-header {{
    background: var(--bg2); border: 1px solid var(--border);
    border-radius: 16px; padding: 36px 40px; margin-bottom: 48px;
  }}
  .report-meta {{
    display: flex; gap: 24px; flex-wrap: wrap; margin-top: 16px;
  }}
  .report-meta span {{
    font-size: 12px; color: var(--text3);
    font-family: monospace; letter-spacing: 0.5px;
  }}
  .report-meta span b {{ color: var(--text2); font-weight: 500; }}

  @media (max-width: 640px) {{
    .page-wrap {{ padding: 32px 20px 60px; }}
    h1 {{ font-size: 28px; }}
    h2 {{ font-size: 18px; }}
  }}
</style>
</head>
<body>
<div class="page-wrap">
  <div class="report-header">
    <h1>Informe Ejecutivo de Ciberseguridad</h1>
    <div class="report-meta">
      <span><b>Generado por:</b> AuditAI Multi-Agente</span>
      <span><b>Normativas:</b> ISO 27001 · ENS · GDPR · NIS2 · PCI-DSS</span>
      <span><b>Motor:</b> CrewAI + Ollama</span>
    </div>
  </div>
  {body}
</div>
<script>
  // Wrap tables for horizontal scroll
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


# ──────────────────────────────────────────
# ENDPOINTS
# ──────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index():
    """Sirve el frontend."""
    html_path = Path("/app/static/index.html")
    if html_path.exists():
        return HTMLResponse(html_path.read_text(encoding="utf-8"))
    return HTMLResponse("<h1>AuditAI</h1><p>Falta el archivo /app/static/index.html</p>")


@app.get("/api/evidencias")
async def listar_evidencias():
    """Lista los archivos que ya están en la carpeta /app/evidencias."""
    archivos = []
    for f in EVIDENCIAS_DIR.iterdir():
        if f.is_file():
            archivos.append({
                "nombre": f.name,
                "tamaño": f.stat().st_size,
                "modificado": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
            })
    return {"archivos": sorted(archivos, key=lambda x: x["nombre"])}


@app.post("/api/evidencias/upload")
async def subir_evidencias(files: list[UploadFile] = File(...)):
    """Sube archivos nuevos a /app/evidencias."""
    subidos = []
    for file in files:
        dest = EVIDENCIAS_DIR / file.filename
        content = await file.read()
        dest.write_bytes(content)
        subidos.append({"nombre": file.filename, "tamaño": len(content)})
    return {"subidos": subidos}


@app.delete("/api/evidencias/{nombre}")
async def borrar_evidencia(nombre: str):
    """Elimina un archivo de evidencias."""
    path = EVIDENCIAS_DIR / nombre
    if not path.exists():
        raise HTTPException(404, "Archivo no encontrado")
    path.unlink()
    return {"ok": True}


@app.post("/api/analizar")
async def iniciar_analisis():
    """Lanza el análisis en background y devuelve un job_id."""
    archivos = [f for f in EVIDENCIAS_DIR.iterdir() if f.is_file()]
    if not archivos:
        raise HTTPException(400, "No hay archivos en la carpeta de evidencias.")

    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "estado": "starting",
        "agente_actual": None,
        "agente_nombre": None,
        "agente_estado": None,
        "agente_idx": -1,
        "total_agentes": 7,
        "mensaje": "Preparando agentes…",
        "error": None,
        "informe_md": None,
        "informe_html": None,
        "fecha": None,
    }
    threading.Thread(target=run_analysis, args=(job_id,), daemon=True).start()
    return {"job_id": job_id}


@app.get("/api/estado/{job_id}")
async def estado_job(job_id: str):
    """Polling del estado de un job."""
    if job_id not in jobs:
        raise HTTPException(404, "Job no encontrado")
    job = jobs[job_id]
    return {
        "estado":        job["estado"],           # starting | running | done | error
        "agente_idx":    job["agente_idx"],
        "agente_nombre": job["agente_nombre"],
        "agente_estado": job["agente_estado"],
        "total_agentes": job["total_agentes"],
        "mensaje":       job["mensaje"],
        "error":         job.get("error"),
        "fecha":         job.get("fecha"),
    }


@app.get("/api/informe/{job_id}/html", response_class=HTMLResponse)
async def obtener_informe_html(job_id: str):
    """Devuelve el informe como HTML."""
    if job_id not in jobs:
        raise HTTPException(404, "Job no encontrado")
    job = jobs[job_id]
    if job["estado"] != "done":
        raise HTTPException(400, "El informe aún no está listo")
    return HTMLResponse(job["informe_html"])


@app.get("/api/informe/{job_id}/md")
async def obtener_informe_md(job_id: str):
    """Devuelve el informe como Markdown."""
    if job_id not in jobs:
        raise HTTPException(404, "Job no encontrado")
    job = jobs[job_id]
    if job["estado"] != "done":
        raise HTTPException(400, "El informe aún no está listo")
    return {"markdown": job["informe_md"]}


@app.get("/api/informe/ultimo/html", response_class=HTMLResponse)
async def ultimo_informe_html():
    """Devuelve el último informe guardado en disco (si existe)."""
    path = DB_DIR / "informe_final.html"
    if not path.exists():
        raise HTTPException(404, "No hay informe generado todavía")
    return HTMLResponse(path.read_text(encoding="utf-8"))


@app.get("/api/informe/ultimo/descargar")
async def descargar_ultimo_informe():
    """Descarga el último informe HTML como archivo."""
    path = DB_DIR / "informe_final.html"
    if not path.exists():
        raise HTTPException(404, "No hay informe generado todavía")
    return FileResponse(
        path, media_type="text/html",
        filename=f"auditoria_{datetime.now().strftime('%Y%m%d')}.html"
    )
