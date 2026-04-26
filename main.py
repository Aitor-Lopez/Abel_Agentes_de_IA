import os
from dotenv import load_dotenv
from crewai import LLM, Agent, Task, Crew, Process
from crewai_tools import DirectoryReadTool, FileReadTool

load_dotenv()

# ──────────────────────────────────────────────────────────────
#  CONFIGURACIÓN DE RUTAS
# ──────────────────────────────────────────────────────────────
EVIDENCIAS_DIR = os.getenv("EVIDENCES_PATH", "/app/evidencias")
DB_DIR = "/app/db"

os.makedirs(EVIDENCIAS_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)

archivos = [f for f in os.listdir(EVIDENCIAS_DIR) if os.path.isfile(os.path.join(EVIDENCIAS_DIR, f))]

if not archivos:
    print("⚠️  ERROR: No hay archivos en la carpeta de evidencias.")
    print("⚠️  Deteniendo ejecución para evitar alucinaciones.")
    exit(1)

print(f"✅  {len(archivos)} archivo(s) encontrado(s) en evidencias: {archivos}")

# ──────────────────────────────────────────────────────────────
#  LLM
# ──────────────────────────────────────────────────────────────
llm = LLM(
    model=os.getenv("MODEL_NAME"),
    base_url=os.getenv("OLLAMA_BASE_URL"),
    temperature=0.1,
)

# ──────────────────────────────────────────────────────────────
#  HERRAMIENTAS
# ──────────────────────────────────────────────────────────────
docs_tool = DirectoryReadTool(directory=EVIDENCIAS_DIR)
file_tool = FileReadTool()

# ──────────────────────────────────────────────────────────────
#  CAPA 1: AGENTES AUDITORES ESPECIALIZADOS
# ──────────────────────────────────────────────────────────────
normativas = [
    {
        "n": "ISO 27001:2022",
        "g": "Identificar incumplimientos en los 93 controles del Anexo A de ISO 27001:2022, evaluando la gestión de activos, control de accesos, criptografía, seguridad física, gestión de incidentes y continuidad de negocio.",
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
        "g": "Auditar el cumplimiento del Real Decreto 311/2022 (ENS), evaluando las medidas de protección en las categorías BÁSICA, MEDIA y ALTA, con énfasis en los marcos de operación, protección y soporte.",
        "backstory": (
            "Eres un auditor acreditado ENS por el CCN-CERT con experiencia en administraciones públicas, entidades "
            "locales y proveedores de servicios digitales para el sector público español. Conoces en profundidad la "
            "Guía CCN-STIC 808 y las instrucciones técnicas de seguridad. Has participado en más de 40 proyectos de "
            "adecuación ENS y manejas con fluidez las diferencias entre las categorías de seguridad. Priorizas los "
            "marcos de operación (op) y de protección (mp) en tus análisis."
        ),
    },
    {
        "n": "GDPR / RGPD",
        "g": "Verificar el cumplimiento del Reglamento (UE) 2016/679, analizando bases legales de tratamiento, ejercicio de derechos ARCO+, registro de actividades, evaluaciones de impacto (EIPD) y transferencias internacionales.",
        "backstory": (
            "Eres un Data Protection Officer (DPO) certificado con especialización en derecho digital europeo y "
            "ciberseguridad. Has asesorado a más de 60 organizaciones en su adecuación al RGPD y has gestionado "
            "notificaciones de brechas ante la AEPD. Dominas el análisis de flujos de datos, la elaboración de "
            "registros de actividades de tratamiento y el diseño de evaluaciones de impacto (EIPD). En tus informes "
            "siempre citas los artículos específicos del RGPD y las resoluciones de la AEPD relevantes."
        ),
    },
    {
        "n": "NIS2 (Directiva UE 2022/2555)",
        "g": "Evaluar la resiliencia operacional y las obligaciones de gestión de riesgos, notificación de incidentes y seguridad de la cadena de suministro conforme a la Directiva NIS2 y su transposición nacional.",
        "backstory": (
            "Eres un experto en ciberseguridad de infraestructuras críticas y servicios esenciales, con certificación "
            "CISSP y experiencia en sectores como energía, transporte, banca y salud. Has participado en ejercicios "
            "de resiliencia a nivel europeo coordinados por ENISA y conoces en detalle los requisitos de notificación "
            "de incidentes (alertas tempranas en 24h, notificación en 72h, informe final en 1 mes). Tu análisis "
            "siempre evalúa la madurez de la gestión de riesgos, la seguridad de la cadena de suministro y los "
            "planes de continuidad operacional."
        ),
    },
    {
        "n": "PCI-DSS v4.0",
        "g": "Auditar los 12 requisitos de PCI-DSS v4.0 para proteger los datos de tarjetas de pago, evaluando la segmentación de red, cifrado de datos en tránsito y reposo, gestión de vulnerabilidades y controles de acceso.",
        "backstory": (
            "Eres un Qualified Security Assessor (QSA) certificado PCI-DSS con más de 10 años evaluando entornos de "
            "datos de titulares de tarjetas (CDE). Has realizado assessments para bancos, procesadores de pago y "
            "comercios de nivel 1. Conoces a fondo los requisitos de la versión 4.0, especialmente los cambios en "
            "autenticación multifactor, gestión de contraseñas y los nuevos enfoques de cumplimiento personalizados. "
            "Tu análisis siempre incluye el alcance del CDE, los flujos de datos de pago y el estado de las "
            "compensating controls cuando aplica."
        ),
    },
]

