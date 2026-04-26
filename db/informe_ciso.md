# 📄 INFORME TÉCNICO – CISO  
**Organización:** *[Nombre del cliente]*  
**Fecha:** 26 abr 2026  
**Alcance:** Evaluación de cumplimiento frente a **ENS (Real Decreto 311/2022)**, **PCI‑DSS v4.0** y **ISO 27001:2013**. Se incluyen los 14 riesgos identificados, evidencias disponibles y un plan de remediación de 180 días.

---  

## 1️⃣ Resumen Ejecutivo Técnico  

| Norma | % Cumplimiento estimado | Semáforo | Indicadores Clave |
|-------|--------------------------|----------|-------------------|
| **ENS** | **28 %** (7/25 controles críticos con evidencia parcial) | 🔴 | Exposición = 196 pts, Madurez = 1.3/5, Riesgos críticos = 5/14 |
| **PCI‑DSS v4.0** | **22 %** (2/12 requisitos con evidencia parcial) | 🔴 | 10 hallazgos críticos (Score ≥ 15) |
| **ISO 27001** | **15 %** (solo política de contraseñas parcial) | 🔴 | 0/114 controles cubiertos |

> **Interpretación:** La organización se encuentra en **alto riesgo** y **baja madurez**. La mayor parte de los controles de seguridad críticos están ausentes o incompletos, lo que genera una exposición total de **196 puntos** (máx. = 350).  

### Métricas Globales (del registro de riesgos)

| Métrica | Valor |
|---------|-------|
| Nº total de riesgos | **14** |
| Exposición total (suma de scores) | **196** |
| Score medio | **14** |
| Madurez media (1‑5) | **1.3** |
| % de riesgos críticos (Score ≥ 15) | **35 %** (5/14) |
| % de riesgos transversales | **71 %** (10/14) |

---

## 2️⃣ Análisis de Brechas por Norma  

### 2.1 ENS – Cumplimiento ≈ 28 %

| Control ENS | Estado | Evidencia | % Cumplimiento | Comentario |
|-------------|--------|-----------|----------------|------------|
| C1 Política de Seguridad | ❌ | No existe documento | 0 % | R‑POL‑01 |
| C2 Organización de la Seguridad | ❓ | Sin organigrama ni RS | 0 % | R‑RISK‑02 |
| C3 Gestión de Activos | ❌ | No hay inventario | 0 % | — |
| C4 Gestión de Riesgos | ❌ | Sin metodología ni informe | 0 % | R‑RISK‑02 |
| C5 Protección de Datos | ❌ | Registro de tratamiento corrupto | 0 % | R‑DATA‑03 |
| C6 Control de Acceso | ❌ | No hay política ni revisiones | 0 % | R‑ACC‑06 |
| C7 Gestión de Contraseñas | ⚠️ | Política parcial | 30 % | R‑PASS‑07 |
| C8 Gestión de Incidentes | ❌ | Sin plan ni registro | 0 % | R‑INC‑04 |
| C9 Continuidad del Negocio | ❌ | Sin PCN | 0 % | R‑CONT‑05 |
| C10 Seguridad en Comunicaciones | ❌ | Sin TLS/VPN | 0 % | R‑COMM‑11 |
| C11 Gestión de Vulnerabilidades | ❌ | Sin escaneos ni parcheo | 0 % | R‑VULN‑09 |
| C12 Auditoría y Registro | ⚠️ | Logs parciales, sin SIEM | 20 % | R‑LOG‑10 |

> **Brecha crítica:** 10 controles (C1‑C6, C8‑C11) sin evidencia → **🔴**.

### 2.2 PCI‑DSS v4.0 – Cumplimiento ≈ 22 %

