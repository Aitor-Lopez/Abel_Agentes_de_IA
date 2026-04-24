**

# 📊 Reporte Ejecutivo de Riesgos de Ciberseguridad  
*Destinatarios: CISO, DPO y Dirección General*  
*Fecha: 24‑04‑2026*  

---  

## 1️⃣ Resumen Ejecutivo  

Durante la fase de auditoría se identificaron **24 hallazgos** distribuidos en cuatro niveles de criticidad (Crítico, Alto, Medio, Bajo). Los riesgos críticos (1‑7) comprometen la **confidencialidad, integridad y disponibilidad** de datos sensibles y generan incumplimientos directos con los marcos regulatorios **ENS, GDPR, PCI‑DSS y NIS2**.  

Los hallazgos críticos se centran en:  

| # | Área afectada | Impacto principal |
|---|---------------|-------------------|
| 1 | Política de contraseñas | Accesos no controlados → violación de GDPR Art. 32 y ENS P5.x |
| 2 | Gestión de incidentes | Falta de notificación → sanciones NIS2 Art. 10‑12 y GDPR Art. 33‑34 |
| 3 | Proceso de gestión de riesgos | Ausencia de marco de riesgo → incumplimiento NIS2 Art. 4‑5 |
| 4 | Política de seguridad integral | Vacíos en hardening, segmentación, cifrado → PCI‑DSS 12.1 |
| 5 | Monitorización y detección | No hay SIEM → imposibilidad de detección temprana (NIS2 Art. 22‑23) |
| 6 | Protección de datos de tarjetas y personales | Cifrado solo en tránsito → incumplimiento PCI‑DSS 3, GDPR Art. 32 |
| 7 | Auditoría y rendición de cuentas | Evidencias incompletas → incumplimiento ENS P9.1 y NIS2 Art. 19‑20 |

**Conclusión rápida:** Si no se mitigan en los próximos 30 días, la organización está expuesta a **multas regulatorias** (hasta 20 M € bajo GDPR), **pérdida de confianza** de clientes y **riesgo de interrupción operativa**.  

---  

## 2️⃣ Tabla Consolidada de Riesgos  