especialistas = [
    Agent(
        role=f"Auditor Senior {item['n']}",
        goal=item["g"],
        backstory=item["backstory"],
        tools=[docs_tool, file_tool],
        llm=llm,
        verbose=True,
        max_iter=5,
        memory=False,
    )
    for item in normativas
]

# Tareas de auditoría por normativa
tareas_audit = []
for agent in especialistas:
    norma = agent.role.replace("Auditor Senior ", "")
    tarea = Task(
        description=f"""
Eres el {agent.role}. Sigue estos pasos en orden:

PASO 1 — INVENTARIO DE EVIDENCIAS
Usa la herramienta DirectoryReadTool para listar todos los archivos disponibles en '{EVIDENCIAS_DIR}'.
Anota exactamente qué archivos existen.

PASO 2 — LECTURA DE EVIDENCIAS
Para CADA archivo encontrado en el paso anterior, usa FileReadTool para leer su contenido completo.
Lee todos los archivos: PDFs, TXTs, JSONs, MDs y cualquier otro formato.
Si un archivo no es legible, anótalo como "no accesible" pero continúa con los demás.

PASO 3 — ANÁLISIS DE CUMPLIMIENTO {norma}
Analiza el contenido leído aplicando los controles y requisitos de {norma}. Identifica:
- Controles/requisitos CUMPLIDOS: indica qué evidencia lo demuestra.
- Controles/requisitos INCUMPLIDOS: explica qué falta o qué es deficiente.
- Controles/requisitos SIN EVIDENCIA: aquellos que no pueden evaluarse por falta de documentación.

PASO 4 — CLASIFICACIÓN DE HALLAZGOS
Para cada incumplimiento, asigna:
- Criticidad: Crítico | Alto | Medio | Bajo
- Impacto potencial: descripción concisa del riesgo
- Recomendación específica: acción correctiva concreta

PASO 5 — SÍNTESIS
Si no hay archivos o no hay evidencias relevantes para {norma}, indícalo explícitamente con "SIN EVIDENCIAS PARA ESTA NORMATIVA" y explica qué tipo de documentación sería necesaria.
        """,
        expected_output=f"""
Informe estructurado de auditoría {norma} con las siguientes secciones:

1. RESUMEN EJECUTIVO {norma}: estado global de cumplimiento (%) y principales riesgos
2. EVIDENCIAS ANALIZADAS: lista de archivos leídos y su relevancia
3. HALLAZGOS DE INCUMPLIMIENTO: tabla con ID, descripción, criticidad, impacto y recomendación
4. CONTROLES CUMPLIDOS: controles donde hay evidencia positiva
5. GAPS DE DOCUMENTACIÓN: controles que no pueden evaluarse por falta de evidencias
6. RECOMENDACIONES PRIORITARIAS: top 5 acciones ordenadas por criticidad
        """,
        agent=agent,
    )
    tareas_audit.append(tarea)

