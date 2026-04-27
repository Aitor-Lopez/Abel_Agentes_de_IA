**  

---

## 1️⃣ Métricas Globales del Programa de Riesgos  

| Métrica | Valor | Comentario |
|---------|-------|------------|
| **Exposición total (suma de scores)** | **139** | Suma de los scores de todos los riesgos identificados (escala 1‑25). |
| **Madurez del SGSI (1‑5)** | **3** | 20 controles con evidencia de cumplimiento / 36 controles evaluados ≈ 56 % → nivel medio‑alto (3). |
| **Número total de riesgos únicos** | **10** | Tras eliminar duplicidades y agrupar riesgos transversales. |
| **Riesgos críticos (score ≥ 15)** | **8** | Representan el 80 % de la exposición total. |
| **Distribución por dominio** |  • **Acceso y gestión de identidades**: 3  <br>• **Seguridad física**: 2  <br>• **Gestión de activos / documentación**: 4  <br>• **Continuidad / incidentes**: 1 | Permite visualizar áreas con mayor concentración de riesgos. |

---

## 2️⃣ Registro Unificado de Riesgos (ordenado por **Score** descendente)

| # | ID Riesgo | Descripción del Riesgo (transversal) | Normativas Afectadas | Criticidad (1‑5) | Probabilidad (1‑5) | Impacto (1‑5) | **Score (1‑25)** | Estado | Acción Recomendada | Responsable | Plazo |
|---|----------|---------------------------------------|----------------------|------------------|--------------------|---------------|------------------|--------|---------------------|-------------|-------|
| **1** | R‑01 | **Desactivación tardía de cuentas** (cuentas de usuarios y VPN no desactivadas < 24 h). | ISO 27001 A.5.15, ENS 5.15, NIS2 Art. 9‑10 | 5 (Alto) | 4 (Alta) | 5 (Alto) | **20** | Abierto | Automatizar la desactivación mediante integración nómina‑AD; validar en 24 h. | CISO / IT‑Ops | Q2‑2026 |
| **2** | R‑02 | **Punto ciego en videovigilancia del Datacenter** (acceso físico no detectado). | ISO 27001 A.7.4, ENS 7.4, NIS2 Art. 12 | 5 (Crítico) | 4 (Alta) | 5 (Crítico) | **20** | Abierto | Re‑orientar cámara o instalar espejo convexo; validar cobertura 100 %. | Seguridad Física | Q2‑2026 |
| **3** | R‑03 | **Falta de registro de activos** (inventario inexistente). | ISO 27001 A.8.1 | 5 (Alto) | 3 (Media) | 5 (Alto) | **15** | Abierto | Crear inventario de activos con clasificación de información; mantener actualizado. | Gestión de Activos | Q3‑2026 |
| **4** | R‑04 | **Gestión de cuentas de servicio sin evidencia** (privilegios no controlados). | ISO 27001 A.9.3 | 5 (Alto) | 3 (Media) | 5 (Alto) | **15** | Abierto | Documentar todas las cuentas de servicio, aplicar principio de mínimo privilegio y revisiones trimestrales. | Seguridad de Identidades | Q3‑2026 |
| **5** | R‑05 | **Ausencia de controles de seguridad en desarrollo** (SDLC no evidenciado). | ISO 27001 A.14.1 | 5 (Alto) | 3 (Media) | 5 (Alto) | **15** | Abierto | Adoptar Secure Development Lifecycle, registrar pruebas de seguridad y revisiones de código. | Desarrollo Seguro | Q4‑2026 |
| **6** | R‑06 | **Falta de evaluación de la cadena de suministro** (proveedores no evaluados). | ISO 27001 A.15.1 | 5 (Alto) | 3 (Media) | 5 (Alto) | **15** | Abierto | Implementar proceso de due‑diligence de terceros, clasificación de riesgo y monitorización continua. | Compras / Riesgo | Q4‑2026 |
| **7** | R‑07 | **Ausencia de plan de continuidad del negocio (BCP)** y pruebas de recuperación. | ISO 27001 A.17.1 | 5 (Alto) | 3 (Media) | 5 (Alto) | **15** | Abierto | Desarrollar BCP, definir RTO/RPO, ejecutar pruebas de recuperación anual. | Continuidad | Q1‑2027 |
| **8** | R‑08 | **Formalización insuficiente del proceso de gestión de incidentes** (documentación parcial). | ISO 27001 A.16.1, NIS2 Art. 13‑14 | 5 (Alto) | 3 (Media) | 5 (Alto) | **15** | En mitigación | Formalizar procedimiento de notificación a autoridad, establecer SLA de 24 h y pruebas trimestrales. | SOC / CISO | Q3‑2026 |
| **9** | R‑09 | **Política de uso aceptable de activos sin evidencia** (no documentada). | ISO 27001 A.8.2 | 3 (Media) | 3 (Media) | 3 (Media) | **5** | Abierto | Definir política de uso aceptable, comunicar y registrar aceptación de usuarios. | GRC | Q4‑2026 |
| **10** | R‑10 | **Gestión de contraseñas – riesgo residual** (cumple pero sin auditorías continuas). | ISO 27001 A.9.2, ENS Gestión de contraseñas, NIS2 Art. 9‑10 | 3 (Media) | 2 (Baja) | 3 (Media) | **4** | En mitigación | Programar auditorías mensuales de cumplimiento, validar bloqueo y caducidad. | Seguridad de Identidades | Q2‑2026 |

