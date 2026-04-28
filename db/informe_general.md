**INFORME GENERAL DE CUMPLIMIENTO NORMATIVO**  
*Versión 1.0 – 28 abr 2026*  
Clasificación: **Confidencial – Uso interno (DPO, Compliance Officers, Auditores externos)**  

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0 |
| **Fecha** | 28 abr 2026 |
| **Clasificación** | Confidencial – Uso interno |
| **Elaborado por** | **CISO – Carlos Méndez** |
| **Revisado por** | **DPO – Laura Ortega** |
| **Aprobado por** | **Director General – Javier Ruiz** |

---

## 1. Alcance y Metodología de la Auditoría  

| Ítem | Descripción |
|------|-------------|
| **Ámbito** | Todas las unidades de negocio de **Ejemplo S.A.** que procesan datos personales, datos de tarjetas de pago y que están sujetas a los requisitos de ISO 27001:2022, ENS (Real Decreto 311/2022), GDPR (RGPD), NIS2 (Directiva UE 2022/2555) y PCI‑DSS v4.0. |
| **Período de revisión** | 01 ene 2025 – 31 mar 2026. |
| **Metodología** | 1. Recolección de evidencias (políticas, logs, JSON, informes de auditoría). 2. Normalización de hallazgos (68 hallazgos → 20 riesgos únicos). 3. Valoración de criticidad, probabilidad e impacto (escala 1‑5) y cálculo de **Score** (Criticidad × Probabilidad × Impacto ÷ 5). 4. Cruce de requisitos entre normas (riesgos transversales). 5. Elaboración de matrices de control y registro de no conformidades. |
| **Limitaciones** | • No se inspeccionaron físicamente los servidores del sitio de producción (se trabajó con evidencias documentales). <br>• La revisión de terceros (proveedores de EDR/DLP) se basó en la documentación entregada por el área de compras. <br>• Algunas áreas (p.ej. desarrollo de software) no aportaron evidencia de pruebas de seguridad, por lo que se ha calificado como **Sin Evidencia**. |

---

## 2. Estado de Cumplimiento por Normativa  

> **Leyenda de Estado**: **C** = Cumple, **NC** = No Cumple, **NE** = No Evidencia, **NA** = No Aplica.  

### 2.1 ISO 27001:2022  

| Control / Artículo | Descripción | Estado | Evidencia | Observaciones |
|--------------------|-------------|--------|-----------|----------------|
| **5.1** – Política de seguridad de la información | Política aprobada y difundida (85 % del personal). | **C** | POL‑SGSI‑2025‑v2.pdf (acta de aprobación). | Incrementar difusión al 100 %. |
| **5.13** – Protección de datos personales | Registro de actividades (Art. 30 GDPR) con bases legales. | **C** | registro_tratamiento.json. | Mantener actualización anual. |
| **5.15** – Control de accesos (desactivación de cuentas) | Desactivación de cuentas VPN 72 h después de la baja (requisito < 24 h). | **NC** | Log de bajas de usuarios (informe ISO). | Automatizar vía integración nómina‑AD. |
| **7.4** – Seguridad física (cámaras) | Punto ciego en cámara del datacenter. | **NE** (observación) | Video de CCTV (bitácora). | Re‑orientar cámara o instalar espejo convexo. |
| **8.1** – Protección de endpoints (EDR, cifrado) | EDR activo, BitLocker en todos los laptops. | **C** | Reporte EDR, logs de cifrado. | Auditorías trimestrales recomendadas. |
| **8.10** – DLP | Bloqueo de envío de datos “Confidencial” a dominios externos. | **C** | Logs DLP Microsoft 365. | Revisar etiquetas anualmente. |
| **9.2** – Gestión de contraseñas | Requisitos de complejidad, caducidad 90 días, bloqueo tras 5 intentos. | **C** | política_contraseñas.md, logs de bloqueo. | Implementar recordatorios automáticos. |
| **12.1** – Seguridad de red (firewall) | Cambio de regla firewall (puerto 443) registrado. | **C** (parcial) | logs_registro.txt. | Formalizar proceso de aprobación y segmentación. |
| **13.2** – Copias de seguridad | **Sin evidencia** de pruebas de backup. | **NE** | – | Documentar política y pruebas de restauración. |
| **14.1** – Gestión de incidentes | **Sin evidencia** de proceso de respuesta. | **NE** | – | Definir y probar plan de respuesta. |
| **15.1** – Continuidad del negocio | **Sin evidencia** de BCP/DRP. | **NE** | – | Elaborar BCP y pruebas de recuperación. |
| *(Resto de controles del Anexo A)* | No se aportó evidencia. | **NE** | – | Solicitar documentación correspondiente. |