# ──────────────────────────────────────────────────────────────
#  CAPA 2: ANALISTA DE RIESGOS (CLASIFICADOR)
# ──────────────────────────────────────────────────────────────
clasificador = Agent(
    role="Analista Senior de Riesgos Corporativos",
    goal=(
        "Consolidar todos los hallazgos de auditoría de las 5 normativas, eliminar duplicidades, "
        "correlacionar riesgos transversales y producir un registro unificado de riesgos priorizado "
        "con métricas de exposición y scores de riesgo residual."
    ),
    backstory=(
        "Eres un Risk Manager certificado CRISC (Certified in Risk and Information Systems Control) "
        "con experiencia en marcos de gestión de riesgos como ISO 31000, FAIR y NIST RMF. Has diseñado "
        "cuadros de mando de riesgos para consejos de administración de compañías del IBEX-35. "
        "Tu valor diferencial es detectar riesgos transversales que afectan a múltiples normativas "
        "simultáneamente y cuantificar su impacto económico potencial. Eres preciso, usas datos "
        "numéricos cuando los hay y siempre distingues entre riesgo inherente y residual."
    ),
    llm=llm,
    verbose=True,
    max_iter=4,
    memory=False,
)

tarea_clasificacion = Task(
    description="""
Analiza los informes de auditoría de ISO 27001, ENS, GDPR, NIS2 y PCI-DSS que te han proporcionado.

PASO 1 — CONSOLIDACIÓN
Reúne todos los hallazgos de incumplimiento de las 5 normativas. Elimina duplicidades
(el mismo problema técnico reportado por múltiples auditores = 1 entrada unificada).

PASO 2 — CORRELACIÓN TRANSVERSAL
Identifica riesgos que afectan a más de una normativa simultáneamente. Por ejemplo:
"Falta de cifrado de datos en reposo" puede incumplir ISO 27001 A.8.24, GDPR Art.32 y PCI-DSS Req.3.
Estos riesgos transversales deben marcarse como CRÍTICOS por su impacto amplificado.

PASO 3 — SCORING DE RIESGOS
Para cada riesgo, asigna:
- Criticidad: Crítico / Alto / Medio / Bajo
- Probabilidad: Alta / Media / Baja
- Impacto: Alto / Medio / Bajo
- Score compuesto (1-25): probabilidad × impacto en escala 1-5
- Normativas afectadas: lista de normativas impactadas
- Plazo recomendado: 0-30d | 30-90d | 90-180d | +180d

PASO 4 — REGISTRO UNIFICADO
Crea el registro consolidado ordenado por Score descendente.

PASO 5 — MÉTRICAS GLOBALES
Calcula:
- Total hallazgos por criticidad
- Distribución por normativa
- Top 3 dominios de riesgo más afectados
- Estimación de nivel de madurez global (1-5)
    """,
    expected_output="""
Registro unificado de riesgos con:
1. MÉTRICAS GLOBALES: dashboard numérico de exposición
2. TOP 10 RIESGOS CRÍTICOS: tabla priorizada con score, normativas afectadas y plazo
3. REGISTRO COMPLETO: todos los hallazgos consolidados con scoring
4. RIESGOS TRANSVERSALES: hallazgos que cruzan múltiples normativas
5. DISTRIBUCIÓN POR DOMINIO: agrupación temática de riesgos (identidad, datos, red, físico, etc.)
    """,
    agent=clasificador,
    context=tareas_audit,
)

# ──────────────────────────────────────────────────────────────
#  CAPA 3A: INFORME TÉCNICO-EJECUTIVO PARA CISO
# ──────────────────────────────────────────────────────────────
agente_ciso = Agent(
    role="Redactor de Informe Técnico para CISO",
    goal=(
        "Generar un informe técnico detallado para el CISO (Chief Information Security Officer) "
        "con todos los hallazgos técnicos, análisis de brechas, métricas de seguridad y "
        "un roadmap de remediación concreto con responsables y KPIs."
    ),
    backstory=(
        "Eres un consultor senior de ciberseguridad con experiencia redactando informes técnicos "
        "para CISOs de grandes corporaciones. Sabes que el CISO necesita profundidad técnica: "
        "quiere ver exactamente qué controles fallan, qué CVEs o vulnerabilidades están expuestas, "
        "qué arquitecturas son deficientes y qué herramientas o procesos hay que implementar. "
        "Tu estilo es directo, usa tablas y listas técnicas, y siempre incluye métricas concretas. "
        "Nunca hablas de 'mejorar la seguridad' sin especificar el QUÉ, CÓMO y CUÁNDO exactos."
    ),
    llm=llm,
    verbose=True,
    max_iter=4,
    memory=False,
)