> **Nota:** Los scores se calculan con la fórmula **Score = (Criticidad × Probabilidad × Impacto) / 5**, de modo que el rango máximo es 25.

---

## 3️⃣ Riesgos Transversales Identificados  

| Riesgo Transversal | Controles/Normas Relacionados | Impacto Global |
|--------------------|------------------------------|----------------|
| **Desactivación tardía de cuentas** | ISO 27001 A.5.15, ENS 5.15, NIS2 Art. 9‑10 | Acceso no autorizado prolongado → alta exposición de datos críticos. |
| **Punto ciego en videovigilancia** | ISO 27001 A.7.4, ENS 7.4, NIS2 Art. 12 | Vulnerabilidad física → posible sabotaje o robo de activos. |
| **Falta de documentación de controles críticos** (activos, cuentas de servicio, SDLC, cadena suministro, BCP) | ISO 27001 A.8.1, A.9.3, A.14.1, A.15.1, A.17.1; ENS; NIS2 | Dificulta auditoría, aumenta probabilidad de incumplimiento regulatorio. |
| **Gestión de incidentes incompleta** | ISO 27001 A.16.1, NIS2 Art. 13‑14 | Retraso en notificación y lecciones aprendidas → mayor impacto de incidentes. |

---

## 4️⃣ Distribución de Riesgos por Dominio  

| Dominio | Nº de Riesgos | % del Total |
|---------|---------------|--------------|
| Acceso y gestión de identidades | 3 | 30 % |
| Seguridad física | 2 | 20 % |
| Gestión de activos / documentación | 4 | 40 % |
| Continuidad & gestión de incidentes | 1 | 10 % |

---

## 5️⃣ Recomendaciones Estratégicas para la Dirección  

1. **Priorizar los dos riesgos críticos (R‑01 y R‑02)** – ambos con score 20 y alta probabilidad de materializarse.  
2. **Implementar un programa de “Documentación y Evidencia”** que cubra todos los controles sin evidencia (activos, cuentas de servicio, SDLC, cadena suministro, BCP).  
3. **Establecer un “Marco de Madurez”** basado en el modelo ISO 27001 + ENS + NIS2, con revisiones semestrales para elevar la madurez de 3 a 4.  
4. **Integrar la automatización de desactivación de cuentas** en el flujo de nómina/HRIS y validar con pruebas de penetración internas.  
5. **Actualizar la arquitectura de videovigilancia** y registrar pruebas de cobertura en el BCP.  

---

## 6️⃣ Próximos Pasos (Roadmap de 12 meses)

| Trimestre | Hito | Acción Clave |
|-----------|------|--------------|
| **Q2‑2026** | 1️⃣ Automatizar desactivación de cuentas & auditoría de contraseñas | Implementar script de provisioning, pruebas de cierre < 24 h. |
|           | 2️⃣ Ajustar cámara de videovigilancia | Instalación de espejo convexo, pruebas de cobertura 100 %. |
| **Q3‑2026** | 3️⃣ Inventario de activos y cuentas de servicio | Herramienta CMDB, revisión de privilegios. |
|           | 4️⃣ Formalizar proceso de gestión de incidentes | SOP, SLA 24 h, simulacros trimestrales. |
| **Q4‑2026** | 5️⃣ Definir y publicar políticas de uso aceptable y BCP | Workshops, pruebas de recuperación. |
|           | 6️⃣ Implementar SDLC seguro y evaluación de proveedores | Herramientas SAST/DAST, matriz de riesgo de terceros. |
| **Q1‑2027** | 7️⃣ Re‑evaluación de madurez y reporte al Consejo | Métricas de exposición, score total, plan de mejora continua. |

---

### 📌 Conclusión  

El registro unificado muestra una exposición total de **139 puntos** y una madurez actual de **3/5**. Los **dos riesgos críticos** (desactivación tardía de cuentas y punto ciego de videovigilancia) concentran el 29 % de la exposición y deben ser mitigados con prioridad. La mayor parte de la exposición restante proviene de **deficiencias de documentación** que, aunque no generan un incidente inmediato, aumentan la probabilidad de incumplimiento regulatorio y dificultan la auditoría.  

Al ejecutar el roadmap propuesto y elevar la madurez a nivel 4, la organización reducirá significativamente su exposición, cumplirá con ISO 27001, ENS y NIS2, y ofrecerá al Consejo de Administración una visión clara y accionable del panorama de riesgos.