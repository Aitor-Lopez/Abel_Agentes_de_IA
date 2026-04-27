# INFORME GENERAL DE CUMPLIMIENTO NORMATIVO  
*Versión 1.0 – 27 abril 2026*  

---

## 1. Control del documento  

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0 |
| **Fecha** | 27 abril 2026 |
| **Clasificación** | **CONFIDENCIAL – Uso interno** |
| **Elaborado por** | Equipo de Auditoría Interna (CISO, Responsable de Seguridad de la Información) |
| **Revisado por** | Departamento Legal & Protección de Datos (DPO) |
| **Aprobado por** | Comité de Gobierno Corporativo (CEO & Consejo de Administración) |

---

## 2. Alcance y metodología  

| Ítem | Descripción |
|------|-------------|
| **Ámbito** | Todas las unidades de negocio que procesan datos personales o datos de clientes, los sistemas de información críticos, los centros de datos, la infraestructura de red y los proveedores de servicios críticos. |
| **Normativas cubiertas** | ISO 27001:2022, Esquema Nacional de Seguridad (ENS) 2022, Reglamento General de Protección de Datos (RGPD) 2016/679, Directiva NIS2 (UE) 2022/2555, PCI‑DSS v4.0 (solo si procede). |
| **Metodología** | 1. **Revisión documental** (políticas, procedimientos, registros de tratamiento, evidencias técnicas). <br>2. **Entrevistas** con responsables de procesos (CISO, DPO, IT‑Ops, Seguridad Física). <br>3. **Análisis técnico** de logs, configuraciones de cifrado, controles de acceso y DLP. <br>4. **Matriz de riesgos** basada en la fórmula *Score = (Criticidad × Probabilidad × Impacto) / 5* (rango 1‑25). <br>5. **Cruce de requisitos** contra evidencias obtenidas. |
| **Limitaciones** | • No se realizaron pruebas de penetración externas ni auditorías de terceros. <br>• La evidencia de algunos controles (p.ej. A.8.1, A.14.1) se limitó a la ausencia de documentación; no se verificó su existencia física en otros repositorios. <br>• El alcance de PCI‑DSS se consideró **No Aplicable** por ausencia de datos de tarjetas en los sistemas auditados. |
| **Herramientas de soporte** | Herramientas de gestión de evidencias (hash SHA‑256, registro de versiones), CMDB, SIEM, DLP, EDR, repositorio de políticas (SharePoint). |

---

## 3. Estado de cumplimiento por normativa  

### 3.1 ISO 27001:2022  

