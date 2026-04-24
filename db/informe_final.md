**

# 📄 Reporte Ejecutivo de Riesgos de Seguridad  
**Destinatarios:** CISO, DPO y Dirección General  
**Fecha:** 24 abril 2026  

---  

## 1️⃣ Resumen Ejecutivo  

Durante la última auditoría de seguridad (abril 2026) se identificaron ocho riesgos críticos para la confidencialidad, integridad y disponibilidad de la Cardholder Data Environment (CDE) y de los sistemas operacionales (OT). La evaluación se realizó contra los requisitos de **NIS2** y **PCI‑DSS**.  

- **Riesgos críticos (2):** Vulnerabilidad sin parchear en el firewall (CVE‑2023‑XXXXX) y ausencia total de política de seguridad de la información.  
- **Riesgos altos (3):** Uso de TLS 1.0, falta de segmentación OT‑IT y ausencia de IDS/IPS.  
- **Riesgos medios (3):** Deficiencias en notificación de incidentes, registro insuficiente de incidentes y logs de auditoría incompletos.  

Los riesgos críticos deben ser mitigados **inmediatamente (< 7 días)**; los de alta prioridad en **≤ 30 días** y los de nivel medio en **≤ 90 días**. El plan de acción está estructurado en tres ventanas temporales (0‑30 d, 30‑90 d, 90‑180 d) con responsables, entregables y KPIs de seguimiento.

---  

## 2️⃣ Tabla Consolidada de Riesgos y Criticidad  

| # | Riesgo (descripción) | Evidencia (archivo y hallazgo) | Requisito NIS2 / PCI‑DSS asociado | Criticidad | Justificación de la criticidad | Acción recomendada (prioridad) |
|---|----------------------|--------------------------------|-----------------------------------|------------|--------------------------------|--------------------------------|
| **1** | **Vulnerabilidad crítica sin parchear en el firewall** (CVE‑2023‑XXXXX) | `network_report.txt – Finding 1` – “Unpatched vulnerability CVE‑2023‑XXXXX on firewall (risk: high)” | NIS2 Art. 14 – Gestión de riesgos y medidas técnicas adecuadas  <br>PCI‑DSS Req 1.1.1 – Configuración segura del firewall | **Crítico** | Permite acceso no autorizado a la red, comprometiendo disponibilidad, integridad y confidencialidad de la CDE. Un exploit puede afectar toda la zona de datos de tarjetas. | Aplicar el parche inmediatamente y establecer proceso de gestión de vulnerabilidades (Req 6.1). |
| **2** | **Uso de cifrado obsoleto (TLS 1.0) en conexiones externas** | `network_report.txt – Finding 2` – “Weak encryption (TLS 1.0) on external connections” | NIS2 Art. 14 – Uso de protocolos seguros  <br>PCI‑DSS Req 4.1 – Cifrado fuerte (TLS 1.2 o superior) | **Alto** | TLS 1.0 vulnerable a ataques de downgrade y descifrado; exposición de datos de tarjetas en tránsito. | Desactivar TLS 1.0, habilitar TLS 1.2+ en todos los servicios externos y validar con escaneos de seguridad. |
| **3** | **Falta de segmentación entre redes OT e IT** | `network_report.txt – Finding 3` – “No segmentation between OT and IT networks” | NIS2 Art. 14 – Segmentación de redes críticas  <br>PCI‑DSS Req 1.2.1 – Aislamiento de la CDE | **Alto** | Un compromiso en OT puede propagarse a IT y a la CDE, ampliando la superficie de ataque. | Diseñar e implementar arquitectura de segmentación (firewalls internos, VLANs, Zero‑Trust). |
| **4** | **Ausencia de sistema de detección/previsión de intrusiones (IDS/IPS)** | `network_report.txt – Finding 4` – “Lack of intrusion detection system (IDS) monitoring” | NIS2 Art. 14 – Detección y respuesta a incidentes  <br>PCI‑DSS Req 11.4 – Implementar IDS/IPS | **Alto** | Impide detección temprana de actividades maliciosas, aumentando tiempo de exposición y daño potencial. | Desplegar solución IDS/IPS con correlación de eventos, integrar con SIEM. |
| **5** | **Deficiencia en la notificación de incidentes a la autoridad competente** | `incident_log.json – INC001` y `INC002` – No se evidencia registro de notificación a la autoridad ni cumplimiento del plazo de 24 h | NIS2 Art. 16 – Notificación de incidentes dentro de 24 h  <br>PCI‑DSS Req 12.10 – Notificación a entidades adquirentes y bancos | **Medio** | Incumple obligación legal y dificulta coordinación sectorial. | Formalizar proceso de notificación, entrenar personal y probar flujo dentro de 24 h. |
| **6** | **Registro de incidentes insuficiente (falta de análisis de causa raíz y lecciones aprendidas)** | `incident_log.json – INC002` – “response: Isolated affected system, restored from backup” (sin RCA ni plan de mejora) | NIS2 Art. 16 – Registro y lecciones aprendidas  <br>PCI‑DSS Req 12.10 – Documentación de lecciones aprendidas | **Medio** | Sin RCA ni plan de mejora, se repite la misma vulnerabilidad. | Ampliar registros para incluir RCA, acciones correctivas y seguimiento. |
| **7** | **Política de seguridad de la información inexistente o insuficiente** | `policy_doc.pdf` – Contenido solo “Policy Document” sin detalle de políticas, roles, procedimientos ni planes de continuidad | NIS2 Art. 13 – Existencia de políticas de seguridad  <br>PCI‑DSS Req 12.1 – Política de seguridad de la información | **Crítico** | Impide demostrar cumplimiento, asignar responsabilidades y guiar la implementación de controles. | Redactar y publicar política completa, aprobar por alta dirección y difundir. |
| **8** | **Registros de auditoría y monitoreo de accesos a la CDE insuficientes** | `incident_log.json` – No se muestra registro de accesos a la CDE ni de logs de eventos de seguridad | PCI‑DSS Req 10.2 – Registro y monitoreo de accesos a datos de tarjetas  <br>PCI‑DSS Req 10.5 – Retención de logs 12 meses | **Medio** | Sin logs detallados no se puede demostrar trazabilidad ni detección de actividades sospechosas. | Configurar logging completo, centralizar en SIEM, retener ≥12 meses y revisar periódicamente. |