tarea_informe_ciso = Task(
    description="""
Con base en el registro unificado de riesgos y los informes de auditoría por normativa,
redacta el INFORME TÉCNICO PARA CISO en formato Markdown.

El informe debe ser técnicamente profundo y operacionalmente accionable.

Estructura OBLIGATORIA:

# Informe Técnico de Auditoría Multi-Normativa — CISO
## Metadatos del Informe
(fecha, alcance, normativas cubiertas, nivel de madurez global)

## 1. Resumen Ejecutivo Técnico
- Indicadores de exposición: total hallazgos Crítico/Alto/Medio/Bajo
- Semáforo de cumplimiento por normativa (🔴🟡🟢)
- Los 3 riesgos de mayor impacto inmediato

## 2. Análisis de Brechas por Normativa
Para cada una de las 5 normativas (ISO 27001, ENS, GDPR, NIS2, PCI-DSS):
- Porcentaje estimado de cumplimiento
- Controles/artículos incumplidos con referencia exacta
- Evidencias que soportan cada hallazgo

## 3. Hallazgos Técnicos Consolidados
Tabla completa: ID | Hallazgo | Normativas | Criticidad | Score | Evidencia | Recomendación Técnica

## 4. Análisis de Riesgos Transversales
Riesgos que cruzan múltiples normativas con impacto amplificado

## 5. Arquitectura de Seguridad — Estado Actual vs. Objetivo
Gaps arquitectónicos identificados y controles compensatorios recomendados

## 6. Roadmap de Remediación Técnica
Tabla: Acción | Responsable Técnico | Herramienta/Proceso | Plazo | KPI de Éxito | Normativas que Remedia

### Fase 1 — Inmediato (0-30 días): acciones críticas y quick-wins
### Fase 2 — Corto plazo (30-90 días): mejoras estructurales
### Fase 3 — Medio plazo (90-180 días): madurez y automatización

## 7. KPIs y Métricas de Seguimiento
Métricas técnicas para medir progreso de remediación

## 8. Recursos y Presupuesto Estimado
Esfuerzo estimado en días/persona y herramientas recomendadas

## 9. Conclusiones Técnicas
    """,
    expected_output="Informe técnico completo en Markdown para CISO, con profundidad técnica, tablas detalladas y roadmap accionable.",
    agent=agente_ciso,
    context=[tarea_clasificacion, *tareas_audit],
)

# ──────────────────────────────────────────────────────────────
#  CAPA 3B: INFORME EJECUTIVO PARA CEO / DIRECCIÓN
# ──────────────────────────────────────────────────────────────
agente_ceo = Agent(
    role="Redactor de Informe Ejecutivo para CEO y Dirección",
    goal=(
        "Generar un informe ejecutivo de alto nivel para el CEO, Consejo de Administración y "
        "dirección no técnica, traduciendo los riesgos de seguridad en impacto de negocio, "
        "riesgo reputacional, exposición regulatoria y decisiones estratégicas requeridas."
    ),
    backstory=(
        "Eres un consultor de riesgos corporativos y gobierno de TI con experiencia presentando "
        "ante consejos de administración e inversores. Sabes que el CEO y el consejo no quieren "
        "tecnicismos: quieren entender el impacto en el negocio, las sanciones regulatorias posibles, "
        "el riesgo reputacional y qué decisiones estratégicas necesitan tomar. "
        "Tu lenguaje es claro, usa analogías de negocio cuando es útil, y siempre cuantifica "
        "el impacto económico potencial (multas regulatorias, costes de brecha, impacto en continuidad). "
        "Evitas jerga técnica; cuando la usas, la explicas en términos de negocio."
    ),
    llm=llm,
    verbose=True,
    max_iter=4,
    memory=False,
)

