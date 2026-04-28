**  

# INFORME TÉCNICO – CISO  
**Organización:** Ejemplo S.A. – Sede Central  
**Ámbito:** Infraestructura IT, Desarrollo de Software, RRHH, Gestión de Datos Personales y Continuidad del Negocio  
**Fecha:** 28 abril 2026  
**Autor:** Redactor Senior de Informes Técnicos (CISO Consultor)  

---  

## 1. Resumen Ejecutivo Técnico  

| Norma | Hallazgos críticos | % Cumplimiento estimado | Semáforo |
|-------|-------------------|--------------------------|----------|
| **ISO 27001** | 84 controles sin evidencia (solo 9 % evidenciados) | **9 %** | 🔴 |
| **ENS** (Real Decreto 311/2022) | 2 de 5 controles críticos sin evidencia | **60 %** | 🟡 |
| **GDPR** | 5 de 12 requisitos críticos sin evidencia (DPIA, ARCO+, Notificación) | **58 %** | 🟡 |
| **NIS2** | 5 de 12 requisitos críticos sin evidencia (incidentes, cadena suministro, continuidad) | **58 %** | 🟡 |
| **PCI‑DSS v4.0** | 5 de 12 requisitos críticos sin evidencia (cifrado datos, segmentación, pruebas) | **58 %** | 🟡 |

**Exposición total (Σ Score):** **176 puntos** (rango 0‑250).  
**Madurez media (1‑5):** **2.1** → fase *Definida* (CMMI‑style).  

> **Interpretación rápida**  
> - 🔴 ISO 27001 → Urgente: 84 controles sin evidencia.  
> - 🟡 Todas las demás normas → Riesgos críticos concentrados en pocos controles (desactivación de cuentas, notificación de incidentes, continuidad, cifrado de datos de tarjeta).  

---  

## 2. Análisis de Brechas por Normativa  

| Norma | Controles evaluados | Controles con evidencia | Controles sin evidencia / NC | % Cumplimiento | Comentario clave |
|-------|--------------------|------------------------|----------------------------|----------------|-------------------|
| **ISO 27001** | 93 (Anexo A) | 9 (EDR, DLP, cifrado, política, logs) | 84 (incl. gestión de incidentes, continuidad, pruebas, segmentación) | **9 %** | Falta de evidencia en la mayoría de los controles críticos (incidentes, BCP, pruebas de penetración, gestión de terceros). |
| **ENS** | 5 controles críticos (5.1, 5.15, 7.4, 9.2, 14) | 3 (Política, EDR, DLP) | 2 (Desactivación tardía de cuentas, punto ciego CCTV) | **60 %** | Los dos hallazgos son de alto impacto y transversales. |
| **GDPR** | 12 requisitos críticos (Art. 30, 6, 9, 33‑34, 35) | 7 (Registro, bases legales, política, cifrado, DLP, EDR) | 5 (DPIA para datos especiales, ARCO+, Notificación de brechas, pruebas de seguridad, gestión de exportaciones) | **58 %** | Necesario DPIA y procesos de derechos ARCO+. |
| **NIS2** | 12 requisitos críticos (Art. 19‑21, 23‑24, 14‑15, 31) | 7 (Política, logs, firewall, DLP, EDR, registro de actividades) | 5 (Notificación de incidentes, gestión de cadena suministro, BCP/DRP, formación, pruebas de penetración) | **58 %** | Falta de proceso formal de notificación y de gestión de riesgos de terceros. |
| **PCI‑DSS v4.0** | 12 requisitos críticos (Req 1‑12) | 7 (Firewall logs, EDR, DLP, cifrado de discos, política de contraseñas, bloqueo) | 5 (Cifrado de datos de tarjeta en reposo y tránsito, segmentación de red, pruebas de penetración, desarrollo seguro, gestión de copias) | **58 %** | Riesgo de pérdida de certificación si no se corrige. |

---  

## 3. Registro Unificado de Hallazgos  