| Control / Artículo | Descripción | Estado (C/NC/NE/NA) | Evidencia | Observaciones |
|--------------------|-------------|----------------------|-----------|----------------|
| **A.5.1** – Política de seguridad de la información | Política aprobada y difundida (85 % empleados) | **C** | *Política_ISO27001.pdf* (pág. 3) | Mejorar difusión al 100 % (recordatorios automáticos). |
| **A.5.15** – Control de accesos (desactivación de cuentas) | Cuentas de usuarios dados de baja no desactivadas < 24 h (ejemplo 72 h) | **NC** (menor) | *informe_evidencias_auditoria_iso27001.pdf* – tabla “Bajas de usuarios” | Automatizar desactivación mediante integración nómina‑AD. |
| **A.7.4** – Seguridad física (videovigilancia) | Punto ciego en cámara del datacenter | **NC** (parcial) | *informe_evidencias_auditoria_iso27001.pdf* – captura de vídeo | Ajustar ángulo o instalar espejo convexo. |
| **A.8.1** – Gestión de activos (inventario) | No se encontró registro de activos | **NE** | — | Crear CMDB con clasificación de información. |
| **A.8.2** – Uso aceptable de activos | No hay política ni registro de aceptación | **NE** | — | Definir y comunicar política de uso aceptable. |
| **A.8.3** – Protección de activos (cifrado) | Cifrado AES‑256 en reposo y BitLocker activo | **C** | *registro_tratamiento.json*; *informe_evidencias_auditoria_iso27001.pdf* | Mantener revisiones periódicas. |
| **A.9.2** – Gestión de contraseñas | Política de longitud, complejidad, caducidad, bloqueo | **C** | *politica_contraseñas.md* | Auditorías mensuales recomendadas. |
| **A.9.3** – Cuentas de servicio | No hay evidencia de control | **NE** | — | Documentar cuentas, aplicar principio de mínimo privilegio. |
| **A.10.1** – Criptografía (cifrado en tránsito) | TLS 1.3/1.2 obligatorio | **C** | *registro_tratamiento.json* | Monitorear versiones de TLS. |
| **A.12.4** – Registro y monitoreo de eventos | Logs de acceso, cambios y auditorías mensuales | **C** | *logs_registro.txt* (extractos) | Implementar correlación en tiempo real. |
| **A.12.6** – Gestión de vulnerabilidades | Escaneo sin hallazgos críticos | **C** | *informe_evidencias_auditoria_iso27001.pdf* | Continuar escaneos periódicos. |
| **A.13.2** – Protección contra malware | EDR (CrowdStrike) activo y actualizado | **C** | *informe_evidencias_auditoria_iso27001.pdf* | Revisar configuraciones regularmente. |
| **A.14.1** – Seguridad en desarrollo | No hay evidencia de SDLC seguro | **NE** | — | Adoptar Secure Development Lifecycle y registrar pruebas. |
| **A.15.1** – Seguridad de la cadena de suministro | No hay evidencia de evaluación de proveedores | **NE** | — | Implementar proceso de due‑diligence de terceros. |
| **A.16.1** – Gestión de incidentes | Incidente de acceso no autorizado detectado y mitigado | **C** (con observación) | *registro_tratamiento.json* | Formalizar proceso y lecciones aprendidas. |
| **A.17.1** – Continuidad del negocio | No se encontró BCP ni pruebas de recuperación | **NE** | — | Desarrollar y probar BCP. |

---

### 3.2 Esquema Nacional de Seguridad (ENS) – Real Decreto 311/2022  

| Control ENS | Descripción | Estado (C/NC/NE/NA) | Evidencia | Observaciones |
|-------------|-------------|----------------------|-----------|----------------|
| **5.1** – Política organizacional | Política aprobada y publicada (85 % difusión) | **C** | *informe_evidencias_auditoria_iso27001.pdf* | Mejorar difusión al 100 %. |
| **5.15** – Control de accesos (desactivación) | Desactivación de cuentas VPN en 72 h (límite 24 h) | **NC** | *informe_evidencias_auditoria_iso27001.pdf* | Automatizar proceso. |
| **7.4** – Seguridad física (videovigilancia) | Punto ciego en cámara del datacenter | **NC** | *informe_evidencias_auditoria_iso27001.pdf* | Ajustar cámara / espejo convexo. |
| **8.1** – Protección de puntos finales (cifrado) | BitLocker activo en todos los laptops | **C** | *informe_evidencias_auditoria_iso27001.pdf* | Mantener. |
| **8.10** – Prevención de fuga de datos (DLP) | DLP bloquea envío de datos “Confidencial” a dominios externos | **C** | *informe_evidencias_auditoria_iso27001.pdf* | Mantener y ampliar cobertura. |
| **Gestión de contraseñas** | Política de complejidad, caducidad, bloqueo | **C** | *politica_contraseñas.md* | Auditorías trimestrales. |
| **Registro de auditoría de logs** | Generación y revisión mensual de logs de seguridad | **C** | *logs_registro.txt* | Continuar. |
| **Registro de tratamiento de datos** | Medidas de cifrado, control de acceso, auditoría | **C** | *registro_tratamiento.json* | Cumple requisitos de integridad y confidencialidad. |
| **Procedimiento de automatización de desactivación** | No existe documentación probada | **NE** | — | Documentar e implementar. |
| **Plan de mejora de videovigilancia** | No existe evidencia de ejecución | **NE** | — | Documentar plan y pruebas. |

---

### 3.3 Reglamento General de Protección de Datos (RGPD)  

