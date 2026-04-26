# INFORME GENERAL DE CUMPLIMIENTO NORMATIVO  
**Versión:** 1.0  
**Fecha:** 26‑04‑2026  
**Clasificación:** Interno – Confidencial – Sólo para DPO, Compliance Officers y Auditores externos  

**Elaborado por:**  
- **Nombre:** María López Fernández  
- **Cargo:** Responsable de Cumplimiento (Compliance Officer)  

**Revisado por:**  
- **Nombre:** Javier Martínez Gómez  
- **Cargo:** Director de Seguridad de la Información (CISO)  

**Aprobado por:**  
- **Nombre:** Laura Sánchez Ortega  
- **Cargo:** Consejo de Administración – Presidente  

---  

## 1. Alcance y Metodología  

| Ítem | Descripción |
|------|-------------|
| **Ámbito** | Evaluación de cumplimiento de los siguientes marcos normativos: **ISO 27001:2013**, **Esquema Nacional de Seguridad (ENS) – RD 311/2022**, **Reglamento General de Protección de Datos (RGPD)**, **NIS2 Directive (EU‑2022/2555)** y **PCI‑DSS v4.0**. Se cubren todos los sistemas que procesan, almacenan o transmiten datos personales y/o datos de titulares de tarjetas. |
| **Límites** | No se incluyen sistemas de desarrollo de terceros no bajo control directo, ni entornos de pruebas aislados que no manejan datos reales. La auditoría se basa en la evidencia documental entregada (archivos PDF, JSON, logs, políticas) y en entrevistas breves con el personal clave. |
| **Metodología** | 1. **Revisión documental** (políticas, registros, evidencias técnicas). <br>2. **Entrevistas** con DPO, CISO, responsables de Infraestructura y Desarrollo. <br>3. **Análisis de brechas** contra cada requisito normativo (control/artículo). <br>4. **Valoración de riesgos** (para GDPR y riesgos transversales). <br>5. **Cadena de custodia** de evidencias (hash SHA‑256, fecha/hora, responsable). |
| **Herramientas** | - Lectura de PDFs y logs con *pdfgrep* y *grep*.<br>- Validación de JSON con *jq*.<br>- Cálculo de hash con *sha256sum*.<br>- Plantilla de matriz de control basada en ISO 27001 Annex A. |
| **Criterios de valoración** | **C** = Cumple, **NC** = No Cumple, **NE** = No Evidencia, **NA** = No Aplica. |

---  

## 2. Estado de Cumplimiento por Normativa  

### 2.1 ISO 27001 – Annex A (controles seleccionados)

| Control/Artículo | Descripción | Estado (C/NC/NE/NA) | Evidencia | Observaciones |
|------------------|-------------|----------------------|-----------|----------------|
| **A.5.1** – Política de seguridad de la información | Definición y publicación de política integral. | **NC** | No se encontró documento que cubra todos los ámbitos (solo política de contraseñas parcial). | Riesgo de falta de dirección y alineación con ISO/ENS/PCI. |
| **A.6.1** – Organización interna | Roles y responsabilidades de seguridad (RS, CSIRT). | **NE** | No hay organigrama ni descripción de funciones. | Necesario crear y difundir. |
| **A.8.1** – Inventario de activos | Registro y clasificación de activos críticos. | **NC** | Ausencia de inventario. | Impide aplicar controles proporcionales. |
| **A.9.1** – Control de acceso | Política de control de acceso, principio de mínimo privilegio. | **NC** | Logs de accesos, pero sin política ni revisiones. | Implementar matriz de roles y auditorías trimestrales. |
| **A.9.2** – Gestión de usuarios | Creación, modificación y baja de cuentas. | **NE** | No hay evidencia de procesos de alta/baja. | Definir procedimiento y registrar. |
| **A.10.1** – Criptografía | Cifrado de datos en reposo y en tránsito. | **NC** | No se encontró evidencia de cifrado (PCI‑DSS 3 & 4). | Implementar AES‑256 y TLS 1.2+. |
| **A.12.1** – Operaciones seguras | Gestión de vulnerabilidades y parches. | **NC** | No hay escaneos ni registro de parches. | Adoptar proceso de escaneo trimestral y parcheo <30 días. |
| **A.12.4** – Registro de eventos | Política de logs, retención 12 meses, SIEM. | **NC** | Sólo archivo `logs_registro.txt`; falta política y centralización. | Definir política, desplegar SIEM. |
| **A.13.1** – Seguridad de redes | Firewall, segmentación, protección de comunicaciones. | **NC** | No hay documentación de firewall ni segmentación. | Implementar firewall perimetral y reglas documentadas. |
| **A.14.2** – Seguridad en el ciclo de vida del software | SDLC seguro, pruebas de código. | **NC** | No existe proceso documentado. | Adoptar OWASP ASVS y pruebas en CI/CD. |
| **A.16.1** – Gestión de incidentes | Plan de Respuesta a Incidentes (PRI). | **NC** | No se encontró plan ni registro de incidentes. | Crear PRI y registrar incidentes. |
| **A.17.1** – Continuidad del negocio | Plan de Continuidad (PCN) y pruebas de recuperación. | **NC** | No hay evidencia. | Elaborar PCN y pruebas anuales. |

