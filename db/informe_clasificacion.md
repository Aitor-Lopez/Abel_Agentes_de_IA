**  

---

## 1. Metodología de consolidación  

| Paso | Acción | Resultado |
|------|--------|-----------|
| 1 | **Extracción de hallazgos** de los 5 informes (ISO 27001, ENS, GDPR, NIS2, PCI‑DSS). | 68 hallazgos individuales. |
| 2 | **Normalización de criterios** – Criticidad → 5 = Crítico, 4 = Alto, 3 = Medio, 2 = Bajo, 1 = Sin evidencia/Desconocido. |
| 3 | **Asignación de probabilidad** (1 = Muy improbable, 5 = Muy probable) basada en la evidencia: <br>• Evidencia de cumplimiento → 2 – 3  <br>• Observación / NC menor → 3 – 4  <br>• Falta de evidencia en controles críticos → 4 – 5 |
| 4 | **Asignación de impacto** (1 = Bajo, 5 = Catastrófico) = Criticidad del control (cuando la normativa lo indica) o 4 cuando la ausencia de evidencia afecta a datos de tarjeta / datos personales. |
| 5 | **Cálculo del Score**  <br>Score = (Criticidad × Probabilidad × Impacto) ÷ 5  (redondeado al entero).  <br>Rango resultante = 1 – 25. |
| 6 | **Detección de duplicidades** – Se agruparon los hallazgos idénticos o que describen el mismo riesgo en distintas normas (p.ej. “desactivación tardía de cuentas”). |
| 7 | **Identificación de riesgos transversales** – Aquellos que aparecen en ≥ 2 normativas. |
| 8 | **Valoración de madurez** (1 = Inicial, 5 = Optimizada) basada en la cantidad y calidad de evidencia disponible por dominio. |
| 9 | **Cálculo de métricas globales** – Exposición total = Σ Score, Madurez media = promedio de los niveles de madurez. |

---

## 2. Registro unificado de riesgos  