---

### 2.2 Esquema Nacional de Seguridad (ENS)  

| Control / Artículo | Descripción | Estado | Evidencia | Observaciones |
|--------------------|-------------|--------|-----------|----------------|
| **5.1** – Política de seguridad | Política aprobada y alineada a objetivos de negocio (85 % difusión). | **C** | POL‑SGSI‑2025‑v2.pdf. | Difusión al 100 % requerida. |
| **5.15** – Control de accesos | Desactivación tardía de cuentas VPN (72 h). | **NC** | Informe ISO 27001 (5.15). | Automatizar desactivación < 24 h. |
| **8.1** – Protección de endpoints | EDR y BitLocker activos. | **C** | Reporte EDR, logs cifrado. | Mantener proceso de parcheo. |
| **8.10** – DLP | Bloqueo de datos confidenciales a dominios externos. | **C** | Logs DLP. | Revisión anual de etiquetas. |
| **7.4** – Seguridad física | Punto ciego en cámara del datacenter. | **NE** (observación) | Video CCTV. | Corregir ángulo o instalar espejo. |
| **9.2** – Gestión de contraseñas | Política documentada, sin evidencia de aplicación práctica. | **C** (parcial) | política_contraseñas.md, logs. | Auditorías de cumplimiento de contraseñas. |
| **31** – Registro de actividades de tratamiento | Registro JSON con bases legales y plazos. | **C** | registro_tratamiento.json. | Mantener actualizado. |
| **19‑21** – Notificación de incidentes | **Sin evidencia** de procedimiento de notificación. | **NE** | – | Crear política de notificación (72 h). |
| **23‑24** – Gestión de riesgos de la cadena de suministro | **Sin evidencia** de evaluación de proveedores. | **NE** | – | Implementar proceso de evaluación y cláusulas de seguridad. |
| **14‑15** – Continuidad operativa | **Sin evidencia** de BCP/DRP. | **NE** | – | Desarrollar y probar planes de continuidad. |
| **11** – Formación y concienciación | **Sin evidencia** de campañas de formación. | **NE** | – | Lanzar programa de concienciación y pruebas de phishing. |

---

### 2.3 Reglamento General de Protección de Datos (GDPR / RGPD)  

| Artículo / Control | Descripción | Estado | Evidencia | Observaciones |
|---------------------|-------------|--------|-----------|----------------|
| **Art. 30** – Registro de actividades | Registro JSON con finalidades, bases legales, plazos. | **C** | registro_tratamiento.json. | Actualizar anualmente. |
| **Art. 6** – Base legal del tratamiento | Bases legales (ejecución de contrato, obligación legal) declaradas. | **C** | registro_tratamiento.json. | Vincular cada finalidad a su base. |
| **Art. 9** – Datos especiales (estado civil) | Tratamiento sin base legal ni DPIA. | **NC** (potencial) | registro_tratamiento.json (categoría “estado civil”). | Realizar DPIA y obtener consentimiento explícito. |
| **Art. 32** – Seguridad del tratamiento | Cifrado de discos (BitLocker) y DLP implementados. | **C** | Reporte EDR, logs DLP. | Añadir cifrado en tránsito para exportaciones. |
| **Art. 33/34** – Notificación de brechas | **Sin evidencia** de proceso de notificación. | **NE** | – | Definir procedimiento y registro de incidentes. |
| **Derechos ARCO** (acceso, rectificación, supresión, portabilidad) | **Sin evidencia** de procedimientos o formularios. | **NE** | – | Crear y publicar canal de ejercicio de derechos. |
| **Art. 35** – DPIA | **Sin evidencia** de DPIA para datos especiales. | **NE** | – | Realizar DPIA y documentar. |

---

### 2.4 Directiva NIS2  