| Nº | Riesgo | Descripción del Incumplimiento | Evidencia | Marco(s) de Referencia | Criticidad |
|----|--------|--------------------------------|-----------|------------------------|------------|
| **1** | **Política de contraseñas insuficiente** | Longitud mínima 6 c, sin complejidad, caducidad 365 d, sin historial. | `politica contraseñas.md` v1.0 + logs de cambio | ENS P5.x, GDPR Art. 25/32, PCI‑DSS 8, NIS2 Art. 6‑7 | **Crítico** |
| **2** | **Gestión de incidentes inexistente** | No hay registro ni notificación de intento sospechoso (24 h). | `logs_registro.txt` (intento sospechoso) + ausencia de proceso | ENS P6.1, GDPR Art. 33‑34, NIS2 Art. 10‑12 | **Crítico** |
| **3** | **Ausencia de proceso de gestión de riesgos** | No existe metodología ni matriz de riesgos. | No hay documento de política o matriz | NIS2 Art. 4‑5 | **Crítico** |
| **4** | **Falta de política de seguridad de la información integral** | Sólo política de contraseñas; falta hardening, segmentación, cifrado, etc. | `politica contraseñas.md` + ausencia de otras políticas | PCI‑DSS 12.1, NIS2 Art. 6‑7 | **Crítico** |
| **5** | **Monitorización y detección insuficientes** | No hay SIEM, correlación ni alertas automáticas; logs limitados. | `logs_registro.txt` (solo autenticación) | NIS2 Art. 22‑23, PCI‑DSS 10.5 | **Crítico** |
| **6** | **Protección de datos de tarjetas y personales insuficiente** | Cifrado solo en tránsito; falta cifrado en reposo y segmentación. | `registro tratamiento.json` (cifrado en tránsito) | PCI‑DSS 3,7; ENS P7.x; GDPR Art. 32; NIS2 | **Crítico** |
| **7** | **Auditoría y rendición de cuentas incompletas** | Informe ISO 27001 sin hallazgos ni plan de acción. | `informe_evidencias_auditoria_iso27001.pdf` | ENS P9.1, NIS2 Art. 19‑20, PCI‑DSS 12.1 | **Crítico** |
| **8** | Control de accesos y segregación de privilegios deficientes | Acceso denegado a recurso confidencial por “guest”; sin revisión periódica. | `logs_registro.txt` | NIS2 Art. 8‑9, PCI‑DSS 8 | **Alto** |
| **9** | Gestión de vulnerabilidades y pruebas de penetración ausentes | No hay escaneos, pruebas ni proceso de parcheo. | No hay evidencia documental | PCI‑DSS 11, NIS2 Art. 7 | **Alto** |
| **10** | Protección contra malware inexistente | No hay solución anti‑malware ni actualizaciones de firmas. | No hay evidencia | PCI‑DSS 5 | **Alto** |
| **11** | Seguridad física no documentada | Falta de registro de acceso físico a salas de servidores. | No hay evidencia | PCI‑DSS 9 | **Alto** |
| **12** | Cadena de suministro sin controles | No hay evaluaciones de proveedores ni cláusulas de seguridad. | No hay evidencia | NIS2 Art. 13‑14 | **Alto** |
| **13** | Consentimiento y bases legales poco claras | Base legal genérica “RGPD” sin Art. 6.x; sin registro de consentimiento. | `registro tratamiento.json` | GDPR Art. 6, 7 | **Alto** |
| **14** | Derechos de los interesados no gestionados | No hay procesos para SAR, rectificación, supresión. | `registro tratamiento.json` sin procedimiento | GDPR Art. 15‑22 | **Alto** |
| **15** | Notificación de brechas de seguridad ausente | No se evidencia notificación a autoridad ni a interesados. | `logs_registro.txt` | GDPR Art. 33‑34, NIS2 Art. 10‑12 | **Alto** |
| **16** | Retención y actualización de registros de tratamiento obsoleta | Última revisión 2022‑12‑01 (>12 meses). | `registro tratamiento.json` | GDPR Art. 30, ENS P7.x | **Alto** |
| **17** | Pruebas de restauración de backups inexistentes | Backup diario, sin pruebas de restauración ni retención segura. | `logs_registro.txt` | ENS P8.1, PCI‑DSS 9, NIS2 Art. 15‑16 | **Alto** |
| **18** | Formación y concienciación en ciberseguridad inexistente | No hay programa de capacitación. | No hay evidencia | NIS2 Art. 21 | **Medio** |
| **19** | Transferencias internacionales no documentadas | Falta de evaluaciones o cláusulas para transferencias fuera del EEE. | No hay evidencia | GDPR Art. 44‑50 | **Medio** |
| **20** | Política de retención de logs insuficiente | Logs no inmutables ni con retención mínima de 1 año. | `logs_registro.txt` | PCI‑DSS 10.5, ENS P10 | **Medio** |
| **21** | Procedimientos de gestión de cambios no formalizados | Cambio de firewall registrado sin proceso de aprobación. | `logs_registro.txt` | NIS2 Art. 7 | **Medio** |
| **22** | Documentación de auditoría ISO 27001 incompleta (sub‑riesgo) | Falta evidencia de auditorías internas/externas completas. | `informe_evidencias_auditoria_iso27001.pdf` | ENS, NIS2 | **Medio** |
| **23** | Ausencia de registro de credenciales predeterminadas | No se evidencia eliminación de credenciales por defecto. | No hay evidencia | PCI‑DSS 2 | **Bajo** |
| **24** | Política de backup sin cifrado | Backup diario sin indicación de cifrado. | `logs_registro.txt` | PCI‑DSS 9, ENS P8 | **Bajo** |

---  

## 3️⃣ Plan de Acción Priorizado  

### ⏱️ 0‑30 Días (Respuesta Inmediata – **Crítico**)  

