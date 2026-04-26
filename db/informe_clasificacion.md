**  

---

## 1️⃣ Registro Unificado de Riesgos (14 riesgos)

| # | ID Riesgo | Descripción (transversal) | Normativas afectadas | Categoría / Dominio | **Criticidad** (1‑5) | Probabilidad (1‑5) | Impacto (1‑5) | **Score** = (C × P × I)/5 (1‑25) | Madurez (1‑5) | Transversal |
|---|----------|----------------------------|----------------------|--------------------|----------------------|--------------------|---------------|-----------------------------------|--------------|-------------|
| 1 | R‑POL‑01 | Falta de Política de Seguridad Integral (no existe documento que cubra todos los ámbitos) | ENS C1, PCI‑DSS Req 12 | Gobernanza / Política | 5 (Crítico) | 4 | 5 | **20** | 1 | Sí |
| 2 | R‑RISK‑02 | Ausencia de proceso formal de Gestión de Riesgos (no hay metodología ni informe) | ENS C4 | Gobernanza / Riesgo | 5 | 4 | 5 | **20** | 1 | Sí |
| 3 | R‑DATA‑03 | Protección insuficiente de datos personales y de titulares de tarjeta (registro de tratamiento incompleto, sin cifrado en reposo) | ENS C5, PCI‑DSS Req 3 | Protección de Datos | 5 | 4 | 5 | **20** | 1 | Sí |
| 4 | R‑INC‑04 | Falta de Plan de Respuesta a Incidentes y pruebas de seguridad continuas | ENS C8, PCI‑DSS Req 11 | Gestión de Incidentes | 5 | 4 | 5 | **20** | 1 | Sí |
| 5 | R‑CONT‑05 | Ausencia de Plan de Continuidad del Negocio y pruebas de recuperación | ENS C9 | Continuidad del Negocio | 4 (Alto) | 3 | 4 | **10** | 1 | No |
| 6 | R‑ACC‑06 | Control de Acceso deficiente (sin política, sin principio de mínimo privilegio, sin revisiones) | ENS C6, PCI‑DSS Req 7‑8 | Control de Acceso | 4 | 4 | 5 | **16** | 2 | Sí |
| 7 | R‑PASS‑07 | Política de Contraseñas incompleta y ausencia de gestión de contraseñas predeterminadas | ENS C7, PCI‑DSS Req 2 | Gestión de Credenciales | 3 (Medio) | 3 | 4 | **7** | 2 | Sí |
| 8 | R‑FW‑08 | Falta de firewall y segmentación de red / protección de comunicaciones (sin reglas, sin cifrado TLS) | PCI‑DSS Req 1, ENS C10 | Infraestructura / Red | 5 | 4 | 5 | **20** | 1 | Sí |
| 9 | R‑VULN‑09 | Gestión de vulnerabilidades y parches insuficiente (sin escaneos regulares, sin proceso de remediación) | ENS C11, PCI‑DSS Req 5‑6 | Vulnerabilidad | 4 | 4 | 5 | **16** | 2 | Sí |
|10 | R‑LOG‑10 | Registro y monitorización de logs incompletos (sin política de retención, sin SIEM) | ENS C12, PCI‑DSS Req 10 | Auditoría / Monitoreo | 4 | 4 | 5 | **16** | 2 | Sí |
|11 | R‑COMM‑11 | Protección de comunicaciones en tránsito insuficiente (sin TLS, sin VPN) | ENS C10, PCI‑DSS Req 4 | Seguridad de la Información | 3 | 3 | 4 | **7** | 1 | Sí |
|12 | R‑PHYS‑12 | Falta de controles de seguridad física (acceso a salas, CCTV) | PCI‑DSS Req 9 | Seguridad Física | 3 | 2 | 3 | **4** | 1 | No |
|13 | R‑MAL‑13 | Ausencia de protección anti‑malware y actualizaciones de firmas | PCI‑DSS Req 5 | Seguridad de End‑Points | 4 | 3 | 4 | **10** | 1 | No |
|14 | R‑DEV‑14 | Falta de proceso de desarrollo seguro (SDLC, pruebas de código, gestión de versiones) | PCI‑DSS Req 6 | Seguridad de Aplicaciones | 4 | 3 | 4 | **10** | 1 | No |