---  

## 3️⃣ Plan de Acción Priorizado  

| Horizonte Temporal | Riesgo(s) | Acción concreta | Responsable | Entregable | KPI de cumplimiento |
|--------------------|----------|-----------------|--------------|------------|----------------------|
| **0‑30 d** (Urgente) | 1, 7 | • Aplicar parche CVE‑2023‑XXXXX al firewall (verificar con escaneo posterior).<br>• Redactar Política de Seguridad de la Información (alcance, roles, procesos, continuidad).<br>• Aprobar política por Comité de Dirección y publicar en intranet. | CISO / Equipo de Infraestructura <br> CISO / Legal & Compliance | - Parche aplicado y validado.<br>- Política firmada y disponible. | - % de parches críticos aplicados (objetivo 100%).<br>- Política publicada y firmada (objetivo 100%). |
| **30‑90 d** (Rápido) | 2, 3, 4, 5, 6, 8 | • Desactivar TLS 1.0 y habilitar TLS 1.2+ en todos los servidores externos.<br>• Diseñar arquitectura de segmentación OT‑IT (firewalls internos, VLANs, ACLs).<br>• Implementar IDS/IPS (ej. Snort, Suricata) y conectar al SIEM.<br>• Formalizar proceso de notificación a autoridad (plantilla, flujo, pruebas de tiempo <24 h).<br>• Extender registro de incidentes con RCA y plan de mejora.<br>• Configurar logging completo de accesos a la CDE, centralizar en SIEM, retener 12 meses. | Arquitectura de Seguridad <br>Equipo OT/IT <br>Equipo SOC <br>Compliance Officer <br>Incident Response Lead <br>Equipo de Logging | - Configuración TLS verificada por escáner SSL Labs.<br>- Diagrama de segmentación aprobado y firewalls configurados.<br>- IDS/IPS en producción, alertas en SIEM.<br>- Procedimiento de notificación probado (simulación).<br>- Plantilla RCA completada en al menos 2 incidentes.<br>- Logs de CDE almacenados 12 meses en SIEM. | - % de servicios con TLS 1.2+ (objetivo 100%).<br>- Tiempo medio de detección de intrusión (MTTD) < 5 min.<br>- Tiempo de notificación a autoridad < 24 h en pruebas.<br>- % de incidentes con RCA documentada (objetivo 100%). |
| **90‑180 d** (Optimización) | Ninguno nuevo, pero se revisan los riesgos medios para **cierre** y **mejora continua** | • Realizar auditoría interna de cumplimiento NIS2/PCI‑DSS (ciclo trimestral).<br>• Ejecutar pruebas de penetración externas para validar mitigaciones.<br>• Implementar programa de concienciación y entrenamiento continuo (phishing, manejo de datos). | Auditoría Interna <br>Equipo Red Team <br>HR & Seguridad | - Informe de auditoría con hallazgos < 5 % residual.<br>- Reporte de pentest con vulnerabilidades críticas < 0.<br>- 90 % de empleados completaron entrenamiento. | - % de hallazgos críticos remediados (objetivo 100%).<br>- Índice de participación en entrenamiento (>90%). |