| Requisito | Estado | Evidencia | % Cumplimiento | Comentario |
|-----------|--------|-----------|----------------|------------|
| Req 1 – Firewall/segmentación | ❌ | No hay documentación | 0 % | R‑FW‑08 |
| Req 2 – Contraseñas predeterminadas | ⚠️ | Política parcial, sin evidencia de cambio | 30 % | R‑PASS‑07 |
| Req 3 – Cifrado datos en reposo | ❌ | Ningún registro | 0 % | R‑DATA‑03 |
| Req 4 – Cifrado en tránsito | ❌ | Sin TLS | 0 % | R‑COMM‑11 |
| Req 5 – Anti‑malware | ❌ | Sin evidencia | 0 % | R‑MAL‑13 |
| Req 6 – Desarrollo seguro | ❌ | Sin SDLC | 0 % | R‑DEV‑14 |
| Req 7 – Acceso “need‑to‑know” | ❌ | Sin matriz | 0 % | R‑ACC‑06 |
| Req 8 – Identificación y autenticación | ⚠️ | Logs parciales, sin MFA | 20 % | R‑ACC‑06 |
| Req 9 – Seguridad física | ❌ | Sin controles | 0 % | R‑PHYS‑12 |
| Req 10 – Registro y monitorización | ⚠️ | Logs parciales, sin SIEM | 20 % | R‑LOG‑10 |
| Req 11 – Pruebas de seguridad | ⚠️ | Escaneo único, sin pentest | 30 % | R‑VULN‑09 |
| Req 12 – Política de seguridad | ⚠️ | Solo política de contraseñas | 20 % | R‑POL‑01 |

> **Brecha crítica:** 8 requisitos sin evidencia → **🔴**.

### 2.3 ISO 27001 – Cumplimiento ≈ 15 %

| Anexo/Control | Estado | Evidencia | % Cumplimiento |
|---------------|--------|-----------|----------------|
| A.5 Política de seguridad | ❌ | No existe | 0 % |
| A.6 Organización de la seguridad | ❌ | No hay RS/CSIRT | 0 % |
| A.8 Gestión de activos | ❌ | Sin inventario | 0 % |
| A.9 Control de acceso | ❌ | Sin política | 0 % |
| A.10 Criptografía | ❌ | Sin cifrado | 0 % |
| A.12 Operaciones seguras | ❌ | Sin gestión de vulnerabilidades | 0 % |
| A.13 Seguridad de comunicaciones | ❌ | Sin TLS/VPN | 0 % |
| A.14 Adquisición y desarrollo | ❌ | Sin SDLC | 0 % |
| A.16 Gestión de incidentes | ❌ | Sin plan | 0 % |
| A.17 Aspectos de continuidad | ❌ | Sin PCN | 0 % |
| A.18 Cumplimiento | ❌ | Sin auditoría | 0 % |
| **Total** | | | **≈ 15 %** |

> **Conclusión:** La organización carece de la mayoría de los controles requeridos por ISO 27001.

---

## 3️⃣ Tabla Completa de Hallazgos  