| ID | Hallazgo | Normativas afectadas | Criticidad (1‑5) | Score (1‑25) | Evidencia | Recomendación Técnica |
|----|----------|----------------------|-------------------|--------------|-----------|------------------------|
| **R01** | Desactivación tardía de cuentas de usuario/VPN (> 24 h) | ISO 27001 5.15, ENS 5.15, NIS2 5.15, PCI‑DSS Req 7 | 5 (Crítico) | 20 | Log de desactivación 72 h (ISO 27001 evidencia) | Automatizar desactivación mediante integración nómina → AD (PowerShell / Azure AD Connect). |
| **R02** | Punto ciego en cámara CCTV del Datacenter | ISO 27001 7.4, ENS 7.4, NIS2 7.4, PCI‑DSS Req 9 | 5 | 12 | Video y bitácora física (ISO 27001) | Re‑orientar cámara o instalar espejo convexo; actualizar mapa de cobertura. |
| **R03** | Ausencia de procedimiento documentado de notificación de incidentes/brechas | NIS2 Art. 19‑21, GDPR Art. 33/34, ISO 27001 14.1, PCI‑DSS Req 12 | 5 | 20 | **Sin evidencia** | Definir política de notificación (plazo 72 h), plantilla de informe, flujo de aprobación (ServiceNow). |
| **R04** | Falta de evidencia de continuidad del negocio y DRP | NIS2 Art. 14‑15, ISO 27001 15.1, PCI‑DSS Req 1 | 5 | 20 | **Sin evidencia** | Elaborar BCP/DRP, definir RTO ≤ 4 h, RPO ≤ 1 h; ejecutar pruebas de recuperación trimestrales. |
| **R05** | Tratamiento de datos especiales (estado civil) sin base legal ni DPIA | GDPR Art. 9, ISO 27001 5.13, NIS2 Art. 31 | 5 | 20 | **Sin evidencia** | Realizar DPIA, obtener consentimiento explícito, registrar en Art. 30. |
| **R06** | Exportación de base de datos de clientes sin cifrado ni control de autorización | ISO 27001 13.2, NIS2 31, PCI‑DSS Req 3/4 | 4 | 13 | Log de exportación (DataExport) sin cifrado | Implementar cifrado TLS 1.3 + firma HMAC; registro de autorización (workflow en ServiceNow). |
| **R07** | Falta de segmentación de red y reglas de firewall para datos de tarjetas | PCI‑DSS Req 1, ISO 27001 12.1 | 4 | 10 | Log de cambio firewall (puerto 443) sin segmentación | Crear zona DMZ, ACLs “deny‑all” excepto tráfico necesario; usar firewalls de nueva generación (NGFW). |
| **R08** | Política de contraseñas documentada pero sin evidencia de aplicación práctica | ISO 27001 9.2, PCI‑DSS Req 8, NIS2 11 | 4 | 7 | Política (MD) sin auditoría de hashes | Ejecutar auditoría trimestral de hashes (Nessus/Qualys) y generar informe de cumplimiento. |
| **R09** | Ausencia de gestión de riesgos de la cadena de suministro | NIS2 Art. 23‑24, ISO 27001 15.1 | 4 | 13 | **Sin evidencia** | Evaluar proveedores críticos (EDR, DLP, Cloud) con cuestionario ISO 27005; incluir cláusulas de seguridad en contratos. |
| **R10** | Falta de pruebas de penetración y escaneos de vulnerabilidad periódicos | PCI‑DSS Req 11, ISO 27001 12.6, NIS2 | 4 | 13 | **Sin evidencia** | Programar pentest anual (OWASP Top 10) y escaneos trimestrales (Nessus). |
| **R11** | Cifrado de datos en reposo de tarjetas no evidenciado | PCI‑DSS Req 3, GDPR Art. 32 | 5 | 15 | **Sin evidencia** | Activar BitLocker/FDE en servidores de pago; validar con escáner de cumplimiento (CIS‑CIS). |
| **R12** | Cifrado de datos en tránsito (TLS/SSL) no evidenciado | PCI‑DSS Req 4, GDPR Art. 32 | 5 | 15 | **Sin evidencia** | Forzar TLS 1.3 en todos los endpoints; escanear con SSL Labs. |
| **R13** | Falta de evidencia de procesos de desarrollo seguro (SDLC) | PCI‑DSS Req 6, ISO 27001 14.2 | 4 | 10 | **Sin evidencia** | Adoptar Secure‑DevOps (SAST + DAST, OWASP Dependency‑Check) integrado en CI/CD (GitLab). |
| **R14** | Ausencia de registro y control de accesos físicos a salas críticas (más allá del punto ciego) | ISO 27001 7.4, ENS 7.4, NIS2 | 4 | 10 | **Sin evidencia** | Instalar lectores de tarjetas + video‑analytics; registrar en SIEM. |
| **R15** | Falta de evidencia de formación y concienciación en ciberseguridad | NIS2 Art. 11, ISO 27001 7.2 | 3 | 5 | **Sin evidencia** | Lanzar campaña de e‑learning (PhishMe) y medir % completado. |
| **R16** | Gestión de copias de seguridad sin evidencia (control 13.2 ISO) | ISO 27001 13.2, NIS2 31 | 3 | 5 | **Sin evidencia** | Documentar política de backup, ejecutar pruebas de restauración mensuales. |
| **R17** | Política de seguridad no leída por el 15 % restante del personal | ISO 27001 5.1, ENS 5.1 | 2 | 1 | Evidencia de 85 % lectura | Enviar recordatorio automático y requerir firma digital. |
| **R18** | Control de cambios de firewall sin proceso formal de aprobación | ISO 27001 12.1, PCI‑DSS Req 1 | 3 | 4 | Log de cambio sin workflow | Implementar proceso de Change Management (ITIL) con aprobaciones. |
| **R19** | Registro de actividades de tratamiento de datos personales incompleto | GDPR Art. 30, NIS2 31 | 3 | 4 | **Sin evidencia** | Completar registro con campos “destinatario”, “plazo de conservación”. |
| **R20** | Política de gestión de incidentes sin evidencia de pruebas de respuesta | ISO 27001 14.1, NIS2 19‑21 | 4 | 7 | **Sin evidencia** | Simular incidente (table‑top) cada 6 meses; registrar resultados. |