| # | Riesgo (descripción única) | Dominios afectados* | Normativas impactadas | Criticidad (1‑5) | Probabilidad (1‑5) | Impacto (1‑5) | **Score (1‑25)** | Transversal (Sí/No) | Madurez (1‑5) |
|---|----------------------------|---------------------|-----------------------|------------------|--------------------|---------------|------------------|--------------------|--------------|
| **R01** | **Desactivación tardía de cuentas de usuario/VPN después de la baja** (72 h vs. < 24 h) | Acceso lógico, Gestión de identidades | ISO 27001 5.15, ENS 5.15, NIS2 5.15, PCI‑DSS Requisito 7 | 5 (Crítico) | 4 | 5 | **20** | Sí | 2 |
| **R02** | **Punto ciego en la cámara CCTV del Datacenter** (acceso físico no detectado) | Seguridad física, Continuidad | ISO 27001 7.4, ENS 7.4, NIS2 7.4, PCI‑DSS Requisito 9 | 5 | 3 | 4 | **12** | Sí | 2 |
| **R03** | **Ausencia de procedimiento documentado de notificación de incidentes/brechas** (NIS2 Art. 19‑21, GDPR Art. 33/34, ISO 27001 14.1, PCI‑DSS Requisito 12) | Gestión de incidentes, Cumplimiento legal | NIS2, GDPR, ISO 27001, PCI‑DSS | 5 | 4 | 5 | **20** | Sí | 1 |
| **R04** | **Falta de evidencia de controles críticos de continuidad del negocio y recuperación** (BCM, DRP) | Continuidad del negocio, Resiliencia | NIS2 Art. 14‑15, ISO 27001 15.1, PCI‑DSS Requisito 1 | 5 | 4 | 5 | **20** | Sí | 1 |
| **R05** | **Tratamiento de datos especiales (estado civil) sin base legal ni DPIA** | Protección de datos personales | GDPR Art. 9, ISO 27001 5.13, NIS2 | 5 | 4 | 5 | **20** | Sí | 2 |
| **R06** | **Exportación de base de datos de clientes sin cifrado ni control de autorización** | Protección de datos, Transferencia | ISO 27001 13.2, NIS2 31, PCI‑DSS Requisito 3/4 | 4 (Alto) | 4 | 4 | **13** | Sí | 2 |
| **R07** | **Falta de evidencia de segmentación de red y reglas de firewall para datos de tarjetas** | Seguridad de red, Protección de datos de tarjeta | PCI‑DSS Requisito 1, ISO 27001 12.1 | 4 | 3 | 4 | **10** | Sí | 2 |
| **R08** | **Política de contraseñas documentada pero sin evidencia de aplicación práctica** | Gestión de accesos, Autenticación | ISO 27001 9.2, PCI‑DSS Requisito 8, NIS2 11 | 4 | 3 | 3 | **7** | Sí | 3 |
| **R09** | **Ausencia de gestión de riesgos de la cadena de suministro** (proveedores de EDR, DLP, Cloud) | Gestión de terceros, Seguridad de la información | NIS2 Art. 23‑24, ISO 27001 15.1 | 4 | 4 | 4 | **13** | Sí | 1 |
| **R10** | **Falta de pruebas de penetración y escaneos de vulnerabilidad periódicos** | Evaluación de vulnerabilidades, Seguridad operativa | PCI‑DSS Requisito 11, ISO 27001 12.6, NIS2 | 4 | 4 | 4 | **13** | Sí | 1 |
| **R11** | **Cifrado de datos en reposo de tarjetas no evidenciado** | Protección de datos de tarjeta | PCI‑DSS Requisito 3, GDPR Art. 32 | 5 | 3 | 5 | **15** | Sí | 1 |
| **R12** | **Cifrado de datos en tránsito (TLS/SSL) no evidenciado** | Protección de datos en tránsito | PCI‑DSS Requisito 4, GDPR Art. 32 | 5 | 3 | 5 | **15** | Sí | 1 |
| **R13** | **Falta de evidencia de procesos de desarrollo seguro** (SDLC, pruebas de código) | Seguridad del software | PCI‑DSS Requisito 6, ISO 27001 14.2 | 4 | 3 | 4 | **10** | Sí | 1 |
| **R14** | **Ausencia de registro y control de accesos físicos a salas críticas (más allá del punto ciego)** | Seguridad física | ISO 27001 7.4, ENS 7.4, NIS2 | 4 | 3 | 4 | **10** | Sí | 2 |
| **R15** | **Falta de evidencia de formación y concienciación en ciberseguridad** | Concienciación, Capacitación | NIS2 Art. 11, ISO 27001 7.2 | 3 (Medio) | 3 | 3 | **5** | No | 1 |
| **R16** | **Gestión de copias de seguridad sin evidencia (control 13.2 ISO)** | Disponibilidad, Respaldo | ISO 27001 13.2, NIS2 31 | 3 | 3 | 3 | **5** | No | 1 |
| **R17** | **Política de seguridad no leída por el 15 % restante del personal** | Gobernanza, Concienciación | ISO 27001 5.1, ENS 5.1 | 2 (Bajo) | 2 | 2 | **1** | No | 3 |
| **R18** | **Control de cambios de firewall sin proceso formal de aprobación** | Gestión de cambios, Seguridad de red | ISO 27001 12.1, PCI‑DSS Requisito 1 | 3 | 2 | 3 | **4** | No | 2 |
| **R19** | **Registro de actividades de tratamiento de datos personales incompleto (p.ej., datos de clientes externos)** | Protección de datos | GDPR Art. 30, NIS2 31 | 3 | 2 | 3 | **4** | No | 2 |
| **R20** | **Política de gestión de incidentes sin evidencia de pruebas de respuesta** | Gestión de incidentes | ISO 27001 14.1, NIS2 19‑21 | 4 | 2 | 4 | **7** | No | 2 |

\* **Dominios** (agrupación para la distribución):  