tarea_informe_ceo = Task(
    description="""
Con base en el registro unificado de riesgos y los informes de auditoría,
redacta el INFORME EJECUTIVO PARA CEO Y DIRECCIÓN en formato Markdown.

El informe debe ser claro, conciso y orientado a decisiones de negocio. SIN tecnicismos innecesarios.

Estructura OBLIGATORIA:

# Informe Ejecutivo de Riesgos de Ciberseguridad — Dirección
## Información del Informe
(fecha, nivel de confidencialidad, destinatarios)

## 1. Resumen para la Dirección (máximo 1 página)
- Estado actual de la organización en 3 frases clave
- Semáforo de cumplimiento normativo
- Decisión estratégica más urgente requerida

## 2. Exposición al Riesgo Regulatorio
Para cada normativa, en lenguaje de negocio:
- ¿Qué puede pasar si no se cumple? (multas, sanciones, cese de actividad)
- Cuantificación del riesgo regulatorio:
  * GDPR: hasta 20M€ o 4% facturación global
  * ENS: pérdida de contratos con AAPP
  * NIS2: multas hasta 10M€ o 2% facturación
  * PCI-DSS: revocación de capacidad de procesar pagos con tarjeta
  * ISO 27001: impacto en certificación y contratos

## 3. Impacto Potencial en el Negocio
- Riesgo de continuidad operacional
- Riesgo reputacional y de confianza de clientes
- Impacto económico estimado de una brecha de seguridad
- Ventajas competitivas perdidas por incumplimiento

## 4. Los 5 Riesgos Más Críticos para el Negocio
(Explicados en lenguaje de negocio, sin jerga técnica)
Para cada uno: qué es, qué podría pasar, qué decisión requiere la dirección

## 5. Inversión Requerida vs. Coste del Riesgo
Tabla: Área de Mejora | Inversión Estimada | Riesgo Mitigado | ROI de Seguridad

## 6. Decisiones Estratégicas Requeridas por la Dirección
Lista priorizada de aprobaciones, asignaciones de presupuesto o cambios organizativos
que solo puede tomar la dirección

## 7. Plan de Acción Ejecutivo (Hoja de Ruta a 6 meses)
Timeline visual simplificado de los hitos clave

## 8. Próximos Pasos Inmediatos
Top 3 acciones que deben ocurrir en los próximos 30 días

## 9. Declaración de Responsabilidad
Breve párrafo sobre la responsabilidad de la dirección en el gobierno de la ciberseguridad
    """,
    expected_output="Informe ejecutivo en Markdown para CEO y Dirección, sin tecnicismos, con foco en impacto de negocio, riesgo regulatorio y decisiones estratégicas.",
    agent=agente_ceo,
    context=[tarea_clasificacion],
)

# ──────────────────────────────────────────────────────────────
#  CAPA 3C: INFORME GENERAL / DPO / CUMPLIMIENTO
# ──────────────────────────────────────────────────────────────
agente_general = Agent(
    role="Redactor de Informe General de Cumplimiento Normativo",
    goal=(
        "Generar un informe de cumplimiento normativo integral para el DPO, responsable de "
        "cumplimiento, auditores externos y equipos de legal/compliance, con mapeo detallado "
        "de controles, estado de cumplimiento y plan de acción normativo."
    ),
    backstory=(
        "Eres un especialista en compliance y gobierno corporativo con experiencia en auditorías "
        "externas e internas para organismos reguladores. Has preparado informes de cumplimiento "
        "para la AEPD, el CCN y auditores de certificación ISO. Sabes que el DPO y el equipo de "
        "compliance necesitan trazabilidad completa: cada hallazgo debe enlazarse con el artículo "
        "o control específico, la evidencia que lo soporta y el estado de remediación. "
        "Tu estilo es formal, preciso y documentalmente riguroso. Usas referencias normativas exactas."
    ),
    llm=llm,
    verbose=True,
    max_iter=4,
    memory=False,
)