| Artículo / Control | Descripción | Estado | Evidencia | Observaciones |
|--------------------|-------------|--------|-----------|----------------|
| **5.1** – Política de seguridad | Política aprobada (85 % difusión). | **C** | POL‑SGSI‑2025‑v2.pdf. | Alcanzar 100 % de lectura. |
| **5.15** – Control de accesos | Desactivación tardía de cuentas VPN (72 h). | **NC** | Informe ISO 27001 (5.15). | Automatizar < 24 h. |
| **7.4** – Seguridad física | Punto ciego en cámara del datacenter. | **NE** (observación) | Video CCTV. | Corregir. |
| **8.1** – Protección de endpoints | EDR y BitLocker activos. | **C** | Reporte EDR. | Mantener. |
| **8.10** – DLP | Bloqueo de datos confidenciales a dominios externos. | **C** | Logs DLP. | Revisar. |
| **19‑21** – Notificación de incidentes | **Sin evidencia** de proceso de notificación a la autoridad competente. | **NE** | – | Crear procedimiento (plazo 24 h). |
| **23‑24** – Gestión de riesgos de la cadena de suministro | **Sin evidencia** de evaluación de proveedores críticos. | **NE** | – | Implementar evaluación y cláusulas contractuales. |
| **14‑15** – Continuidad operativa | **Sin evidencia** de BCP/DRP. | **NE** | – | Desarrollar y probar. |
| **11** – Formación y concienciación | **Sin evidencia** de programa de formación. | **NE** | – | Lanzar campaña y pruebas de phishing. |

---

### 2.5 PCI‑DSS v4.0  

| Requisito | Descripción | Estado | Evidencia | Observaciones |
|-----------|-------------|--------|-----------|----------------|
| **1** – Configuración de firewall y segmentación | Registro de cambio de firewall (puerto 443) disponible, pero **no** hay evidencia de segmentación de red ni de reglas específicas para datos de tarjetas. | **C (parcial)** | logs_registro.txt (cambio firewall). | Definir zonas DMZ y listas ACL para datos de tarjetas. |
| **2** – Configuraciones seguras | EDR activo, parches al día, cifrado de discos. | **C** | Reporte EDR, logs BitLocker. | Mantener. |
| **3** – Protección de datos almacenados | **Sin evidencia** de cifrado de datos de tarjetas en reposo. | **NE** | – | Implementar cifrado (AES‑256) y registrar. |
| **4** – Cifrado de datos en tránsito | **Sin evidencia** de TLS/SSL para transmisión de datos de tarjetas. | **NE** | – | Adoptar TLS 1.2+ y registrar. |
| **5** – Protección contra malware | EDR implementado. | **C** | Reporte EDR. | Mantener. |
| **6** – Desarrollo seguro | **Sin evidencia** de procesos SDLC, pruebas de código o escaneos de vulnerabilidades en aplicaciones. | **NE** | – | Definir proceso de desarrollo seguro y pruebas. |
| **7** – Control de acceso a datos de tarjetas | Política de control de accesos (NC 5.15) y observación de punto ciego físico. | **NC (parcial)** | Informe ISO 5.15, video CCTV. | Automatizar desactivación y corregir vigilancia física. |
| **8** – Identificación y autenticación | Política de contraseñas y logs de bloqueo. | **C** | política_contraseñas.md, logs. | Auditorías periódicas. |
| **9** – Restricción de acceso físico | Bitácora física completa, pero cámara con punto ciego. | **NC (parcial)** | Video CCTV. | Mejorar vigilancia. |
| **10** – Registro y monitoreo | Logs de autenticación, cambios de firewall y exportaciones de bases de datos. | **C** | logs_registro.txt. | Añadir correlación con SIEM. |
| **11** – Pruebas de seguridad | **Sin evidencia** de pruebas de penetración o escaneos de vulnerabilidad. | **NE** | – | Programar pentest anual y escaneos trimestrales. |
| **12** – Políticas y procedimientos | Política de seguridad aprobada (ISO 5.1). | **C** | POL‑SGSI‑2025‑v2.pdf. | Completar con procesos de incidentes y continuidad. |

---

## 3. Registro de No Conformidades (NC)