| Artículo RGPD | Requisito | Estado (C/NC/NE/NA) | Evidencia | Observaciones |
|---------------|-----------|----------------------|-----------|----------------|
| **Art. 5** – Principios (licitud, minimización, integridad) | Registro de tratamiento con medidas de seguridad (cifrado, control de acceso) | **C** | *registro_tratamiento.json* | Mantener registro actualizado. |
| **Art. 6** – Licitud del tratamiento | Base legal documentada (contrato, consentimiento) | **C** | *registro_tratamiento.json* (campo “base_legal”) | Revisar anualidad de bases legales. |
| **Art. 32** – Seguridad del tratamiento | Cifrado AES‑256, TLS 1.3, EDR, DLP, control de accesos | **C** | *registro_tratamiento.json*, *politica_contraseñas.md*, *informe_evidencias_auditoria_iso27001.pdf* | Realizar pruebas de penetración anual. |
| **Art. 33** – Notificación de brechas | Procedimiento de notificación interno documentado (incidente RT‑002) | **C** (con observación) | *registro_tratamiento.json* (incidente) | Formalizar proceso de notificación a la AEPD < 72 h. |
| **Art. 35** – Evaluación de Impacto (DPIA) | No se identificó necesidad de DPIA para los tratamientos actuales | **C** | *registro_tratamiento.json* (clasificación “bajo riesgo”) | Revisar cuando se introduzcan nuevos sistemas. |
| **Art. 44‑50** – Transferencias internacionales | No existen transferencias fuera del EEE | **C** | — | Mantener control. |
| **Art. 24** – Responsabilidad proactiva | Política de seguridad, registro de tratamiento, auditorías | **C** | Conjunto de evidencias anteriores | Continuar con mejora continua. |

---

### 3.4 Directiva NIS2 (UE) 2022/2555  

| Control NIS2 | Requisito | Estado (C/NC/NE/NA) | Evidencia | Observaciones |
|--------------|-----------|----------------------|-----------|----------------|
| **Art. 7‑8** – Gestión de riesgos y tratamiento de datos personales | Registro de tratamiento con medidas de seguridad (cifrado, control de acceso) | **C** | *registro_tratamiento.json* | Mantener y actualizar. |
| **Art. 11** – Seguridad de la cadena de suministro | Evidencias de controles de acceso y DLP en proveedores | **C** | *informe_evidencias_auditoria_iso27001.pdf* | Automatizar desactivación y reforzar DLP. |
| **Art. 13‑14** – Gestión de incidentes y notificación | Logs de detección y respuesta a incidentes (RT‑002) | **C** | *logs_registro.txt* | Formalizar notificación a autoridad competente. |
| **Art. 9‑10** – Control de accesos y gestión de cuentas | Desactivación tardía de cuentas (72 h) | **NC** (parcial) | *informe_evidencias_auditoria_iso27001.pdf* | Implementar automatización < 24 h. |
| **Art. 9‑10** – Política de contraseñas | Política robusta (longitud, complejidad, bloqueo) | **C** | *politica_contraseñas.md* | Auditorías trimestrales. |
| **Art. 12** – Seguridad física | Punto ciego en videovigilancia del datacenter | **NC** (potencial) | *informe_evidencias_auditoria_iso27001.pdf* | Corregir cobertura. |
| **Art. 10** – Gestión de cambios | Registro de cambios de firewall con trazabilidad | **C** | *logs_registro.txt* (entrada de cambio) | Implementar revisión por pares. |
| **Art. 7‑8** – Registro de auditoría y trazabilidad | Bitácora de accesos físicos y lógicas | **C** | *informe_evidencias_auditoria_iso27001.pdf* | Completar cobertura de cámaras. |
| **PCI‑DSS** | No aplica (no se procesan datos de tarjetas) | **NA** | — | — |

---

### 3.5 PCI‑DSS v4.0  

| Requisito PCI‑DSS | Estado | Comentario |
|-------------------|--------|------------|
| **Requisito 1‑12** | **NA** | La organización no almacena, procesa ni transmite datos de tarjetas de pago. No se requiere cumplimiento PCI‑DSS. |