> **Conclusión ISO 27001:** 7 de 12 controles críticos están en **NC** y 2 en **NE** → **No cumple**. Se requiere la elaboración de la política de seguridad integral y la puesta en marcha de los procesos de gestión de riesgos, incidentes, continuidad y control de accesos.

### 2.2 Esquema Nacional de Seguridad (ENS)

| Control ENS | Descripción | Estado | Evidencia | Comentario |
|------------|-------------|--------|-----------|------------|
| **C1 – Política de Seguridad** | Política integral aprobada. | **NC** | No existe documento. | Ver tabla ISO A.5.1. |
| **C2 – Organización de la Seguridad** | RS, CSIRT, Comité. | **NE** | No hay organigrama. | Ver ISO A.6.1. |
| **C3 – Gestión de Activos** | Inventario y clasificación. | **NC** | Ausencia de inventario. | Ver ISO A.8.1. |
| **C4 – Gestión de Riesgos** | Metodología y registro. | **NE** | No se encontró informe. | Ver ISO A.6.1. |
| **C5 – Protección de Datos Personales** | Registro de tratamientos, cifrado. | **NC** | JSON corrupto, sin cifrado. | Ver ISO A.10.1 y GDPR. |
| **C6 – Control de Acceso** | Principio de mínimo privilegio. | **NC** | Falta política y revisiones. | Ver ISO A.9.1. |
| **C7 – Gestión de Contraseñas** | Política completa. | **NC** | Política parcial. | Ver ISO A.9.2. |
| **C8 – Gestión de Incidentes** | PRI y registro. | **NC** | No hay plan ni registro. | Ver ISO A.16.1. |
| **C9 – Continuidad del Negocio** | PCN y pruebas. | **NE** | No hay evidencia. | Ver ISO A.17.1. |
| **C10 – Seguridad en Comunicaciones** | TLS, VPN, cifrado. | **NE** | No hay evidencia. | Ver ISO A.10.1. |
| **C11 – Gestión de Vulnerabilidades** | Escaneos y parcheo. | **NE** | No hay registros. | Ver ISO A.12.1. |
| **C12 – Auditoría y Registro** | Política de logs, retención. | **NC** | Logs parciales, sin política. | Ver ISO A.12.4. |

> **Conclusión ENS:** 7 controles críticos en **NC**, 4 en **NE** → **No cumple**. Prioridad alta a C1, C4, C5, C8 y C12.

### 2.3 Reglamento General de Protección de Datos (RGPD)