### 1.1️⃣ Top 10 Riesgos críticos (Score descendente)

| Rank | ID | Descripción | Score |
|------|----|--------------|-------|
| 1 | R‑POL‑01 | Falta de Política de Seguridad Integral | **20** |
| 2 | R‑RISK‑02 | Ausencia de Gestión de Riesgos | **20** |
| 3 | R‑DATA‑03 | Protección insuficiente de datos personales y de tarjetas | **20** |
| 4 | R‑INC‑04 | Falta de Plan de Respuesta a Incidentes | **20** |
| 5 | R‑FW‑08 | Falta de firewall y segmentación de red | **20** |
| 6 | R‑ACC‑06 | Control de Acceso deficiente | **16** |
| 7 | R‑VULN‑09 | Gestión de vulnerabilidades y parches insuficiente | **16** |
| 8 | R‑LOG‑10 | Registro y monitorización de logs incompleta | **16** |
| 9 | R‑CONT‑05 | Ausencia de Plan de Continuidad del Negocio | **10** |
|10 | R‑MAL‑13 | Ausencia de protección anti‑malware | **10** |

---

## 2️⃣ Métricas Globales

| Métrica | Valor |
|---------|-------|
| **Número total de riesgos** | 14 |
| **Exposición total (suma de scores)** | **196** |
| **Score medio** | 14 ≈ (196 / 14) |
| **Madurez media (1‑5)** | **1.3** |
| **% de riesgos críticos (Score ≥ 15)** | 35 % (5 de 14) |
| **% de riesgos transversales** | 71 % (10 de 14) |

### 2.1 Distribución de riesgos por dominio

| Dominio | Nº Riesgos | % del total |
|---------|------------|-------------|
| Gobernanza / Política | 2 | 14 % |
| Gestión de Riesgos | 1 | 7 % |
| Protección de Datos | 2 | 14 % |
| Control de Acceso | 2 | 14 % |
| Infraestructura / Red | 2 | 14 % |
| Vulnerabilidad / Parches | 1 | 7 % |
| Auditoría & Monitoreo | 1 | 7 % |
| Continuidad del Negocio | 1 | 7 % |
| Seguridad Física | 1 | 7 % |
| Seguridad de End‑Points | 1 | 7 % |
| Desarrollo Seguro | 1 | 7 % |

---

## 3️⃣ Recomendaciones de Priorización (basado en Score y madurez)

| Prioridad | Acción clave | Riesgos asociados | Horizonte |
|-----------|--------------|------------------|------------|
| **1** | **Definir y publicar una Política de Seguridad Integral** (R‑POL‑01) y **formalizar la Gestión de Riesgos** (R‑RISK‑02). | R‑POL‑01, R‑RISK‑02 | ≤ 90 días |
| **2** | **Implementar controles de firewall, segmentación y cifrado de comunicaciones** (R‑FW‑08, R‑COMM‑11). | R‑FW‑08, R‑COMM‑11 | ≤ 120 días |
| **3** | **Crear Plan de Respuesta a Incidentes y pruebas de seguridad continuas** (R‑INC‑04). | R‑INC‑04 | ≤ 120 días |
| **4** | **Establecer Control de Acceso basado en mínimo privilegio y revisiones trimestrales** (R‑ACC‑06). | R‑ACC‑06 | ≤ 150 días |
| **5** | **Completar registro de tratamiento de datos personales y aplicar cifrado en reposo** (R‑DATA‑03). | R‑DATA‑03 | ≤ 180 días |
| **6** | **Desarrollar Plan de Continuidad del Negocio y pruebas de recuperación** (R‑CONT‑05). | R‑CONT‑05 | ≤ 180 días |
| **7** | **Implementar proceso de gestión de vulnerabilidades y parcheo** (R‑VULN‑09). | R‑VULN‑09 | ≤ 180 días |
| **8** | **Definir política de logs, retención 12 meses y despliegue de SIEM** (R‑LOG‑10). | R‑LOG‑10 | ≤ 180 días |
| **9** | **Completar política de contraseñas y eliminar credenciales predeterminadas** (R‑PASS‑07). | R‑PASS‑07 | ≤ 180 días |
| **10**| **Implementar controles de seguridad física y anti‑malware** (R‑PHYS‑12, R‑MAL‑13). | R‑PHYS‑12, R‑MAL‑13 | ≤ 210 días |
| **11**| **Adoptar proceso de desarrollo seguro (SDLC, pruebas de código)** (R‑DEV‑14). | R‑DEV‑14 | ≤ 210 días |