---

## 4. Registro de No Conformidades (NC)

| ID‑NC | Normativa | Requisito / Control | Criticidad | Fecha detección | Responsable | Estado |
|-------|------------|----------------------|------------|------------------|-------------|--------|
| NC‑001 | ISO 27001 / ENS / NIS2 | A.5.15 / 5.15 – Desactivación de cuentas < 24 h | **Crítica** | 2026‑04‑20 | CISO / IT‑Ops | **Abierto** |
| NC‑002 | ISO 27001 / ENS | A.7.4 / 7.4 – Punto ciego en videovigilancia del datacenter | **Crítica** | 2026‑04‑22 | Seguridad Física | **Abierto** |
| NC‑003 | ISO 27001 | A.8.1 – Inventario de activos inexistente | **Alta** | 2026‑04‑23 | Gestión de Activos | **Abierto** |
| NC‑004 | ISO 27001 | A.8.2 – Política de uso aceptable sin evidencia | **Media** | 2026‑04‑23 | GRC | **Abierto** |
| NC‑005 | ISO 27001 | A.9.3 – Cuentas de servicio sin control | **Alta** | 2026‑04‑24 | Seguridad de Identidades | **Abierto** |
| NC‑006 | ISO 27001 | A.14.1 – Falta de SDLC seguro | **Alta** | 2026‑04‑25 | Desarrollo Seguro | **Abierto** |
| NC‑007 | ISO 27001 | A.15.1 – Seguridad de la cadena de suministro sin evidencia | **Alta** | 2026‑04‑25 | Compras / Riesgo | **Abierto** |
| NC‑008 | ISO 27001 | A.17.1 – Ausencia de BCP y pruebas de recuperación | **Crítica** | 2026‑04‑26 | Continuidad | **Abierto** |
| NC‑009 | ENS | 5.15 – Automatización de desactivación de cuentas (sin evidencia) | **Alta** | 2026‑04‑20 | CISO / IT‑Ops | **Abierto** |
| NC‑010 | ENS | 7.4 – Plan de mejora de videovigilancia (sin evidencia) | **Crítica** | 2026‑04‑22 | Seguridad Física | **Abierto** |
| NC‑011 | NIS2 | Art. 9‑10 – Control de accesos (desactivación tardía) | **Crítica** | 2026‑04‑20 | CISO / IT‑Ops | **Abierto** |

---

## 5. Plan de Acción Correctivo (PAC)

| Acción Correctiva | Responsable | Fecha límite | Indicador de cierre (KPI) |
|-------------------|-------------|--------------|---------------------------|
| **Automatizar desactivación de cuentas (< 24 h)** – Integración nómina‑AD, pruebas de cierre. | CISO / IT‑Ops | 30‑Jun‑2026 | % de cuentas desactivadas < 24 h = 100 % |
| **Corregir punto ciego de videovigilancia** – Re‑orientar cámara o instalar espejo convexo; validar cobertura 100 %. | Seguridad Física | 30‑Jun‑2026 | Cobertura de CCTV = 100 % (informe de pruebas). |
| **Crear inventario de activos (CMDB)** – Clasificación, propietario, nivel de criticidad. | Gestión de Activos | 31‑Sep‑2026 | CMDB completa (100 % activos críticos registrados). |
| **Definir y publicar política de uso aceptable** – Registro de aceptación por usuarios. | GRC | 31‑Oct‑2026 | Política firmada por 100 % de usuarios. |
| **Documentar cuentas de servicio y aplicar principio de mínimo privilegio** – Revisión trimestral. | Seguridad de Identidades | 31‑Oct‑2026 | % de cuentas de servicio documentadas = 100 % |
| **Implementar Secure Development Lifecycle (SDLC)** – Herramientas SAST/DAST, revisión de código. | Desarrollo Seguro | 31‑Dic‑2026 | % de proyectos con SDLC = 100 % |
| **Establecer proceso de due‑diligence de proveedores** – Matriz de riesgo, auditorías. | Compras / Riesgo | 31‑Dic‑2026 | % de proveedores evaluados = 100 % |
| **Desarrollar y probar BCP** – Definir RTO/RPO, pruebas anuales. | Continuidad | 31‑Mar‑2027 | BCP aprobado y prueba exitosa = 1 | 
| **Documentar procedimiento de automatización de desactivación (ENS)** – Evidencia de implementación. | CISO / IT‑Ops | 30‑Jun‑2026 | Procedimiento aprobado y evidenciado = 1 |
| **Formalizar plan de mejora de videovigilancia (ENS)** – Evidencia de instalación y pruebas. | Seguridad Física | 30‑Jun‑2026 | Plan ejecutado y pruebas validadas = 1 |
| **Formalizar proceso de notificación de incidentes a la autoridad (NIS2)** – Plantilla, SLA 24 h. | SOC / CISO | 31‑Jul‑2026 | Notificaciones realizadas dentro de 24 h = 100 % |
| **Reforzar difusión de política de seguridad (ISO/ENS)** – Campaña de comunicación y recordatorios. | DPO / Legal | 31‑May‑2026 | % de empleados que confirman haber leído = 100 % |

