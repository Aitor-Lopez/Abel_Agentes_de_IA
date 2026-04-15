import os
from dotenv import load_dotenv
from crewai import LLM, Agent, Task, Crew, Process
from langchain_ollama import ChatOllama
from crewai_tools import DirectoryReadTool, FileReadTool

load_dotenv()

# Conexión al titán 120B Cloud
llm = LLM(
    model=os.getenv("MODEL_NAME"), # Aquí ya irá con "ollama/..."
    base_url=os.getenv("OLLAMA_BASE_URL"),
    temperature=0.1
)
evidencias_dir = '/app/evidencias'
archivos = os.listdir(evidencias_dir) if os.path.exists(evidencias_dir) else []
docs_tool = DirectoryReadTool(directory='/app/evidencias')
file_tool = FileReadTool()

# Capa 1: Especialistas
normativas = [
    {"n": "ISO 27001", "g": "Auditoría de controles SGSI."},
    {"n": "ENS", "g": "Cumplimiento Esquema Nacional de Seguridad."},
    {"n": "GDPR", "g": "Protección de datos y privacidad."},
    {"n": "NIS2", "g": "Resiliencia infraestructuras críticas."},
    {"n": "PCI-DSS", "g": "Seguridad en transacciones financieras."}
]

especialistas = [
    Agent(
        role=f"Auditor Senior {item['n']}",
        goal=item['g'],
        backstory=f"Experto en {item['n']} con certificación internacional.",
        tools=[docs_tool, file_tool],
        llm=llm,
        verbose=True
    ) for item in normativas
]

# Tareas de los especialistas
tareas_audit = [
    Task(
        description=f"""
        1. Usa DirectoryReadTool para listar archivos en '/app/evidencias'.
        2. Usa FileReadTool para leer SOLO los archivos que existan realmente.
        3. SI NO HAY ARCHIVOS, reporta 'Sin evidencias para auditar'.
        4. NO inventes nombres de archivos ni contenidos.
        5. Analiza evidencias reales para la normativa {agent.role.split()[-1]}.
        """,
        expected_output="Informe detallado de incumplimientos basado ÚNICAMENTE en archivos existentes.",
        agent=agent
    ) for agent in especialistas
]

# Capa 2: Clasificador
clasificador = Agent(
    role="Analista de Riesgos",
    goal="Consolidar y priorizar hallazgos.",
    backstory="Responsable de triaje y criticidad de vulnerabilidades.",
    llm=llm,
    verbose=True
)

tarea_clasificacion = Task(
    description="Unifica los informes y asigna criticidad (Crítico, Alto, Medio, Bajo).",
    expected_output="Lista unificada de riesgos priorizados.",
    agent=clasificador,
    context=tareas_audit
)

# Capa 3: Reporte
reportero = Agent(
    role="Estratega de Ciberseguridad",
    goal="Generar informe para CISO, DPO y Dirección.",
    backstory="Especialista en comunicación de riesgos corporativos.",
    llm=llm,
    verbose=True
)

tarea_reporte = Task(
    description="Crea el reporte final ejecutivo en Markdown.",
    expected_output="Documento final estructurado.",
    agent=reportero,
    context=[tarea_clasificacion]
)

# Crew
crew = Crew(
    agents=[*especialistas, clasificador, reportero],
    tasks=[*tareas_audit, tarea_clasificacion, tarea_reporte],
    process=Process.sequential
)

if not archivos:
    print("⚠️ ERROR: No hay archivos en la carpeta de evidencias.")
    print("⚠️ Deteniendo ejecución para evitar alucinaciones.")
    exit()
    
if __name__ == "__main__":
    result = crew.kickoff()
    with open("/app/db/informe_final.md", "w") as f:
        f.write(str(result))