tarea_informe_general = Task(
    description="""
Con base en el registro unificado de riesgos y los informes de auditoría por normativa,
redacta el INFORME GENERAL DE CUMPLIMIENTO NORMATIVO en formato Markdown.

Este informe es para DPO, compliance officers, auditores externos y equipos de legal.
Debe ser formalmente riguroso, con referencias normativas exactas y trazabilidad completa.

Estructura OBLIGATORIA:

# Informe de Cumplimiento Normativo Multi-Marco — Documento General
## Control del Documento
(versión, fecha, clasificación, elaborado por, revisado por, aprobado por)

## 1. Alcance y Metodología
- Alcance de la auditoría (sistemas, procesos, datos auditados)
- Metodología utilizada
- Normativas y versiones evaluadas
- Limitaciones del análisis

## 2. Estado de Cumplimiento por Normativa
Para cada normativa, tabla de controles:
| Control/Artículo | Descripción | Estado (C/NC/NE/NA) | Evidencia | Observaciones |
(C=Cumple, NC=No Cumple, NE=No Evidencia, NA=No Aplica)

### 2.1 ISO 27001:2022 — Matriz de Controles (Anexo A)
### 2.2 ENS (RD 311/2022) — Medidas de Seguridad
### 2.3 GDPR/RGPD — Artículos Evaluados
### 2.4 NIS2 — Obligaciones de Seguridad
### 2.5 PCI-DSS v4.0 — Requisitos

## 3. Registro de No Conformidades
Tabla: ID-NC | Normativa | Requisito | Descripción | Criticidad | Fecha Detección | Responsable | Estado

## 4. Plan de Acción Correctivo (PAC)
Para cada no conformidad:
- Acción correctiva propuesta
- Responsable designado
- Fecha límite
- Indicador de verificación de cierre
- Estado de implementación

## 5. Análisis de Riesgos para el Registro de Tratamientos (GDPR)
(Si hay datos personales identificados en las evidencias)
- Tratamientos identificados
- Brechas en el registro de actividades
- Evaluaciones de impacto (EIPD) pendientes

## 6. Cadena de Custodia de Evidencias
Lista de todas las evidencias analizadas con hash o identificador, fecha y relevancia

## 7. Declaraciones de Aplicabilidad
Para ISO 27001: controles excluidos y justificación

## 8. Historial de Auditorías Previas
(Si hay información disponible en las evidencias)

## 9. Firmas y Aprobaciones
Sección formal de validación del documento
    """,
    expected_output="Informe formal de cumplimiento normativo en Markdown para DPO/Compliance, con matrices de controles, registro de no conformidades y plan de acción correctivo.",
    agent=agente_general,
    context=[tarea_clasificacion, *tareas_audit],
)

# ──────────────────────────────────────────────────────────────
#  CREW
# ──────────────────────────────────────────────────────────────
crew = Crew(
    agents=[
        *especialistas,
        clasificador,
        agente_ciso,
        agente_ceo,
        agente_general,
    ],
    tasks=[
        *tareas_audit,
        tarea_clasificacion,
        tarea_informe_ciso,
        tarea_informe_ceo,
        tarea_informe_general,
    ],
    process=Process.sequential,
    verbose=True,
)


# ──────────────────────────────────────────────────────────────
#  EJECUCIÓN PRINCIPAL
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🚀 Iniciando análisis multi-agente de ciberseguridad...\n")
    result = crew.kickoff()

    # El resultado final corresponde a la última tarea (informe general).
    # Los resultados de tareas previas se extraen via task.output.
    informes = {
        "ciso": tarea_informe_ciso.output.raw if tarea_informe_ciso.output else str(result),
        "ceo": tarea_informe_ceo.output.raw if tarea_informe_ceo.output else "",
        "general": tarea_informe_general.output.raw if tarea_informe_general.output else str(result),
        "clasificacion": tarea_clasificacion.output.raw if tarea_clasificacion.output else "",
    }

    for nombre, contenido in informes.items():
        if contenido:
            path = os.path.join(DB_DIR, f"informe_{nombre}.md")
            with open(path, "w", encoding="utf-8") as f:
                f.write(contenido)
            print(f"✅  Informe guardado: {path}")

    print("\n✅  Análisis completado. Informes disponibles en /app/db/")