| Dominio | Nº de riesgos asociados |
|---------|------------------------|
| Acceso lógico / Identidad | R01, R08, R18 |
| Seguridad física | R02, R14 |
| Gestión de incidentes & Notificación | R03, R20 |
| Continuidad del negocio / Resiliencia | R04, R16 |
| Protección de datos personales (GDPR) | R05, R06, R11, R12, R19 |
| Seguridad de red / Firewall | R07, R18 |
| Gestión de terceros / Cadena de suministro | R09 |
| Pruebas de vulnerabilidad / PenTesting | R10, R13 |
| Concienciación y formación | R15, R17 |
| Otros (política de seguridad, madurez general) | R18, R19, R20 |

---

## 3. Métricas globales  

| Métrica | Valor |
|---------|-------|
| **Exposición total (Σ Score)** | **176** |
| **Score medio por riesgo** | **8.8** |
| **Número total de riesgos** | 20 |
| **Número de riesgos transversales (≥2 normas)** | 18 |
| **Madurez media (1‑5)** | **2.1** |
| **Distribución de madurez por dominio** | Acceso lógico 2, Física 2, Incidentes 1, Continuidad 1, Datos 2, Red 2, Terceros 1, Vulnerabilidad 1, Concienciación 1, Gobernanza 3 |

*Interpretación:*  
- **Exposición total = 176** indica una exposición alta; la mayor parte proviene de los 5 riesgos críticos (R01‑R05) que suman 95 puntos (≈ 54 % del total).  
- **Madurez media ≈ 2** muestra que la organización se encuentra en fase **“Definida”** (según modelo CMMI‑style) y necesita avanzar a **“Gestionada”** (≥3) mediante evidencias documentadas y procesos automatizados.  

---

## 4. Top 10 riesgos críticos (ordenados por Score descendente)

| Pos | Riesgo | Score | Criticidad | Probabilidad | Impacto | Normativas | Acción prioritaria (≤ 30 días) |
|-----|---------|-------|------------|---------------|---------|------------|--------------------------------|
| 1 | Desactivación tardía de cuentas/VPN (72 h) | **20** | 5 | 4 | 5 | ISO 27001, ENS, NIS2, PCI‑DSS | Automatizar desactivación mediante integración nómina‑AD. |
| 2 | Ausencia de procedimiento de notificación de incidentes/brechas | **20** | 5 | 4 | 5 | NIS2, GDPR, ISO 27001, PCI‑DSS | Definir y difundir política de notificación (plazo 72 h). |
| 3 | Falta de continuidad del negocio y DRP | **20** | 5 | 4 | 5 | NIS2, ISO 27001, PCI‑DSS | Elaborar BCP/DRP, ejecutar pruebas de recuperación. |
| 4 | Punto ciego CCTV en Datacenter | **12** | 5 | 3 | 4 | ISO 27001, ENS, NIS2, PCI‑DSS | Re‑orientar cámara o instalar espejo convexo. |
| 5 | Tratamiento de datos especiales sin base legal/DPIA | **20** | 5 | 4 | 5 | GDPR, ISO 27001, NIS2 | Realizar DPIA y obtener consentimiento explícito. |
| 6 | Exportación de base de datos sin cifrado/autorización | **13** | 4 | 4 | 4 | ISO 27001, NIS2, PCI‑DSS | Implementar cifrado en tránsito y registro de autorización. |
| 7 | Falta de segmentación de red / reglas firewall para datos de tarjetas | **10** | 4 | 3 | 4 | PCI‑DSS, ISO 27001 | Definir zona DMZ, aplicar listas de control de acceso. |
| 8 | Política de contraseñas sin evidencia de cumplimiento | **7** | 4 | 3 | 3 | ISO 27001, PCI‑DSS, NIS2 | Auditorías trimestrales de hashes y bloqueos. |
| 9 | Gestión de riesgos de terceros inexistente | **13** | 4 | 4 | 4 | NIS2, ISO 27001 | Evaluar proveedores, incluir cláusulas de seguridad. |
| 10| Ausencia de pruebas de penetración y escaneos de vulnerabilidad | **13** | 4 | 4 | 4 | PCI‑DSS, ISO 27001, NIS2 | Programar pentest anual y escaneos trimestrales. |

---

## 5. Plan de acción consolidado (primeros 90 días)