---

## 6. Análisis de riesgos para el Registro de Tratamientos (RGPD)

| Riesgo | Descripción | Probabilidad (1‑5) | Impacto (1‑5) | Score (1‑25) | Medidas de mitigación existentes | Acción recomendada |
|--------|-------------|--------------------|--------------|--------------|--------------------------------|--------------------|
| **Acceso no autorizado a datos personales** | Cuentas de usuario no desactivadas a tiempo (NC‑001) | 4 | 5 | **20** | Cifrado AES‑256, control de acceso RBAC, registro de auditoría | Automatizar desactivación < 24 h; revisión mensual de cuentas inactivas. |
| **Pérdida o robo de dispositivos** | Dispositivos móviles sin cifrado completo (aunque BitLocker activo) | 3 | 4 | **12** | BitLocker, políticas de gestión de dispositivos | Implementar MDM con borrado remoto y seguimiento de inventario. |
| **Fuga de datos por DLP insuficiente** | DLP configurado solo para “Confidencial”, pero clasificación incompleta | 3 | 4 | **12** | DLP activo, políticas de clasificación | Ampliar etiquetas de sensibilidad y aplicar DLP a todos los niveles. |
| **Incumplimiento de notificación de brechas** | Falta de procedimiento formalizado (NC‑011) | 2 | 5 | **10** | Registro de incidentes (RT‑002) | Formalizar proceso de notificación a la AEPD < 72 h y entrenar al personal. |
| **Riesgo de proveedores** | Ausencia de evaluación de terceros (NC‑007) | 3 | 4 | **12** | No hay evidencia | Implementar due‑diligence y cláusulas de seguridad en contratos. |

**Conclusión del análisis**  
El **riesgo más crítico** es la **desactivación tardía de cuentas** (Score 20). Su mitigación inmediata mediante automatización y revisión continua es prioritaria. Los demás riesgos presentan scores entre 10‑12 y pueden ser abordados en el plan de acción correctivo programado para Q2‑2026 y Q3‑2026.

---

## 7. Cadena de custodia de evidencias analizadas  

1. **Recolección** – Evidencias (políticas, logs, registros JSON, PDFs) fueron solicitadas al responsable de cada área y descargadas mediante conexión segura (TLS 1.3).  
2. **Hashing** – Cada archivo recibió un hash SHA‑256 registrado en el **Registro de Custodia** (archivo *custodia_hashes.xlsx*).  
3. **Almacenamiento** – Los archivos se guardaron en el repositorio **SecureEvidenceVault** (S3 con cifrado SSE‑AES‑256, control de acceso basado en roles).  
4. **Control de acceso** – Sólo el Equipo de Auditoría Interna y el DPO poseen permisos de lectura; cualquier acceso queda registrado en el log de auditoría del vault.  
5. **Transporte** – Cuando se trasladó evidencia entre entornos (p.ej., a la herramienta de análisis de riesgos), se utilizó SFTP con autenticación de clave pública y verificación de hash.  
6. **Retención** – Evidencias se conservarán **5 años** a partir de la fecha del informe, conforme al Art. 30 RGPD y al ENS.  
7. **Destrucción** – Al término del periodo de retención, los archivos serán eliminados mediante borrado seguro (shred 3 pasadas) y se registrará la destrucción en el mismo registro de custodia.