> **Nota:** 18 de 20 riesgos son **transversales** (afectan a ≥ 2 normativas) → oportunidad de remediación única que cubre varios marcos regulatorios.  

---  

## 4. Riesgos Transversales y Impacto Amplificado  

| Riesgo | Normativas impactadas | Impacto combinado (Score × #normas) | Comentario de amplificación |
|--------|------------------------|--------------------------------------|------------------------------|
| **R01 – Desactivación tardía de cuentas** | ISO 27001, ENS, NIS2, PCI‑DSS | 20 × 4 = **80** | Cada norma exige control de acceso; la falta genera exposición prolongada a datos de tarjeta y a datos personales. |
| **R03 – Falta de proceso de notificación de incidentes** | NIS2, GDPR, ISO 27001, PCI‑DSS | 20 × 4 = **80** | Sin notificación, la organización incurre en multas (hasta 20 M € GDPR) y pérdida de reputación. |
| **R04 – Ausencia de BCP/DRP** | NIS2, ISO 27001, PCI‑DSS | 20 × 3 = **60** | Interrupción de servicios críticos → daño financiero y sanciones regulatorias. |
| **R05 – Tratamiento de datos especiales sin DPIA** | GDPR, ISO 27001, NIS2 | 20 × 3 = **60** | Multas GDPR (hasta 20 M €) y riesgo de sanciones ENS. |
| **R06 – Exportación de bases sin cifrado** | ISO 27001, NIS2, PCI‑DSS | 13 × 3 = **39** | Posible fuga de datos personales y de tarjetas → exposición a fraude. |
| **R07 – Falta de segmentación de red** | PCI‑DSS, ISO 27001 | 10 × 2 = **20** | Un atacante que comprometa la red interna puede acceder a datos de tarjeta. |
| **R10 – Falta de pruebas de vulnerabilidad** | PCI‑DSS, ISO 27001, NIS2 | 13 × 3 = **39** | Vulnerabilidades sin descubrir → explotación y brechas. |

**Total de Score de riesgos transversales:** **378** (≈ 55 % del Score total).  

---  

## 5. Gaps Arquitectónicos y Controles Compensatorios  

| Área arquitectónica | Gap detectado | Impacto | Control compensatorio provisional | Comentario |
|----------------------|--------------|----------|--------------------------------|------------|
| **Gestión de identidades** | Desactivación tardía de cuentas, falta de MFA en VPN | Acceso no autorizado prolongado | MFA obligatoria + **Just‑In‑Time** (JIT) provisioning (Azure AD Privileged Identity Management) | Reduce ventana de exposición mientras se implementa automatización completa. |
| **Seguridad perimetral** | Falta de segmentación de red y reglas de firewall específicas para datos de tarjetas | Movimiento lateral | **Micro‑segmentación** con VLANs y políticas de Zero‑Trust (Cisco ISE + NGFW) | Compensa ausencia de segmentación formal. |
| **Protección de datos en tránsito** | No hay TLS/SSL evidenciado | Intercepción de datos | **TLS‑Termination** en load balancer con certificados gestionados por **HashiCorp Vault** | Garantiza cifrado de extremo a extremo. |
| **Protección de datos en reposo** | No hay cifrado de datos de tarjetas | Robo de datos físicos | **Full‑Disk Encryption** (BitLocker/LUKS) + **Database‑level encryption** (Transparent Data Encryption – TDE) | Cumple PCI‑DSS Req 3 y GDPR Art. 32. |
| **Continuidad del negocio** | Ausencia de BCP/DRP | Interrupción prolongada | **Backup‑as‑a‑Service** (Veeam Cloud Connect) + pruebas de recuperación automatizadas (PowerShell / Azure Automation) | Reduce RTO/RPO a niveles aceptables. |
| **Gestión de terceros** | No hay evaluación de riesgos de proveedores | Cadena de suministro vulnerable | **Vendor Risk Management Platform** (ProcessUnity) con cuestionario ISO 27005 y cláusulas de seguridad en contratos. | Cumple NIS2 Art. 23‑24. |
| **Desarrollo seguro** | Falta de SDLC seguro | Vulnerabilidades en código | **Secure‑DevOps pipeline** (GitLab CI + SAST (Checkmarx) + DAST (OWASP ZAP) + Dependency‑Check) | Compensa ausencia de procesos de desarrollo seguro (PCI‑DSS Req 6). |
| **Formación y concienciación** | 15 % del personal no ha leído la política; falta de e‑learning | Riesgo de error humano | **Plataforma de concienciación** (KnowBe4) con métricas de completitud y simulaciones de phishing. | Mejora postura humana. |

---  

## 6. Roadmap de Remediación  

| Acción | Responsable | Herramienta / Solución | Plazo | KPI (medida) | Normativas que remedia |
|--------|-------------|------------------------|-------|--------------|------------------------|
| **Fase 1 – 0‑30 días (quick‑wins críticos)** |
| 1.1 Automatizar desactivación de cuentas (< 24 h) | IT / RRHH | Azure AD Connect + PowerShell | 15 d | % de cuentas desactivadas < 24 h (objetivo 100 %) | ISO 27001 5.15, ENS 5.15, NIS2, PCI‑DSS |
| 1.2 Definir política de notificación de incidentes (plazo 72 h) | CISO | ServiceNow Incident Management | 30 d | Tiempo medio de notificación (≤ 72 h) | NIS2, GDPR, ISO 27001, PCI‑DSS |
| 1.3 Corregir punto ciego CCTV | Facility Mgmt | Cámara PTZ + espejo convexo | 10 d | % de zona cubierta 100 % | ISO 27001 7.4, ENS 7.4, NIS2 |
| 1.4 Implementar MFA + JIT para VPN | Seguridad de Accesos | Azure AD MFA + PIM | 30 d | % de accesos VPN con MFA (≥ 95 %) | ISO 27001 5.15, ENS 5.15, NIS2 |
| **Fase 2 – 30‑90 días (mejoras estructurales)** |
| 2.1 Elaborar BCP/DRP y ejecutar prueba de recuperación | Business Continuity | Veeam + Azure Site Recovery | 60 d | RTO ≤ 4 h, RPO ≤ 1 h | NIS2 14‑15, ISO 27001 15.1, PCI‑DSS Req 1 |
| 2.2 Implementar segmentación de red y NGFW | Infraestructura | Cisco Firepower NGFW + ISE | 45 d | Número de zonas aisladas (≥ 3) | PCI‑DSS Req 1, ISO 27001 12.1 |
| 2.3 Cifrado de datos en reposo y en tránsito (TLS 1.3, TDE) | Seguridad de Datos | HashiCorp Vault + SQL Server TDE | 45 d | % de bases cifradas (100 %) | PCI‑DSS Req 3‑4, GDPR Art. 32 |
| 2.4 DPIA para datos especiales (estado civil) | DPO / Legal | OneTrust DPIA | 45 d | DPIA completada y aprobada | GDPR Art. 9, ISO 27001 5.13 |
| 2.5 Implementar proceso de gestión de riesgos de terceros | Compras / Seguridad | ProcessUnity Vendor Risk | 60 d | % de proveedores críticos evaluados (100 %) | NIS2 23‑24, ISO 27001 15.1 |
| 2.6 Lanzar campaña de concienciación y pruebas de phishing | RRHH / Seguridad | KnowBe4 | 60 d | % de empleados completado (≥ 95 %) | NIS2 Art. 11, ISO 27001 7.2 |
| **Fase 3 – 90‑180 días (madurez y automatización)** |
| 3.1 Integrar Secure‑DevOps en CI/CD | Desarrollo | GitLab CI + SAST/DAST | 120 d | % de builds con escáneres (≥ 100 %) | PCI‑DSS Req 6, ISO 27001 14.2 |
| 3.2 Automatizar pruebas de vulnerabilidad trimestrales | Red Team | Nessus + Tenable.io | 150 d | Nº de vulnerabilidades críticas < 5 | PCI‑DSS Req 11, ISO 27001 12.6 |
| 3.3 Implementar proceso de backup con pruebas de restauración automatizadas | Backup Admin | Veeam + PowerShell | 180 d | % de backups restaurados con éxito (≥ 95 %) | ISO 27001 13.2, NIS2 31 |
| 3.4 Formalizar Change Management para firewall y otros activos críticos | ITSM | ServiceNow Change | 180 d | % de cambios con aprobación (100 %) | ISO 27001 12.1, PCI‑DSS Req 1 |
| 3.5 Consolidar métricas de cumplimiento en Dashboard ejecutivo | CISO | PowerBI / Grafana | 180 d | Score de exposición < 100 | Todas las normativas |

---  

## 7. KPIs de Seguimiento y Estimación de Esfuerzo / Presupuesto  

| KPI | Valor objetivo | Frecuencia de medición | Herramienta de medición |
|-----|----------------|------------------------|------------------------|
| **% de cuentas VPN desactivadas < 24 h** | 100 % | Diario | Azure AD Log Analytics |
| **Tiempo medio de notificación de brecha** | ≤ 72 h | Por incidente | ServiceNow Incident |
| **Cobertura CCTV del Datacenter** | 100 % | Mensual | Informe de auditoría física |
| **% de datos de tarjeta cifrados (reposo y tránsito)** | 100 % | Mensual | Veeam / SSL Labs |
| **RTO / RPO de los servicios críticos** | ≤ 4 h / ≤ 1 h | Trimestral (pruebas BCP) | Azure Site Recovery |
| **% de proveedores críticos evaluados** | 100 % | Trimestral | ProcessUnity |
| **% de empleados con MFA habilitado** | ≥ 95 % | Mensual | Azure AD Conditional Access |
| **% de builds con SAST/DAST exitosos** | 100 % | Cada commit | GitLab CI |
| **Número de vulnerabilidades críticas abiertas** | < 5 | Semanal | Tenable.io |
| **Score de exposición total** | < 100 | Mensual | Dashboard PowerBI (Σ Score) |

### Estimación de esfuerzo y presupuesto (primeros 180 días)

| Área | Horas estimadas | Coste (€) | Comentario |
|------|----------------|-----------|------------|
| **Automatización desactivación cuentas + MFA** | 200 h | 30 000 | Licencias Azure AD Premium P2 incluidas. |
| **CCTV y seguridad física** | 120 h | 15 000 | Compra cámara PTZ + instalación. |
| **Política de notificación y BCP/DRP** | 250 h | 35 000 | Consultoría externa (ISO 27001/NIS2). |
| **Segmentación de red + NGFW** | 300 h | 80 000 | NGFW (Cisco Firepower) + licencias. |
| **Cifrado datos (TLS, TDE, Vault)** | 180 h | 25 000 | Licencias HashiCorp Vault, certificados. |
| **DPIA y gestión de datos especiales** | 100 h | 12 000 | Herramienta OneTrust. |
| **Gestión de terceros** | 150 h | 20 000 | Plataforma ProcessUnity. |
| **Formación y concienciación** | 80 h | 10 000 | Licencias KnowBe4. |
| **Secure‑DevOps pipeline** | 200 h | 30 000 | Herramientas SAST/DAST (Checkmarx, ZAP). |
| **Pruebas de vulnerabilidad y pentest** | 120 h | 18 000 | Contrato con empresa externa. |
| **Total** | **1 900 h** | **≈ 305 000 €** | Incluye licencias, consultoría y horas internas. |

> **Nota:** Los costes son estimaciones basadas en tarifas de mercado (2026) y pueden ajustarse tras la fase de detalle de proyecto.  

---  

## 8. Conclusiones y Recomendaciones Ejecutivas  

1. **Exposición crítica concentrada** – Los 5 riesgos con Score ≥ 20 representan **≈ 55 %** del total de exposición (R01‑R05). Su remediación inmediata (Fase 1) reducirá el Score total por debajo de 100, pasando la organización a un nivel de riesgo **moderado**.  
2. **Cumplimiento normativo bajo** – Solo **≈ 10 %** de los controles ISO 27001 están evidenciados; el resto requiere documentación, pruebas o automatización. Las demás normas presentan brechas críticas (notificación de incidentes, DPIA, BCP).  
3. **Arquitectura insuficiente** – Falta de segmentación de red, cifrado de datos de tarjeta y de tránsito, y de controles de acceso físico. Los controles compensatorios propuestos (Zero‑Trust, MFA, micro‑segmentación) deben implementarse antes de la fase 2.  
4. **Prioridad de inversión** – La mayor parte del presupuesto (≈ 45 %) se destina a **segmentación de red y cifrado**, que son requisitos de PCI‑DSS y GDPR y reducen el riesgo de exposición de datos de tarjeta.  
5. **Beneficio esperado** – Al cumplir con los requisitos de notificación de incidentes y BCP, la organización evita multas potenciales de **hasta 20 M €** (GDPR) y mantiene la certificación PCI‑DSS, lo que protege ingresos y reputación.  

### Próximos pasos  

- **Aprobación del presupuesto** (≈ 300 k €) y asignación de recursos internos.  
- **Kick‑off del proyecto** con comité de seguridad (CISO, DPO, CTO, RRHH).  
- **Seguimiento semanal** de los KPIs críticos (desactivación de cuentas, notificación de incidentes, cifrado).  

---  

**Fin del informe**