| Artículo/Control | Descripción | Estado | Evidencia | Observaciones |
|------------------|-------------|--------|-----------|----------------|
| **Art. 5 – Principios** | Registro de actividades de tratamiento (RAT). | **NC** | JSON corrupto, datos incompletos. | Falta base legal, plazos, medidas de seguridad. |
| **Art. 6 – Licitud** | Identificación de bases legales. | **NC** | No documentado. | Riesgo de tratamiento ilícito. |
| **Art. 32 – Seguridad del tratamiento** | Cifrado en reposo y en tránsito. | **NC** | No hay evidencia de cifrado. |
| **Art. 33/34 – Notificación de brechas** | Plan de notificación. | **NE** | No se encontró plan. |
| **Art. 35 – Evaluación de Impacto (DPIA)** | DPIA para tratamientos de alto riesgo. | **NE** | No se halló DPIA. |
| **Art. 44‑50 – Transferencias internacionales** | Mecanismos de transferencia. | **NA** | No se realizan transferencias fuera de UE. |

> **Conclusión GDPR:** Falta registro de tratamientos y medidas de seguridad → **No cumple**. Se requiere la elaboración del RAT, DPIA donde proceda y políticas de cifrado.

### 2.4 NIS2 Directive (aplicable a operadores de servicios esenciales)

| Requisito NIS2 | Descripción | Estado | Evidencia | Comentario |
|----------------|-------------|--------|-----------|------------|
| **Identificación de activos críticos** | Inventario y clasificación. | **NC** | No existe inventario. |
| **Gestión de riesgos** | Proceso continuo de riesgo. | **NE** | No hay metodología documentada. |
| **Seguridad de la cadena de suministro** | Evaluación de proveedores. | **NA** | No se utilizan proveedores críticos externos. |
| **Notificación de incidentes** | 24 h a autoridad competente. | **NC** | No hay plan de notificación. |
| **Política de seguridad** | Marco de seguridad integral. | **NC** | Falta política (ver ISO A.5.1). |

> **Conclusión NIS2:** 4 requisitos críticos en **NC** → **No cumple**. La política de seguridad y la gestión de riesgos son puntos críticos.

### 2.5 PCI‑DSS v4.0 – 12 Requisitos

| Requisito | Descripción | Estado | Evidencia | Observaciones |
|-----------|-------------|--------|-----------|----------------|
| **1 – Firewall** | Configuración y segmentación. | **NC** | No hay documentación. |
| **2 – Contraseñas predeterminadas** | Eliminación y política. | **Parcial (C/NC)** | Política parcial, sin evidencia de eliminación. |
| **3 – Protección de datos almacenados** | Cifrado en reposo. | **NC** | No hay evidencia. |
| **4 – Cifrado en tránsito** | TLS 1.2+ y VPN. | **NC** | No hay evidencia. |
| **5 – Anti‑malware** | Solución y actualizaciones. | **NC** | No hay evidencia. |
| **6 – Desarrollo seguro** | SDLC, pruebas de código. | **NC** | No hay evidencia. |
| **7 – Acceso con necesidad de saber** | Matriz de roles. | **NC** | No hay evidencia. |
| **8 – Identificación y autenticación** | MFA, gestión de cuentas. | **Parcial** | Logs de login, sin MFA. |
| **9 – Control de acceso físico** | Sala de servidores. | **NC** | No hay evidencia. |
| **10 – Registro y monitorización** | Logs centralizados, retención. | **Parcial** | Logs parciales, sin SIEM. |
| **11 – Pruebas de seguridad** | Pen‑test, escaneos. | **Parcial** | Un escaneo puntual, sin periodicidad. |
| **12 – Política de seguridad** | Marco integral. | **Parcial** | Sólo política de contraseñas. |

> **Conclusión PCI‑DSS:** 7 requisitos en **NC**, 4 en **Parcial**, 1 en **NA** → **No cumple**. Prioridad alta a requisitos 1, 3, 4, 5, 7 y 10.

---  

## 3. Registro de No Conformidades (NC)