| Nº | Acción | Responsable | Entregable | KPI de Verificación |
|----|--------|--------------|------------|----------------------|
| 1 | **Revisar y actualizar la política de contraseñas** (mínimo 12 c, complejidad, caducidad 90 d, historial 12) | CISO | Política v2.0 + comunicación a usuarios | % de usuarios con contraseñas conformes (objetivo ≥ 95 %) |
| 2 | **Implementar proceso de gestión de incidentes** (registro, clasificación, notificación 24 h) | DPO + CSIRT | Playbook de incidentes + herramienta ticketing | Tiempo medio de detección → respuesta ≤ 4 h |
| 3 | **Definir y aprobar proceso de gestión de riesgos** (ISO 27005) | CISO | Metodología + Matriz de riesgos inicial | % de activos críticos evaluados (objetivo 100 %) |
| 4 | **Crear política de seguridad de la información integral** (cobertura de hardening, segmentación, cifrado, control de accesos) | CISO | Documento v1.0 + difusión | Cobertura de controles críticos ≥ 90 % |
| 5 | **Instalar y configurar un SIEM básico** (log collection, correlación, alertas) | Equipo de SOC | SIEM en producción (ej. Elastic, Splunk) | Número de alertas críticas generadas → ≥ 1/semana |
| 6 | **Cifrar datos en reposo** (AES‑256) para bases de datos de tarjetas y PII; segmentación de red de datos de pago | Arquitectura de Seguridad | Configuración de cifrado + segmentación VLAN | % de bases cifradas ≥ 100 % |
| 7 | **Completar informe de auditoría ISO 27001** (hallazgos, plan de acción) | Auditor interno | Informe final con evidencias | Evidencias de auditoría completadas (100 %) |

### ⏱️ 30‑90 Días (Mitigación – **Alto**)  

| Nº | Acción | Responsable | Entregable | KPI |
|----|--------|--------------|------------|-----|
| 8 | Revisar y reforzar control de accesos y segregación de privilegios (principio de menor privilegio) | IAM Lead | Matriz de roles + revisión trimestral | % de cuentas con privilegios excesivos ≤ 5 % |
| 9 | Implementar programa de gestión de vulnerabilidades (escaneo trimestral, parcheo 30 d) | Equipo de Infraestructura | Herramienta de escaneo (Nessus) + reporte mensual | Tiempo medio de remediación ≤ 15 d |
|10| Desplegar solución anti‑malware corporativa y actualizar firmas diariamente | SOC | Antivirus empresarial + reporte de detección | % de endpoints protegidos ≥ 100 % |
|11| Documentar y aplicar controles de seguridad física (registro de acceso a salas) | Facilities Manager | Política física + registro digital | Incidentes físicos registrados = 0 |
|12| Evaluar proveedores críticos (cuestionario de seguridad) y añadir cláusulas contractuales | Procurement + DPO | Matriz de riesgos de terceros | % de proveedores críticos evaluados ≥ 80 % |
|13| Formalizar bases legales y registro de consentimientos (GDPR Art. 6) | DPO | Registro de consentimientos actualizado | % de contactos con consentimiento válido ≥ 95 % |
|14| Implementar proceso de gestión de derechos de los interesados (SAR) | DPO | Workflow de solicitudes + SLA 30 d | % de solicitudes atendidas dentro del SLA ≥ 100 % |
|15| Definir proceso de notificación de brechas (autoridad y afectados) | DPO + CSIRT | Plantilla de notificación + pruebas de simulación | Tiempo de notificación ≤ 24 h en pruebas |
|16| Actualizar registro de tratamientos (revisión anual) | DPO | Registro actualizado 2026 | Última revisión ≤ 30 d |
|17| Realizar pruebas de restauración de backups (mensual) | Backup Lead | Informe de pruebas de restauración | % de backups restaurados con éxito ≥ 95 % |
|18| Lanzar programa de concienciación (phishing, buenas prácticas) | HR + SOC | Curso e‑learning + simulaciones | % de empleados completando curso ≥ 90 % |
|19| Documentar transferencias internacionales de datos (DPA, cláusulas) | DPO | Registro de transferencias + acuerdos | % de transferencias con DPA ≥ 100 % |
|20| Definir política de retención de logs (inmutabilidad 1 año) | SOC | Configuración de almacenamiento inmutable | % de logs retenidos ≥ 100 % |
|21| Formalizar proceso de gestión de cambios (CAB) | Change Manager | Procedimiento + registro de cambios aprobados | % de cambios con aprobación formal ≥ 100 % |
|22| Completar documentación de auditoría ISO 27001 (sub‑riesgo) | Auditor interno | Evidencias de auditorías internas/externas | Evidencias completas = 100 % |

### ⏱️ 90‑180 Días (Optimización – **Medio & Bajo**)  