| ID‑NC | Normativa | Requisito / Control | Criticidad (1‑5) | Fecha detección | Responsable | Estado |
|-------|-----------|----------------------|------------------|------------------|--------------|--------|
| **NC‑01** | ISO 27001 / ENS | 5.15 – Desactivación tardía de cuentas VPN (> 24 h) | 5 | 14/04/2026 | IT / RRHH | **Abierta** |
| **NC‑02** | ISO 27001 / ENS | 7.4 – Punto ciego en cámara CCTV del datacenter | 4 | 14/04/2026 | Facility Management | **Abierta** |
| **NC‑03** | NIS2 | 19‑21 – Falta de procedimiento de notificación de incidentes a la autoridad | 5 | 14/04/2026 | CISO | **Abierta** |
| **NC‑04** | NIS2 | 23‑24 – Ausencia de evaluación de riesgos de la cadena de suministro | 4 | 14/04/2026 | Compras / Seguridad | **Abierta** |
| **NC‑05** | NIS2 | 14‑15 – Falta de BCP/DRP documentado y probado | 5 | 14/04/2026 | Business Continuity | **Abierta** |
| **NC‑06** | NIS2 | 11 – Ausencia de programa de formación y concienciación | 3 | 14/04/2026 | RRHH / Seguridad | **Abierta** |
| **NC‑07** | GDPR | Art. 9 – Tratamiento de datos especiales (estado civil) sin base legal ni DPIA | 5 | 14/04/2026 | DPO | **Abierta** |
| **NC‑08** | GDPR | Art. 33/34 – Falta de proceso de notificación de brechas de seguridad | 5 | 14/04/2026 | DPO / CISO | **Abierta** |
| **NC‑09** | GDPR | Derechos ARCO – No existen procedimientos ni formularios | 5 | 14/04/2026 | DPO | **Abierta** |
| **NC‑10** | GDPR | Art. 35 – Ausencia de DPIA para datos especiales | 5 | 14/04/2026 | DPO | **Abierta** |
| **NC‑11** | PCI‑DSS | Requisito 3 – Falta de cifrado de datos de tarjetas en reposo | 5 | 14/04/2026 | Seguridad de la Información | **Abierta** |
| **NC‑12** | PCI‑DSS | Requisito 4 – Falta de cifrado TLS/SSL para datos de tarjetas en tránsito | 5 | 14/04/2026 | Infraestructura | **Abierta** |
| **NC‑13** | PCI‑DSS | Requisito 6 – Ausencia de proceso de desarrollo seguro (SDLC) | 4 | 14/04/2026 | Desarrollo / Seguridad | **Abierta** |
| **NC‑14** | PCI‑DSS | Requisito 11 – Falta de pruebas de penetración y escaneos de vulnerabilidad | 4 | 14/04/2026 | Red Team | **Abierta** |
| **NC‑15** | ISO 27001 / ENS | 13.2 – Falta de evidencia de copias de seguridad y pruebas de restauración | 3 | 14/04/2026 | Administrador de Backups | **Abierta** |
| **NC‑16** | ISO 27001 / ENS | 14.1 – Falta de evidencia de gestión de incidentes | 3 | 14/04/2026 | CISO | **Abierta** |

---

## 4. Plan de Acción Correctivo (PAC)