---

## 4️⃣ Plan de Acción Resumido (90 / 180 / 210 días)

| Etapa | Actividades principales | Responsable | Entregables |
|-------|------------------------|-------------|-------------|
| **0‑30 d** | - Reunión de arranque con Comité de Seguridad.<br>- Inventario de activos críticos.<br>- Designación de Responsable de Seguridad (RS). | Comité de Seguridad / RS | Acta de arranque, lista de activos, nombramiento RS |
| **30‑90 d** | - Redacción y aprobación de Política de Seguridad (R‑POL‑01).<br>- Definición de metodología de gestión de riesgos (R‑RISK‑02).<br>- Selección e instalación de firewall perimetral y reglas básicas. | RS, Equipo de Infraestructura | Política aprobada, documento de metodología, firewall operativo |
| **90‑150 d** | - Elaboración del Plan de Respuesta a Incidentes (R‑INC‑04).<br>- Implementación de control de acceso (roles, MFA).<br>- Completar registro de tratamiento de datos (R‑DATA‑03). | RS, Equipo de Seguridad, DPO | PRI documentado, matriz de roles, registro de tratamiento actualizado |
| **150‑180 d** | - Desarrollo del Plan de Continuidad del Negocio (R‑CONT‑05).<br>- Implantación de proceso de gestión de vulnerabilidades (R‑VULN‑09).<br>- Política de logs y despliegue de SIEM (R‑LOG‑10). | RS, Equipo de Operaciones | PCN, informe de escaneos, SIEM configurado |
| **180‑210 d** | - Revisión y cierre de políticas de contraseñas, seguridad física y anti‑malware.<br>- Implementación de SDLC seguro (R‑DEV‑14).<br>- Auditoría interna de cumplimiento (ENS + PCI). | RS, Equipo de Desarrollo, Auditoría Interna | Políticas finales, checklist de SDLC, informe de auditoría |

---

## 5️⃣ Conclusión Ejecutiva

- **Exposición total 196** indica un nivel de riesgo **alto** y una **madurez organizacional de 1.3/5**, lo que evidencia que la mayoría de los controles críticos están ausentes o solo parcialmente implementados.  
- **10 de 14 riesgos (71 %) son transversales**, afectando a más de una normativa; su mitigación simultánea genera sinergias de cumplimiento (p.ej., una política de seguridad única cubre ENS, PCI‑DSS y ISO 27001).  
- **Los 5 riesgos con Score = 20** son los que deben ser abordados primero, pues combinan criticidad máxima, alta probabilidad y gran impacto.  
- La hoja de ruta propuesta permite **alcanzar un nivel de madurez ≥ 3** en los próximos 6‑7 meses, reduciendo la exposición en **≈ 80 %** (Score estimado < 40) y cumpliendo los requisitos esenciales de ENS y PCI‑DSS, sentando las bases para ISO 27001 y NIST RMF.  

---  

**Próximo paso:** Programar la reunión de arranque con el Comité de Seguridad para validar prioridades, asignar responsables y lanzar la fase de elaboración de la Política de Seguridad (R‑POL‑01).  

---