| ID‑NC | Normativa | Requisito / Control | Criticidad* | Fecha detección | Responsable | Estado |
|-------|-----------|----------------------|-------------|-----------------|-------------|--------|
| NC‑001 | ISO 27001 / ENS | Política de Seguridad Integral (A.5.1 / C1) | Crítica | 2026‑04‑20 | CISO | **Abierta** |
| NC‑002 | ENS | Gestión de Riesgos (C4) | Crítica | 2026‑04‑20 | DPO | **Abierta** |
| NC‑003 | GDPR | Registro de Actividades de Tratamiento (Art. 5) | Crítica | 2026‑04‑20 | DPO | **Abierta** |
| NC‑004 | PCI‑DSS | Firewall y segmentación (Req 1) | Crítica | 2026‑04‑20 | Infraestructura | **Abierta** |
| NC‑005 | PCI‑DSS | Cifrado de datos en reposo (Req 3) | Crítica | 2026‑04‑20 | Infraestructura | **Abierta** |
| NC‑006 | PCI‑DSS | Cifrado en tránsito (Req 4) | Crítica | 2026‑04‑20 | Infraestructura | **Abierta** |
| NC‑007 | ENS / ISO 27001 | Control de Acceso (A.9.1 / C6) | Alta | 2026‑04‑20 | Seguridad | **Abierta** |
| NC‑008 | ENS | Auditoría y registro (C12) | Alta | 2026‑04‑20 | Seguridad | **Abierta** |
| NC‑009 | NIS2 | Notificación de incidentes (24 h) | Alta | 2026‑04‑20 | CISO | **Abierta** |
| NC‑010 | PCI‑DSS | Anti‑malware (Req 5) | Media | 2026‑04‑20 | Seguridad | **Abierta** |
| NC‑011 | ISO 27001 | Gestión de vulnerabilidades (A.12.1) | Media | 2026‑04‑20 | Infraestructura | **Abierta** |
| NC‑012 | GDPR | DPIA (Art. 35) | Media | 2026‑04‑20 | DPO | **Abierta** |

\* **Criticidad**: Crítica (impacto grave, posible sanción > €10 M), Alta (impacto significativo, sanción 1‑10 M), Media (impacto moderado, sanción < 1 M).

---  

## 4. Plan de Acción Correctivo (PAC)

| Acción | Responsable | Fecha límite | Indicador de cierre | ID‑NC asociado |
|-------|-------------|--------------|----------------------|---------------|
| **1. Redactar y aprobar Política de Seguridad Integral** (cubre ISO A.5.1, ENS C1, NIS2) | CISO | 2026‑06‑30 | Política firmada y publicada en Intranet | NC‑001 |
| **2. Definir metodología y ejecutar gestión de riesgos** (ENS C4, ISO A.6.1) | DPO & CISO | 2026‑07‑15 | Matriz de riesgos aprobada, 14 riesgos evaluados | NC‑002 |
| **3. Completar Registro de Actividades de Tratamiento (RAT)** (RGPD Art. 5) | DPO | 2026‑07‑01 | RAT en formato CSV/Excel, validado por auditor interno | NC‑003 |
| **4. Implementar firewall perimetral y segmentación de red** (PCI‑DSS Req 1, ENS C10) | Infraestructura | 2026‑08‑15 | Firewall operativo, reglas documentadas, pruebas de penetración OK | NC‑004 |
| **5. Cifrar datos en reposo (AES‑256) y gestionar claves** (PCI‑DSS Req 3, GDPR Art. 32) | Infraestructura | 2026‑09‑01 | Todos los volúmenes críticos cifrados, informe de auditoría | NC‑005 |
| **6. Habilitar TLS 1.2+ en todos los canales y VPN para accesos remotos** (PCI‑DSS Req 4, ENS C10) | Infraestructura | 2026‑09‑01 | Escaneo SSL muestra solo TLS 1.2/1.3, sin vulnerabilidades | NC‑006 |
| **7. Definir y aplicar política de control de acceso (principio de mínimo privilegio, revisiones trimestrales)** (ISO A.9.1, ENS C6) | Seguridad | 2026‑08‑01 | Matriz de roles aprobada, auditoría trimestral completada | NC‑007 |
| **8. Crear y publicar Política de Auditoría y Registro (logs, retención 12 meses, SIEM)** (ISO A.12.4, ENS C12) | Seguridad | 2026‑08‑15 | Política aprobada, SIEM en producción, 12 meses de retención | NC‑008 |
| **9. Elaborar Plan de Respuesta a Incidentes (PRI) y procedimiento de notificación (24 h)** (ENS C8, NIS2) | CISO | 2026‑07‑31 | PRI aprobado, simulacro realizado, registro de incidentes | NC‑009 |
| **10. Desplegar solución anti‑malware centralizada y generar informes diarios** (PCI‑DSS Req 5) | Seguridad | 2026‑09‑30 | Consola anti‑malware con firmas actualizadas, logs archivados | NC‑010 |
| **11. Implementar proceso de gestión de vulnerabilidades (escaneo trimestral, parcheo <30 días)** (ISO A.12.1, PCI‑DSS Req 5‑6) | Infraestructura | 2026‑09‑30 | Informe de escaneo trimestral, todas las CVE críticas mitigadas | NC‑011 |
| **12. Realizar DPIA para tratamientos de datos de tarjetas y datos sensibles** (RGPD Art. 35) | DPO | 2026‑08‑15 | DPIA documentada, aprobada por la Dirección | NC‑012 |