> **Nota:** Cada acción incluye una **fecha límite** y un **owner** claramente definido para asegurar rendición de cuentas.

---  

## 4️⃣ Indicadores Clave de Rendimiento (KPIs)  

| KPI | Fórmula / Métrica | Frecuencia de Medición | Umbral objetivo |
|-----|-------------------|------------------------|-----------------|
| **% de parches críticos aplicados** | (Parche críticos aplicados / Total parches críticos) × 100 | Semanal | ≥ 100 % en 7 d |
| **Tiempo medio de notificación a autoridad (MTTN)** | Σ (tiempo real - tiempo de incidente) / Nº incidentes notificados | Mensual | ≤ 24 h |
| **% de servicios con TLS 1.2+** | (Servicios con TLS 1.2+ / Total servicios externos) × 100 | Mensual | 100 % |
| **MTTD (Mean Time To Detect) IDS/IPS** | Σ (tiempo detección - tiempo ataque) / Nº alertas válidas | Diario | ≤ 5 min |
| **% de incidentes con RCA documentada** | (Incidentes con RCA / Total incidentes) × 100 | Trimestral | 100 % |
| **Retención de logs CDE (meses)** | Meses de logs almacenados en SIEM | Mensual | ≥ 12 meses |
| **Índice de cumplimiento NIS2/PCI‑DSS** | (Controles implementados / Controles requeridos) × 100 | Trimestral | ≥ 95 % |
| **Participación en entrenamiento de seguridad** | (Empleados entrenados / Total empleados) × 100 | Trimestral | ≥ 90 % |

---  

## 5️⃣ Conclusiones y Recomendaciones Ejecutivas  

1. **Riesgos críticos (1 y 7) requieren acción inmediata** – la falta de parche y de política de seguridad son brechas que pueden generar sanciones regulatorias y pérdidas financieras significativas.  
2. **Los riesgos altos (2‑4) son vulnerabilidades explotables que deben ser mitigadas antes de que se materialicen ataques dirigidos**; la segmentación OT‑IT y la detección de intrusiones son pilares de una arquitectura resiliente.  
3. **Los riesgos medios (5‑8) impactan la capacidad de respuesta y la evidencia de cumplimiento**; su remediación fortalecerá la gobernanza y la auditoría continua.  
4. **El plan de acción está alineado con los plazos de NIS2 (notificación 24 h) y PCI‑DSS (retención de logs 12 meses, gestión de vulnerabilidades, política de seguridad)**, garantizando que la organización cumpla con ambas normativas.  
5. **Se recomienda establecer un Comité de Seguridad (CISO, DPO, CTO, Legal) que supervise la ejecución del plan, revise los KPIs y autorice recursos adicionales**.  

> **Próximo paso:** El CISO presentará este reporte en la reunión de la Junta Directiva el **30 abril 2026** para validar los recursos y la asignación de responsables.  

---  

*Fin del reporte.*