| Nº | Acción | Responsable | Entregable | KPI |
|----|--------|--------------|------------|-----|
|23| Eliminar credenciales predeterminadas y registrar proceso | Infra Lead | Inventario de credenciales + certificación | % de credenciales predeterminadas eliminadas = 100 % |
|24| Implementar cifrado de backups (AES‑256) y validar | Backup Lead | Backups cifrados + pruebas de integridad | % de backups cifrados ≥ 100 % |
|25| Revisar y actualizar política de seguridad física (acceso biométrico) | Facilities | Política revisada + controles instalados | Incidentes físicos = 0 |
|26| Mejorar integración SIEM con herramientas de ticketing y SOAR | SOC | Playbooks automáticos | Reducción del MTTR en un 30 % |
|27| Realizar auditoría externa de cumplimiento (ENS, GDPR, PCI‑DSS) | Auditor externo | Informe de cumplimiento | Nº de hallazgos críticos = 0 |

---  

## 4️⃣ Indicadores Clave de Rendimiento (KPIs)  

| Área | KPI | Fórmula / Métrica | Umbral objetivo |
|------|-----|-------------------|-----------------|
| **Gestión de contraseñas** | % de contraseñas conformes | (Contraseñas que cumplen requisitos / Total usuarios) ×100 | ≥ 95 % |
| **Incidentes** | Tiempo medio de detección (MTTD) | Σ(Tiempo detección) / Nº incidentes | ≤ 4 h |
| **Incidentes** | Tiempo medio de respuesta (MTTR) | Σ(Tiempo resolución) / Nº incidentes | ≤ 24 h |
| **Cifrado** | % de datos críticos cifrados en reposo | (Datos cifrados / Total datos críticos) ×100 | 100 % |
| **Vulnerabilidades** | Tiempo medio de remediación (TMR) | Σ(Días de parcheo) / Nº vulnerabilidades | ≤ 15 d |
| **Formación** | % de empleados capacitados | (Empleados completados / Total empleados) ×100 | ≥ 90 % |
| **Backups** | % de backups restaurados con éxito | (Restauraciones exitosas / Total pruebas) ×100 | ≥ 95 % |
| **Logs** | Retención inmutable de logs | Días de retención inmutable | ≥ 365 d |
| **Gestión de cambios** | % de cambios con aprobación formal | (Cambios aprobados / Total cambios) ×100 | 100 % |
| **Auditoría ISO 27001** | Cobertura de evidencias | (Evidencias entregadas / Evidencias requeridas) ×100 | 100 % |

---  

## 5️⃣ Conclusiones y Recomendaciones Estratégicas  

1. **Prioridad absoluta a los riesgos críticos (0‑30 d).** La falta de políticas básicas (contraseñas, gestión de incidentes, SIEM) expone a la organización a sanciones regulatorias y a pérdidas de datos que pueden afectar la continuidad del negocio.  

2. **Asignación de recursos:**  
   - **Equipo de Seguridad (CISO, SOC, CSIRT)** debe recibir presupuesto inmediato para SIEM, cifrado y herramientas de gestión de vulnerabilidades.  
   - **DPO** liderará la formalización de procesos de notificación, consentimiento y derechos de los interesados.  

3. **Gobernanza:** Establecer un **Comité de Ciberseguridad** con representación del CISO, DPO, CTO y Dirección para seguimiento semanal de los KPIs y revisión de los hitos del plan de acción.  

4. **Cultura de seguridad:** Implementar un programa continuo de concienciación y simulaciones de phishing (mínimo trimestral) para reducir el factor humano, que sigue siendo la mayor superficie de ataque.  

5. **Monitoreo y reporte:** Publicar un **Dashboard ejecutivo** con los KPIs críticos (MTTD, MTTR, % de cumplimiento de políticas) actualizado cada 2 semanas para la alta dirección.  

6. **Revisión legal y contractual:** Actualizar los contratos con proveedores críticos incorporando cláusulas de seguridad y auditorías de terceros, tal como exige NIS2 Art. 13‑14.  

7. **Roadmap a 12 meses:** Tras la fase de 0‑180 días, ejecutar una auditoría externa de cumplimiento (ENS, GDPR, PCI‑DSS) para validar la eliminación de hallazgos críticos y obtener la certificación de conformidad.  

---  

**Próximos pasos inmediatos (próxima semana):**  

- Convocar reunión de arranque del **Comité de Ciberseguridad**.  
- Designar responsables para los 7 riesgos críticos y definir fechas de entrega de evidencias.  
- Aprobar presupuesto para adquisición de SIEM y solución de cifrado de datos en reposo.  

Con la ejecución disciplinada de este plan, la organización no solo alcanzará el cumplimiento regulatorio, sino que fortalecerá su resiliencia frente a amenazas emergentes, protegiendo la confianza de clientes, socios y reguladores.  

---  

*Fin del reporte.*