| Acción | Responsable | Fecha límite | Indicador de cierre |
|--------|-------------|--------------|---------------------|
| **Automatizar desactivación de cuentas VPN (< 24 h)** | IT / RRHH | 15 may 2026 | Log de desactivación automática en AD (tiempo < 24 h). |
| **Corregir punto ciego de la cámara CCTV** | Facility Management | 10 may 2026 | Foto del ángulo corregido / informe de inspección. |
| **Crear y difundir política de notificación de incidentes (plazo 24 h)** | CISO | 30 may 2026 | Documento aprobado + registro de pruebas de notificación. |
| **Implementar evaluación de riesgos de proveedores críticos** | Compras / Seguridad | 30 jun 2026 | Matriz de riesgos y cláusulas contractuales firmadas. |
| **Desarrollar BCP/DRP y ejecutar prueba de recuperación** | Business Continuity | 30 jul 2026 | Informe de prueba (RTO/RPO cumplidos). |
| **Lanzar programa de concienciación y pruebas de phishing** | RRHH / Seguridad | 30 jun 2026 | % de empleados completó + resultados de phishing. |
| **Realizar DPIA para tratamiento de datos especiales (estado civil)** | DPO | 15 may 2026 | DPIA firmado + registro de consentimientos. |
| **Definir procedimiento de notificación de brechas (Art. 33/34)** | DPO / CISO | 30 may 2026 | Procedimiento aprobado + registro de incidentes. |
| **Crear canal y formularios para ejercicio de derechos ARCO** | DPO | 30 jun 2026 | Portal activo y registro de solicitudes. |
| **Cifrar datos de tarjetas en reposo (AES‑256)** | Seguridad de la Información | 20 may 2026 | Informes de cifrado y logs de verificación. |
| **Implementar TLS 1.2+ para todas las comunicaciones de datos de tarjetas** | Infraestructura | 20 may 2026 | Escaneo SSL que muestre TLS 1.2+ en todos los endpoints. |
| **Definir proceso SDLC con revisiones de código y escaneo SAST/DAST** | Desarrollo / Seguridad | 30 jun 2026 | Checklist completado y evidencias de escaneos. |
| **Programar pentest anual y escaneos de vulnerabilidad trimestrales** | Red Team | 30 may 2026 (primer escaneo) | Informe de vulnerabilidades y plan de remediación. |
| **Documentar política de backups y ejecutar pruebas de restauración** | Administrador de Backups | 30 may 2026 | Evidencia de backup y restauración exitosa. |
| **Formalizar proceso de gestión de incidentes (registro, clasificación, respuesta)** | CISO | 30 may 2026 | Procedimiento aprobado + registro de incidentes de prueba. |
| **Actualizar política de seguridad (ISO 5.1) y obtener acuse de recibo del 100 % del personal** | Comunicaciones | 30 may 2026 | Registro de acuses en intranet. |

---

## 5. Análisis de Riesgos para el Registro de Tratamientos GDPR  

| Riesgo | Descripción | Artículo GDPR | Criticidad (1‑5) | Probabilidad (1‑5) | Impacto (1‑5) | Score (1‑25) | Medidas de mitigación |
|--------|-------------|----------------|-------------------|--------------------|--------------|--------------|-----------------------|
| **R05** | Tratamiento de datos especiales (estado civil) sin base legal ni DPIA. | Art. 9, Art. 35 | 5 | 4 | 5 | **20** | Realizar DPIA, obtener consentimiento explícito, registrar base legal. |
| **R06** | Exportación de base de datos de clientes sin cifrado ni control de autorización. | Art. 32, Art. 33/34 (posible brecha) | 4 | 4 | 4 | **13** | Cifrar en tránsito (TLS), registrar autorización, auditoría de exportaciones. |

*Los scores se calculan según la metodología descrita en la sección 1 (Criticidad × Probabilidad × Impacto ÷ 5).*

---

## 6. Cadena de Custodia de Evidencias Analizadas  

1. **Recolección** – Evidencias (políticas, logs, JSON, capturas de pantalla) fueron solicitadas al responsable de cada área y entregadas mediante **correo cifrado (PGP)** con acuse de recibo.  
2. **Registro** – Cada archivo recibió un **identificador único (EVI‑YYYY‑NNN)** y se almacenó en el repositorio **SharePoint Secure** con control de versiones y registro de acceso.  
3. **Integridad** – Se generó un **hash SHA‑256** para cada evidencia al momento de la carga; los hashes se guardaron en el fichero **hashes_evidencias.xlsx** y se verificaron antes del análisis.  
4. **Transporte** – Cuando se necesitó trasladar logs a la herramienta de análisis forense (FTK), se utilizó **USB 3.0 cifrado (AES‑256)** y se documentó la cadena de custodia en el **registro de traslado (log_custodia.txt)**.  
5. **Almacenamiento** – Evidencias se conservan en **archivos inmutables** durante **5 años** (cumplimiento Art. 30 GDPR y requisitos de auditoría ISO).  
6. **Destrucción** – Al término del proyecto, la destrucción se realizará mediante **borrado seguro (DoD 5220.22‑M)** y certificación de destrucción.

---

## 7. Declaraciones de Aplicabilidad (ISO 27001)  