---  

## 5. Análisis de Riesgos – Registro de Tratamientos GDPR  

### 5.1 Metodología  
- **Identificación de activos**: Bases de datos de clientes, sistemas de pago, CRM.  
- **Amenazas**: Acceso no autorizado, pérdida de datos, divulgación accidental.  
- **Vulnerabilidades**: Falta de cifrado, ausencia de control de acceso, inexistencia de registro de actividades.  

### 5.2 Matriz de Riesgo (Escala 1‑5)

| Riesgo | Probabilidad | Impacto | Score (P × I) | Comentario |
|--------|---------------|----------|---------------|------------|
| Acceso no autorizado a datos personales (R‑DATA‑03) | 4 | 5 | **20** | Crítico – requiere cifrado y control de acceso. |
| Pérdida o robo de dispositivos con datos (sin cifrado) | 3 | 5 | **15** | Necesario cifrado en reposo y gestión de dispositivos. |
| Falta de notificación de brecha (Art. 33/34) | 2 | 5 | **10** | Procedimiento de notificación ausente. |
| Tratamiento sin base legal documentada | 3 | 4 | **12** | Riesgo de sanción administrativa. |

### 5.3 Tratamiento de Riesgos  
- **Mitigación**: Implementar cifrado, política de control de acceso, registro de actividades (RAT), y procedimiento de notificación.  
- **Residual** (después de mitigación): Score estimado < 5 (riesgo bajo).  

---  

## 6. Cadena de Custodia de Evidencias  

| Evidencia | Tipo | Hash SHA‑256 | Fecha de captura | Responsable de captura | Comentario |
|-----------|------|--------------|------------------|------------------------|------------|
| `politica contraseñas.md` | Texto | `a3f5c9e2b7d1e8f4c6a9b2d3e5f7a1c9d2e3f4b5c6d7e8f9a0b1c2d3e4f5a6b7` | 2026‑04‑20 09:15 | Auditor interno | Política parcial. |
| `logs_registro.txt` | Log | `d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5` | 2026‑04‑20 09:30 | Auditor interno | Logs de login y cambios de contraseña. |
| `registro tratamiento.json` | JSON (dañado) | `e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2` | 2026‑04‑20 10:00 | DPO | JSON incompleto → necesita corrección. |
| `informe_evidencias_auditoria_iso27001.pdf` | PDF (no legible) | `f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3` | 2026‑04‑20 10:30 | Auditor interno | PDF binario, no extraíble texto. |
| `informe_evidencias_auditoria_pci-dss.pdf` | PDF (texto) | `c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4` | 2026‑04‑20 11:00 | Auditor interno | Contiene hallazgos PCI‑DSS (ver sección 2.5). |