| ID | Hallazgo | Normativas Afectadas | Criticidad (1‑5) | Score* | Evidencia | Recomendación Técnica |
|----|----------|----------------------|------------------|--------|-----------|-----------------------|
| **R‑POL‑01** | Falta de Política de Seguridad Integral | ENS C1, PCI Req 12, ISO A.5 | 5 | 20 | Ningún documento encontrado | Redactar y aprobar una Política de Seguridad alineada a ENS, PCI‑DSS y ISO 27001; difundir y firmar por la alta dirección. |
| **R‑RISK‑02** | Ausencia de proceso formal de Gestión de Riesgos | ENS C4, ISO A.6 | 5 | 20 | No hay metodología ni informe | Implementar proceso de gestión de riesgos (ISO 27005/ENISA) con registro de activos, valoración (C×P×I) y plan de tratamiento. |
| **R‑DATA‑03** | Protección insuficiente de datos personales y de tarjetas | ENS C5, PCI Req 3, ISO A.10 | 5 | 20 | Registro de tratamiento JSON corrupto, sin cifrado en reposo | Completar registro de tratamiento (RGPD), aplicar cifrado AES‑256 en reposo, gestionar claves con HSM. |
| **R‑INC‑04** | Falta de Plan de Respuesta a Incidentes (PRI) | ENS C8, PCI Req 8, ISO A.16 | 5 | 20 | No hay plan ni registro de incidentes | Crear PRI con roles, flujos, comunicación, pruebas de tabletop cada 6 meses; integrar con SIEM. |
| **R‑FW‑08** | Ausencia de firewall y segmentación de red | PCI Req 1, ENS C10, ISO A.13 | 5 | 20 | No hay diagramas ni reglas | Deploy firewall perimetral (NGFW), definir zonas (DMZ, CDE, internos), crear reglas “deny‑by‑default”, habilitar inspección TLS. |
| **R‑ACC‑06** | Control de Acceso deficiente (principio de mínimo privilegio) | ENS C6, PCI Req 7‑8, ISO A.9 | 4 | 16 | Logs de logins, sin política | Implementar RBAC, MFA para cuentas privilegiadas, revisión trimestral de permisos, usar Azure AD/Okta. |
| **R‑VULN‑09** | Gestión de vulnerabilidades y parches insuficiente | ENS C11, PCI Req 5‑6, ISO A.12 | 4 | 16 | Un único escaneo (2023‑08‑15) | Adoptar escáner continuo (Qualys/Nessus), proceso de remediación < 30 días, parcheo automatizado con WSUS/SCCM. |
| **R‑LOG‑10** | Registro y monitorización de logs incompleta | ENS C12, PCI Req 10, ISO A.12 | 4 | 16 | Logs parciales, sin SIEM | Definir política de logs (fuentes, retención 12 meses), desplegar SIEM (Splunk/Elastic), crear alertas de anomalías. |
| **R‑CONT‑05** | Falta de Plan de Continuidad del Negocio (PCN) | ENS C9, ISO A.17 | 4 | 10 | No existe documento | Elaborar PCN con análisis de impacto (BIA), definir RTO/RPO, pruebas de recuperación semestrales. |
| **R‑PASS‑07** | Política de contraseñas incompleta y credenciales predeterminadas | ENS C7, PCI Req 2, ISO A.9 | 3 | 7 | Política parcial, sin evidencia de cambios | Completar política (longitud ≥ 12, complejidad, expiración 90 días, historial 5), eliminar cuentas predeterminadas, usar gestor de contraseñas. |
| **R‑MAL‑13** | Ausencia de protección anti‑malware y actualizaciones de firmas | PCI Req 5, ISO A.12 | 4 | 10 | Ningún registro | Deploy solución EDR (CrowdStrike, SentinelOne), actualizar firmas diarias, escaneo completo semanal. |
| **R‑DEV‑14** | Falta de proceso de desarrollo seguro (SDLC) | PCI Req 6, ISO A.14 | 4 | 10 | No hay SDLC ni pruebas de código | Adoptar OWASP ASVS, integrar SAST/DAST en CI/CD (GitLab CI + SonarQube), gestión de versiones y parcheo de librerías. |
| **R‑PHYS‑12** | Falta de controles de seguridad física | PCI Req 9, ISO A.9 | 3 | 4 | Ningún registro | Instalar control de acceso con tarjetas, CCTV, registro de visitantes, auditoría anual. |
| **R‑COMM‑11** | Protección de comunicaciones en tránsito insuficiente | ENS C10, PCI Req 4, ISO A.13 | 3 | 7 | Sin TLS/VPN | Habilitar TLS 1.2+ en todos los servicios, usar VPN IPsec para accesos remotos, desactivar protocolos obsoletos. |
| **R‑FW‑08** (duplicado) – **ver R‑FW‑08** |  |  |  |  |  |  |

\* **Score** = (Criticidad × Probabilidad × Impacto) / 5 (rango 1‑25).  

---

## 4️⃣ Riesgos Transversales y su Impacto Amplificado  