| Control ISO 27001 | Aplicabilidad | Justificación de exclusión (si procede) |
|-------------------|---------------|----------------------------------------|
| **A.6.2.1 – Política de uso de dispositivos móviles** | **No Aplica** | La organización no permite BYOD ni dispositivos móviles corporativos fuera del perímetro de la red. |
| **A.8.3.1 – Gestión de medios removibles** | **No Aplica** | No se utilizan medios extraíbles en los entornos críticos; política de “no USB” está en vigor. |
| **A.9.4.5 – Uso de credenciales de un solo uso (OTP)** | **No Aplica** | Los sistemas críticos utilizan autenticación basada en certificado y no requieren OTP. |
| **A.12.5.1 – Copias de seguridad de datos críticos** | **Aplica** – **No Cumple** (ver NC‑15). | Falta evidencia de pruebas de backup; se implementará en el PAC. |
| **A.14.2.3 – Pruebas de seguridad en el ciclo de vida del software** | **Aplica** – **No Cumple** (ver NC‑13). | No se dispone de proceso SDLC documentado; se implementará en el PAC. |
| **A.16.1.5 – Notificación de incidentes a autoridades** | **Aplica** – **No Cumple** (ver NC‑03, NC‑08). | Falta procedimiento de notificación; se desarrollará en el PAC. |
| **A.18.1.4 – Protección de la información personal** | **Aplica** – **No Cumple** (ver NC‑07, NC‑10). | DPIA y bases legales para datos especiales no documentadas; se corregirá. |
| **A.18.2.2 – Cumplimiento de requisitos legales** | **Aplica** – **Cumple** (excepto los NC señalados). | La mayoría de los requisitos legales están cubiertos; los NC pendientes se tratarán. |

*Todas las exclusiones están justificadas por la ausencia de actividad o por la decisión de la alta dirección de no aplicar el control en el contexto actual.*

---

## 8. Conclusiones Ejecutivas  

| Área | Nivel de Madurez | Principales brechas | Acción crítica (≤ 30 días) |
|------|------------------|---------------------|---------------------------|
| **Gestión de Identidades** | 2 (Definida) | Desactivación tardía de cuentas (NC‑01). | Automatizar desactivación < 24 h. |
| **Seguridad Física** | 2 (Definida) | Punto ciego CCTV (NC‑02). | Re‑orientar cámara. |
| **Gestión de Incidentes** | 1 (Inicial) | Falta de proceso de notificación (NC‑03, NC‑08). | Crear política de notificación. |
| **Protección de Datos (GDPR)** | 2 (Definida) | Tratamiento de datos especiales sin DPIA (NC‑07, NC‑10). | Realizar DPIA y obtener consentimientos. |
| **PCI‑DSS** | 1 (Inicial) | Cifrado de datos de tarjetas (NC‑11, NC‑12). | Implementar cifrado en reposo y TLS. |
| **Continuidad del Negocio** | 1 (Inicial) | Ausencia de BCP/DRP (NC‑04). | Desarrollar y probar BCP. |
| **Formación y Concienciación** | 1 (Inicial) | No hay programa (NC‑06). | Lanzar campaña de concienciación. |

**Puntuación global de exposición:** **176** (según la metodología de consolidación). Los cinco riesgos críticos (R01‑R05) representan **≈ 54 %** del total; su mitigación reducirá la exposición por debajo de 100 puntos.

---

## 9. Recomendaciones Finales  

1. **Ejecutar el Plan de Acción Correctivo** en los plazos indicados; monitorizar los indicadores de cierre mensualmente.  
2. **Consolidar la documentación** de procesos (incidentes, continuidad, DPIA, ARCO) en un repositorio único con control de versiones.  
3. **Realizar auditorías internas trimestrales** para validar la implementación de los controles críticos y actualizar la matriz de riesgos.  
4. **Implementar una solución SIEM** que correlacione los logs de autenticación, firewall y exportaciones de datos para detección temprana de incidentes.  
5. **Revisar anualmente** la Declaración de Aplicabilidad ISO 27001 y actualizarla conforme a la evolución del negocio y a los resultados de auditoría.

---

*Este informe se elabora con la única finalidad de proporcionar a la Dirección, al DPO y a los auditores externos una visión completa y trazable del estado de cumplimiento normativo de la organización, con la evidencia correspondiente y un plan de acción detallado para la remediación de las no conformidades detectadas.*  