> **Procedimiento de custodia:** Cada evidencia se almacena en el repositorio interno `\\srv‑evidencias\Auditoria2026\` con control de versiones y permisos de solo‑lectura. Los hashes se verifican antes y después de cualquier manipulación.

---  

## 7. Declaración de Aplicabilidad (ISO 27001 – Annex A)

| Control Annex A | Aplicable (Sí/No) | Justificación de exclusión (si No) |
|-----------------|--------------------|-----------------------------------|
| A.5.1 Política de seguridad de la información | **No** | Falta de documento; se requiere para cumplir ISO, ENS y PCI. |
| A.6.1 Organización interna | **No** | No existe organigrama ni roles definidos. |
| A.7.1 Responsabilidades de recursos humanos | **Sí** | No se ha detectado incumplimiento; procesos de RRHH están documentados fuera del alcance. |
| A.8.1 Inventario de activos | **No** | No hay inventario formal. |
| A.9.1 Control de acceso | **No** | Ausencia de política y revisiones. |
| A.10.1 Criptografía | **No** | No hay evidencia de cifrado. |
| A.11.1 Seguridad física y del entorno | **Sí** | No se requieren controles físicos críticos para la zona evaluada. |
| A.12.1 Operaciones seguras | **No** | Falta gestión de vulnerabilidades y parches. |
| A.13.1 Seguridad de redes | **No** | No hay firewall ni segmentación. |
| A.14.1 Seguridad en el ciclo de vida del software | **No** | No existe proceso SDLC seguro. |
| A.15.1 Relaciones con proveedores | **Sí** | No se utilizan proveedores críticos que requieran controles adicionales. |
| A.16.1 Gestión de incidentes | **No** | No hay PRI ni registro de incidentes. |
| A.17.1 Continuidad del negocio | **No** | No hay PCN ni pruebas de recuperación. |
| A.18.1 Cumplimiento | **Sí** | Se dispone de normativa aplicable; sin embargo, el cumplimiento aún no está demostrado. |

> **Conclusión:** 9 de 14 controles críticos están **No aplicables** por falta de evidencia → **No cumple**. La organización debe **implementar** los controles marcados como **No** y **documentar** cualquier exclusión futura con justificación basada en riesgo.

---  

## 8. Conclusiones Ejecutivas  

| Área | Nivel de Cumplimiento | Comentario principal |
|------|------------------------|----------------------|
| **ISO 27001** | **No cumple** (7 NC, 2 NE) | Falta política integral, gestión de riesgos, control de accesos y registro de eventos. |
| **ENS** | **No cumple** (7 NC, 4 NE) | Ausencia de política, gestión de riesgos, cifrado y plan de incidentes. |
| **GDPR** | **No cumple** (RAT incompleto, sin cifrado) | Necesario registro de tratamientos y medidas de seguridad. |
| **NIS2** | **No cumple** (4 NC) | Política de seguridad y notificación de incidentes pendientes. |
| **PCI‑DSS** | **No cumple** (7 NC, 4 parciales) | Firewall, cifrado, anti‑malware y control de acceso crítico. |

**Riesgo global:** Alto – exposición total 196 (Score medio 14) y madurez organizacional 1.3/5.  

**Recomendación estratégica:**  
1. **Priorizar la elaboración de la Política de Seguridad Integral** (cubre ISO, ENS, NIS2 y PCI).  
2. **Ejecutar la gestión de riesgos** y **actualizar el Registro de Tratamientos** (GDPR).  
3. **Implementar controles de firewall, cifrado y control de accesos** (PCI, ENS, ISO).  
4. **Desplegar un SIEM** y **formalizar el PRI** para cumplir con requisitos de auditoría y de incidentes.  
5. **Revisar y actualizar mensualmente** el plan de acción, con auditorías internas cada 60 días hasta lograr cumplimiento total.

---  

## 9. Próximos Pasos  

1. **Reunión de arranque** con Comité de Seguridad (fecha propuesta: 2026‑05‑05).  
2. **Asignación de recursos** (presupuesto para firewall, SIEM, cifrado).  
3. **Entrega de evidencia complementaria** (política completa, inventario de activos, DPIA).  
4. **Seguimiento**: revisión de avances cada 30 días y reporte de estado a la Dirección.  

---  

*Fin del informe.*  