Resumen del Flujo de Trabajo
Inicio: El script carga configuración y conecta con la IA.
Lectura: Los agentes "Especialistas" leen los archivos de /app/evidencias.
Análisis: Cada especialista revisa los archivos bajo su propia norma (ISO, GDPR, etc.) y genera informes parciales.
Consolidación: El "Analista de Riesgos" toma todos esos informes parciales, los junta y decide cuáles son críticos.
Redacción: El "Estratega" toma la lista priorizada y escribe un informe bonito y ejecutivo en Markdown.
Fin: El informe se guarda en informe_final.md.
docker-compose up --build