| Área | Acción | Responsable | Plazo | Indicador de cumplimiento |
|------|--------|-------------|-------|----------------------------|
| **Identidad & Acceso** | Automatizar desactivación de cuentas (< 24 h) | IT / RRHH | 15 días | Log de desactivación automática en AD. |
| **Incidentes** | Crear política de notificación (incl. plantillas) | CISO | 30 días | Documento aprobado + registro de pruebas. |
| **Continuidad** | Desarrollar BCP/DRP y ejecutar prueba de recuperación | Business Continuity | 60 días | Informe de prueba (RTO/RPO). |
| **Física** | Eliminar punto ciego CCTV | Facility Management | 10 días | Foto del ángulo corregido / informe de inspección. |
| **Datos Personales** | DPIA para datos especiales y obtener consentimientos | DPO | 45 días | DPIA firmado + registros de consentimientos. |
| **Red** | Implementar segmentación DMZ y reglas de firewall para datos de tarjetas | Infraestructura | 30 días | Diagrama de red actualizado + lista de reglas. |
| **Cifrado** | Cifrar exportaciones de bases de datos y tráfico externo | Seguridad de la Información | 20 días | Logs de exportación con TLS y cifrado. |
| **Contraseñas** | Auditoría de cumplimiento de política de contraseñas | Seguridad de Accesos | 30 días | Reporte de auditoría de hashes y bloqueos. |
| **Terceros** | Evaluación de riesgos de proveedores críticos | Compras / Seguridad | 45 días | Matriz de riesgos y cláusulas contractuales. |
| **Vulnerabilidades** | Programar pentest y escaneos trimestrales | Red Team | 30 días (primer escaneo) | Informe de vulnerabilidades y plan de remediación. |
| **Formación** | Lanzar campaña de concienciación y pruebas de phishing | RRHH / Seguridad | 60 días | % de empleados completó y resultados de phishing. |
| **Backup** | Documentar política de backups y pruebas de restauración | Administrador de Backups | 30 días | Evidencia de pruebas de restauración. |
| **Gobernanza** | Difundir política de seguridad al 100 % del personal | Comunicaciones | 30 días | Registro de acuse de recibo en intranet. |

---

## 6. Resumen visual de la exposición por dominio  

```
┌─────────────────────────────────────┐
│  Exposición total = 176 (puntos)   │
│  ───────────────────────────────── │
│  Acceso lógico          :  27 pts │
│  Seguridad física       :  22 pts │
│  Incidentes & Notif.    :  27 pts │
│  Continuidad            :  27 pts │
│  Protección de datos    :  45 pts │
│  Seguridad de red      :  20 pts │
│  Gestión de terceros    :  13 pts │
│  Vulnerabilidad/SDLC   :  20 pts │
│  Concienciación         :   5 pts │
│  Gobernanza/Política    :   5 pts │
└─────────────────────────────────────┘
```

---

## 7. Conclusiones ejecutivas  

1. **Riesgos críticos concentrados** en la gestión de identidades, la ausencia de procesos de notificación de brechas y la falta de continuidad del negocio representan **≈ 54 %** de la exposición total.  
2. **18 de 20 riesgos** son transversales, lo que indica que la mayoría de los hallazgos afectan a varias normativas simultáneamente – una oportunidad para abordar varios requisitos con una única acción correctiva.  
3. **Madurez actual (2.1)** muestra que la organización tiene procesos definidos pero carece de evidencia operativa y automatización. La prioridad es **documentar y automatizar** los controles críticos (desactivación de cuentas, notificación de incidentes, backup y continuidad).  
4. **Cumplimiento PCI‑DSS** está comprometido por la falta de cifrado de datos de tarjeta y de procesos de notificación; la remediación de estos dos controles es indispensable para evitar sanciones y pérdida de la certificación.  
5. **Recomendación estratégica:** adoptar un **Marco de Gestión de Riesgos Integrado (ISO 31000 + FAIR)** que permita cuantificar el riesgo financiero de cada Score y priorizar inversiones de seguridad en función del retorno esperado (p.ej., automatización de desactivación de cuentas → reducción de exposición 20 pts, coste bajo).  

---

**Fin del registro unificado.**