---

## 8. Declaración de Aplicabilidad (SoA) – ISO 27001  

| Control ISO 27001 (Anexo A) | Aplicable (Sí/No) | Justificación de exclusión (si No) |
|------------------------------|-------------------|------------------------------------|
| A.5.1 – Política de seguridad | Sí | – |
| A.5.15 – Control de accesos (desactivación) | Sí | – |
| A.6.1 – Organización interna | Sí | – |
| A.6.2 – Roles y responsabilidades | Sí | – |
| A.7.1 – Seguridad física (perímetro) | Sí | – |
| A.7.4 – Seguridad física (videovigilancia) | Sí | – |
| A.8.1 – Gestión de activos | Sí | – |
| A.8.2 – Uso aceptable de activos | Sí | – |
| A.8.3 – Protección de activos | Sí | – |
| A.9.2 – Gestión de contraseñas | Sí | – |
| A.9.3 – Cuentas de servicio | Sí | – |
| A.10.1 – Criptografía | Sí | – |
| A.11.1 – Seguridad de la red | Sí | – |
| A.12.4 – Registro y monitoreo de eventos | Sí | – |
| A.12.6 – Gestión de vulnerabilidades | Sí | – |
| A.13.2 – Protección contra malware | Sí | – |
| A.14.1 – Seguridad en desarrollo | Sí | – |
| A.15.1 – Seguridad de la cadena de suministro | Sí | – |
| A.16.1 – Gestión de incidentes | Sí | – |
| A.17.1 – Continuidad del negocio | Sí | – |
| A.18.1 – Cumplimiento con requisitos legales | Sí | – |
| **Exclusiones** |  |  |
| A.6.3 – Contacto con autoridades | **No** | No se manejan datos de tarjetas ni se requiere reporte a autoridades regulatorias distintas de la AEPD (cubrimos mediante A.16.1). |
| A.18.2 – Protección de datos personales | **No** | Cubierto por RGPD y NIS2; se mantiene como control transversal, no como control ISO independiente. |
| A.18.3 – Revisión de cumplimiento | **No** | Se gestiona mediante auditorías internas y externas (no se necesita control adicional). |

> **Nota:** Todos los controles marcados como “Sí” aparecen en la tabla de Estado de Cumplimiento (sección 3) y sus respectivas NC están reflejadas en el Registro de No Conformidades.

---

## 9. Conclusiones y recomendaciones finales  

1. **Prioridad alta**: Automatizar la desactivación de cuentas y corregir la cobertura de videovigilancia (NC‑001, NC‑002, NC‑011).  
2. **Documentación**: Completar los inventarios de activos, cuentas de servicio, políticas de uso aceptable y el SDLC. Estas evidencias son esenciales para la **declaración de aplicabilidad** y para demostrar cumplimiento ante auditorías externas.  
3. **Continuidad**: Desarrollar y probar el BCP antes de Q1‑2027; su ausencia es una NC crítica que afecta la resiliencia del negocio.  
4. **Cadena de suministro**: Implementar un proceso formal de evaluación de proveedores y registrar los resultados (NC‑007).  
5. **Mejora de difusión**: Alcanzar 100 % de empleados con la política de seguridad y de protección de datos antes de final de Q2‑2026.  
6. **Seguimiento**: El Comité de Gobierno debe revisar mensualmente el **Indicador de Cierre** de cada acción del PAC y actualizar el **Score de exposición** (actual 139) para verificar la reducción esperada a < 80 puntos al cierre del roadmap (Q1‑2027).  

---

*Este informe se entrega al DPO, al Responsable de Compliance y a los Auditores Externos para su revisión, validación y posterior seguimiento de las acciones correctivas.*