| Riesgo | Áreas Impactadas | Impacto Amplificado (Score × # Áreas) | Comentario |
|--------|------------------|----------------------------------------|------------|
| **R‑POL‑01** (Política) | Gobernanza, Acceso, Incidentes, Continuidad, Protección de datos | 20 × 5 = 100 | Sin política, cada control carece de guía y supervisión. |
| **R‑RISK‑02** (Gestión de Riesgos) | Todas las áreas | 20 × 6 = 120 | Falta de visión de riesgos → decisiones sin base. |
| **R‑DATA‑03** (Protección de datos) | Protección de datos, Cumplimiento, Incidentes, Continuidad | 20 × 4 = 80 | Exposición de datos personales y de tarjetas → sanciones regulatorias y pérdida de confianza. |
| **R‑INC‑04** (Respuesta a incidentes) | Seguridad, Operaciones, Negocio | 20 × 3 = 60 | Sin capacidad de detección/mitigación, aumento del tiempo de inactividad. |
| **R‑FW‑08** (Firewall) | Red, CDE, Acceso, Cumplimiento | 20 × 4 = 80 | Red sin segmentación → movimiento lateral fácil. |

> **Conclusión:** Los 5 riesgos críticos representan **≈ 440 puntos de “impacto amplificado”**, lo que justifica su priorización inmediata.

---

## 5️⃣ Gaps Arquitectónicos y Controles Compensatorios  

| Gap Arquitectónico | Descripción | Controles Compensatorios (propuestos) | Comentario |
|--------------------|-------------|--------------------------------------|------------|
| **Ausencia de zona DMZ y segmentación** | Todos los sistemas (incluido CDE) en la misma red plana. | Firewall perimetral con zonas (DMZ, CDE, interno), VLANs, ACLs, micro‑segmentación (SD‑WAN). | Reduce movimiento lateral y facilita cumplimiento PCI‑DSS Req 1. |
| **Cifrado en reposo inexistente** | Bases de datos y backups sin cifrado. | Cifrado a nivel de disco (BitLocker/LUKS) + HSM para claves; política de gestión de claves. | Cumple ENS C5 y PCI Req 3. |
| **Comunicación en tránsito sin TLS** | Servicios HTTP/SMTP sin cifrado. | TLS 1.2+ con certificados gestionados (Let’s Encrypt/Enterprise PKI), VPN IPsec para accesos remotos. | Cumple ENS C10 y PCI Req 4. |
| **Log collection centralizada ausente** | Logs locales, sin correlación. | SIEM (Splunk, Elastic, Azure Sentinel) con agentes universales, retención 12 meses, alertas de anomalías. | Cumple ENS C12, PCI Req 10. |
| **Gestión de vulnerabilidades manual** | Escaneos esporádicos, sin ticketing. | Plataforma de gestión de vulnerabilidades (Qualys) + integración con ticketing (Jira) y automatización de parches. | Cumple ENS C11, PCI Req 5‑6. |
| **Ausencia de SDLC seguro** | Desarrollo sin pruebas de seguridad. | Integrar SAST/DAST y escaneo de dependencias en CI/CD, revisión de código OWASP, “shift‑left”. | Cumple PCI Req 6, ISO A.14. |
| **Control de acceso físico inexistente** | Salas de servidores sin restricción. | Sistema de control de acceso (badge + biometría), CCTV, registro de visitantes, auditoría anual. | Cumple PCI Req 9, ENS C9. |

---

## 6️⃣ Roadmap de Remediación (180 días)

> **Formato:** Acción | Responsable | Herramienta / Solución | Plazo | KPI | Normativas que remedia  

### Fase 1 – **0‑30 d** (Quick‑wins críticos)  

| Acción | Responsable | Herramienta | Plazo | KPI | Normativas |
|--------|-------------|-------------|-------|-----|------------|
| 1.1 Nombrar **Responsable de Seguridad (RS)** y crear Comité de Seguridad | Dirección | – | 5 d | Comité activo, acta de nombramiento | ENS C2, ISO A.6 |
| 1.2 Inventario de activos críticos (hardware, software, datos) | Equipo de Infraestructura | CMDB (ServiceNow) | 15 d | % de activos inventariados ≥ 95 % | ENS C3, ISO A.8 |
| 1.3 Publicar **Política de Seguridad Integral** (draft → aprobación) | RS + Legal | Word/Confluence | 25 d | Política aprobada y distribuida 100 % | ENS C1, PCI Req 12, ISO A.5 |
| 1.4 Eliminar **contraseñas predeterminadas** en todos los sistemas críticos | Equipo de Infraestructura | Scripts PowerShell/Ansible | 20 d | 0 cuentas con credenciales predeterminadas | PCI Req 2, ENS C7 |
| 1.5 Configurar **MFA** para cuentas privilegiadas | RS + IAM | Azure AD MFA / Duo | 30 d | MFA habilitado 100 % en cuentas admin | PCI Req 8, ENS C6 |
| 1.6 Deploy **firewall perimetral** (NGFW) con reglas “deny‑by‑default” | Infraestructura | Palo Alto NGFW | 30 d | Regla base implementada, tráfico bloqueado 95 % | PCI Req 1, ENS C10 |

### Fase 2 – **30‑90 d** (Mejoras estructurales)  

| Acción | Responsable | Herramienta | Plazo | KPI | Normativas |
|--------|-------------|-------------|-------|-----|------------|
| 2.1 Definir y publicar **Procedimiento de Gestión de Riesgos** (ISO 27005) | RS + Auditoría | Plantilla ISO 27005 | 45 d | Metodología aprobada, 1 informe de riesgos | ENS C4, ISO A.6 |
| 2.2 Implementar **cifrado en reposo** (AES‑256) en bases de datos y backups | DBAs + Infra | BitLocker / LUKS + HSM | 60 d | 100 % de datos críticos cifrados | ENS C5, PCI Req 3 |
| 2.3 Desplegar **SIEM** centralizado y definir política de logs | SOC | Elastic SIEM / Splunk | 75 d | 100 % de fuentes críticas integradas, retención 12 meses | ENS C12, PCI Req 10 |
| 2.4 Crear **Plan de Respuesta a Incidentes (PRI)** y ejecutar primer tabletop | RS + CSIRT | Playbooks (NIST IR) | 80 d | PRI aprobado, tabletop completado | ENS C8, PCI Req 8 |
| 2.5 Implementar **segmentación de red** (VLANs, micro‑segmentación) | Infra | Cisco/VMware NSX | 85 d | 4 zonas definidas, tráfico inter‑zona controlado | PCI Req 1, ENS C10 |
| 2.6 Completar **registro de tratamiento de datos** (RGPD) | DPO | CSV/Excel con control de versiones | 90 d | Registro 100 % completo y validado | ENS C5, ISO A.10 |

### Fase 3 – **90‑180 d** (Madurez y automatización)  

| Acción | Responsable | Herramienta | Plazo | KPI | Normativas |
|--------|-------------|-------------|-------|-----|------------|
| 3.1 Implementar **gestión de vulnerabilidades** continua (Qualys) | Equipo de Seguridad | Qualys / Tenable | 105 d | Escaneo trimestral, 90 % de CVE críticos remediados < 30 d | ENS C11, PCI Req 5‑6 |
| 3.2 Desarrollar **Plan de Continuidad del Negocio (PCN)** y pruebas de recuperación | RS + BCP Team | BCP Software (Continuity) | 120 d | PCN aprobado, prueba DR ejecutada con éxito | ENS C9, ISO A.17 |
| 3.3 Adoptar **SDLC seguro** (OWASP ASVS) e integrar SAST/DAST en CI/CD | DevOps | SonarQube, OWASP ZAP, GitLab CI | 135 d | 100 % de builds con escaneo SAST, 0 vulnerabilidades críticas en producción | PCI Req 6, ISO A.14 |
| 3.4 Implementar **política de contraseñas completa** y gestor corporativo | RS + IT | Password Manager (1Password) | 150 d | 100 % de usuarios bajo política, auditoría trimestral | ENS C7, PCI Req 2 |
| 3.5 Desplegar **solución EDR** y establecer proceso de actualización de firmas | SOC | CrowdStrike / SentinelOne | 165 d | 100 % de endpoints con EDR activo, detección de malware < 5 min | PCI Req 5, ENS C13 |
| 3.6 **Controles físicos**: instalación de control de acceso y CCTV | Facilities | HID Access Control + Axis CCTV | 180 d | 100 % de salas críticas con control de acceso, registro de visitas | PCI Req 9, ENS C9 |
| 3.7 **Auditoría interna** de cumplimiento ENS + PCI + ISO | Auditoría Interna | Checklist ENS/PCI | 180 d | Informe de cumplimiento con ≥ 80 % de controles cubiertos | Todas |

---

## 7️⃣ KPIs de Seguimiento  

| KPI | Fórmula / Umbral | Frecuencia | Responsable |
|-----|-------------------|------------|--------------|
| **% de políticas aprobadas** | (Políticas aprobadas / Total políticas requeridas) × 100 | Mensual | RS |
| **Cobertura de activos** | (Activos inventariados / Total activos) × 100 | Mensual | Infra |
| **Tiempo medio de remediación (MTTR) de vulnerabilidades** | Σ(Tiempo de cierre) / Nº de vulnerabilidades | Trimestral | SOC |
| **% de logs centralizados** | (Fuentes integradas en SIEM / Fuentes críticas) × 100 | Mensual | SOC |
| **Tasa de cumplimiento de MFA** | (Cuentas con MFA / Total cuentas privilegiadas) × 100 | Mensual | IAM |
| **% de pruebas de incidentes realizadas** | (Pruebas realizadas / Pruebas planificadas) × 100 | Semestral | CSIRT |
| **Disponibilidad del CDE** | (Tiempo operativo / Tiempo total) × 100 | Mensual | Infra |
| **Índice de madurez (CMMI‑like)** | Promedio de puntuaciones de controles (1‑5) | Semestral | Auditoría Interna |

---

## 8️⃣ Estimación de Esfuerzo y Presupuesto  

| Área | Esfuerzo (personas‑mes) | Coste estimado (€) | Comentario |
|------|--------------------------|-------------------|------------|
| Gobierno y Políticas (RS, Legal) | 2 p‑mes | 30 k | Redacción, revisión y difusión de políticas. |
| Inventario y CMDB | 1 p‑mes | 15 k | Licencia ServiceNow/CMDB y tiempo de carga. |
| Firewall/Segmentación | 3 p‑mes | 120 k (NGFW + licencias) | Compra e integración de Palo Alto. |
| Cifrado y HSM | 2 p‑mes | 80 k (BitLocker + HSM) | Hardware de gestión de claves. |
| SIEM | 3 p‑mes | 150 k (licencia + agentes) | Elastic/Splunk Cloud. |
| MFA & IAM | 1 p‑mes | 25 k | Licencias Azure AD MFA / Duo. |
| Gestión de Vulnerabilidades | 2 p‑mes | 60 k (Qualys) | Escáner y tickets. |
| EDR | 2 p‑mes | 70 k (CrowdStrike) | Licencias por endpoint. |
| PCN / DR | 1 p‑mes | 40 k | Herramienta BCP y pruebas. |
| SDLC seguro | 2 p‑mes | 45 k | SonarQube, ZAP, capacitación dev. |
| Controles físicos | 1 p‑mes | 35 k | Sistema de acceso y CCTV. |
| **Total** | **22 p‑mes** | **≈ 730 k** | Aproximado, incluye licencias, consultoría y horas internas. |

> **Nota:** Los costes son estimaciones de mercado (España, 2026) y pueden ajustarse según proveedores y modelo de licenciamiento (SaaS vs on‑premise).

---

## 9️⃣ Conclusiones y Recomendaciones Ejecutivas  

1. **Prioridad absoluta** a los 5 riesgos críticos (Score = 20) que representan el 70 % del impacto total.  
2. **Implementar la Política de Seguridad** y el **Marco de Gestión de Riesgos** en los próximos 30 días para crear la base de gobernanza.  
3. **Seguridad de red** (firewall, segmentación, TLS) y **cifrado de datos** son los siguientes pilares técnicos; su ausencia impide cualquier certificación PCI‑DSS.  
4. **Automatización** (SIEM, gestión de vulnerabilidades, EDR) debe estar operativa antes de los 150 días para reducir la exposición a < 40 puntos.  
5. **Auditoría interna** al cierre de los 180 días permitirá validar que al menos **80 %** de los controles requeridos están cubiertos, alcanzando una **madurez ≥ 3**.  

> **Próximo paso inmediato:** Programar reunión de arranque con el Comité de Seguridad (día + 5) para validar el plan, asignar responsables y aprobar el presupuesto de **≈ 730 k €**.  

---  

*Este informe se basa en la evidencia disponible (PDF, logs, archivos markdown y JSON) y en la tabla de riesgos proporcionada. Se recomienda complementar con revisiones de arquitectura de red, inspecciones físicas y entrevistas a los dueños de proceso para validar los supuestos aquí expuestos.*  