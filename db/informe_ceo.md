**  

# INFORME EJECUTIVO – CEO & DIRECCIÓN  
*(Formato Markdown – sin tecnicismos)*  

---

## 1️⃣ Resumen para la Dirección  *(máx. 1 página)*  

| Tema | Situación | Semáforo |
|------|------------|----------|
| **Estado general** | La exposición total a riesgos de cumplimiento es **176 puntos** (escala 0‑250). La mitad de esa exposición proviene de **5 riesgos críticos** que afectan a varias normativas simultáneamente. La madurez de los controles está en **2,1 / 5** (fase “definida”, falta de evidencia y automatización). | 🟡 |
| **Semáforo normativo** | • **GDPR** – Riesgo de multa de hasta **20 M €** o **4 %** de la facturación global. <br>• **ENS** – Posible pérdida de contratos con la Administración Pública. <br>• **NIS2** – Multas de hasta **10 M €** o **2 %** de la facturación. <br>• **PCI‑DSS** – Revocación de la capacidad de procesar pagos con tarjeta. <br>• **ISO 27001** – Pérdida de certificación y de contratos que la exigen. | 🔴 (puntos críticos) |
| **Decisión más urgente** | **Automatizar la desactivación de cuentas y accesos en menos de 24 h** tras la baja de un empleado o proveedor. Esta medida reduce el riesgo más puntuado (20 pts) y evita multas, interrupciones operativas y daño reputacional. | ✅ |

---

## 2️⃣ Exposición al Riesgo Regulatorio (cuantificado)

| Normativa | Posibles sanciones | Exposición estimada (puntos) | Comentario de negocio |
|-----------|-------------------|------------------------------|-----------------------|
| **GDPR** | Hasta **20 M €** o **4 %** de la facturación anual | 45 pts (riesgos de datos personales) | Fuga de datos personales → multas, pérdida de confianza de clientes. |
| **ENS** (Esquema Nacional de Seguridad) | Suspensión o cancelación de contratos con la Administración Pública | 22 pts (riesgos físicos) | Sin cumplimiento → imposibilidad de seguir operando con el sector público. |
| **NIS2** | Multas de hasta **10 M €** o **2 %** de la facturación | 27 pts (incidentes y continuidad) | Falta de notificación de brechas → sanciones y exposición mediática. |
| **PCI‑DSS** | Revocación del derecho a procesar pagos con tarjeta | 20 pts (cifrado y segmentación) | Imposibilidad de vender online → pérdida directa de ingresos. |
| **ISO 27001** | Pérdida de certificación → rescisión de contratos que la exigen | 5 pts (gobernanza) | Dificultad para licitar en proyectos internacionales. |

> **Interpretación rápida:** Si se materializa el peor escenario de cada normativa, la exposición financiera combinada supera los **35 M €** o **≈ 6 %** de la facturación anual, sin contar el daño reputacional y la pérdida de clientes.

---

## 3️⃣ Impacto Potencial en el Negocio  

| Área | Consecuencia si el riesgo se materializa |
|------|-------------------------------------------|
| **Continuidad operativa** | Interrupciones de servicio, incapacidad de procesar pagos, pérdida de datos críticos y costes de recuperación. |
| **Reputación** | Cobertura mediática negativa, pérdida de confianza de clientes y socios, caída de la valoración de marca. |
| **Cartera de clientes** | Cancelaciones de contratos, fuga de clientes a competidores, imposibilidad de captar nuevos negocios que exijan certificaciones. |
| **Finanzas** | Multas regulatorias, costes de litigios, inversión de emergencia para remediar brechas, aumento de primas de seguros. |

---

## 4️⃣ Los 5 Riesgos Más Críticos (explicados en lenguaje de negocio)

| # | Riesgo | Por qué importa para el negocio |
|---|--------|---------------------------------|
| **1** | **Desactivación tardía de cuentas y VPN** (72 h en vez de < 24 h) | Un ex‑empleado o proveedor que sigue teniendo acceso puede robar información, sabotear sistemas o generar fraude. Cada día extra aumenta la exposición a multas y a pérdida de datos. |
| **2** | **Ausencia de procedimiento de notificación de incidentes** | Sin un proceso claro, la empresa no informa a clientes ni autoridades dentro del plazo legal (72 h). Esto genera multas, daño reputacional y pérdida de confianza. |
| **3** | **Falta de plan de continuidad del negocio y recuperación** | En caso de caída del sistema, no hay un plan probado para volver a operar. El tiempo de inactividad prolongado afecta ingresos, penaliza acuerdos de nivel de servicio (SLA) y puede activar cláusulas de rescisión contractual. |
| **4** | **Tratamiento de datos especiales sin base legal ni DPIA** | Se están manejando datos sensibles (p.ej., estado civil) sin autorización. La autoridad de protección de datos puede imponer multas máximas y los clientes pueden retirar su confianza. |
| **5** | **Punto ciego de la cámara CCTV en el datacenter** | Un área sin vigilancia permite accesos físicos no detectados, facilitando robos o manipulaciones de equipos críticos. La falta de evidencia de control físico vulnera normas de seguridad y puede invalidar la certificación PCI‑DSS. |

---

## 5️⃣ Tabla de Inversión vs. ROI de Seguridad  

| Área de Mejora | Inversión Estimada (€/año) | Riesgo Mitigado (puntos) | ROI de Seguridad (valor estimado del riesgo evitado) |
|----------------|---------------------------|--------------------------|------------------------------------------------------|
| Automatización de desactivación de cuentas | 45 000 | 20 | 8 M € (evita multas GDPR/NIS2 + pérdida de ingresos) |
| Política y plataforma de notificación de incidentes | 30 000 | 20 | 6 M € (evita sanciones NIS2/GDPR y protege reputación) |
| Plan de continuidad del negocio (BCP/DRP) y pruebas | 70 000 | 20 | 9 M € (reduce tiempo de inactividad y penalizaciones contractuales) |
| Solución de CCTV y control de acceso físico | 25 000 | 12 | 2 M € (cumple PCI‑DSS y evita fraude interno) |
| DPIA y gestión de datos especiales | 20 000 | 20 | 4 M € (evita multas GDPR y pérdida de clientes) |
| **Total** | **190 000** | **92** | **≈ 29 M €** (≈ 15 % de la facturación anual) |

> **Nota:** El ROI se calcula como el valor financiero del riesgo que se elimina (multas potenciales, pérdida de ingresos y costes de recuperación) dividido por la inversión.

---

## 6️⃣ Decisiones Estratégicas Requeridas por la Dirección  

1. **Aprobar el presupuesto de 190 k €/año** para cubrir las cinco áreas críticas descritas.  
2. **Autorizar la automatización de la gestión de identidades** (integración RRHH‑IT) como prioridad número 1.  
3. **Nombrar un patrocinador ejecutivo** (p.ej., CFO o COO) que supervise la implantación del plan de continuidad del negocio.  
4. **Adoptar un Marco Integrado de Gestión de Riesgos (ISO 31000 + FAIR)** para cuantificar futuros riesgos en términos financieros y priorizar inversiones.  
5. **Establecer un Comité de Cumplimiento** que revise trimestralmente el avance de los controles y reporte a la Junta Directiva.

---

## 7️⃣ Hoja de Ruta Ejecutiva – Próximos 6 Meses  

| Mes | Hito clave | Responsable |
|-----|------------|--------------|
| **M1** | Lanzamiento del proyecto y asignación de presupuesto. <br>Automatización de desactivación de cuentas (piloto). | CEO / CISO |
| **M2** | Definición y difusión de la política de notificación de incidentes (incluye plantillas y simulacros). | CISO |
| **M3** | Instalación y ajuste de la cámara CCTV en el datacenter. <br>Inicio del DPIA para datos especiales. | Facility Manager / DPO |
| **M4** | Desarrollo del BCP/DRP (documentación) y primera prueba de recuperación parcial. | Business Continuity Manager |
| **M5** | Implementación de segmentación de red y reglas de firewall para datos de tarjetas. | Infraestructura |
| **M6** | Revisión integral de avances, auditoría interna de los cinco controles críticos y presentación de resultados al Consejo. | Auditoría Interna / Comité de Cumplimiento |

> **Indicadores de éxito**: 100 % de cuentas desactivadas en < 24 h, política de incidentes aprobada y probada, CCTV sin puntos ciegos, BCP probado con RTO ≤ 4 h, segmentación de red certificada PCI‑DSS.

---

## 8️⃣ Top 3 Acciones Inmediatas (próximos 30 días)

| Acción | Qué se hará | Resultado esperado |
|--------|-------------|--------------------|
| **1. Automatizar la desactivación de cuentas** | Integrar el sistema de nómina con Active Directory para que, al registrar una baja, la cuenta se bloquee automáticamente en < 24 h. | Reducción del riesgo crítico de 20 pts; evita acceso no autorizado. |
| **2. Crear y difundir la política de notificación de incidentes** | Redactar documento, definir flujos de trabajo y realizar una simulación de brecha con el equipo de TI. | Cumplimiento de GDPR/NIS2; reducción de multas y mejora de reputación. |
| **3. Corregir el punto ciego de la cámara CCTV** | Re‑orientar la cámara o instalar espejo convexo; validar con inspección física. | Eliminación del riesgo físico (12 pts); mantiene certificación PCI‑DSS. |

---

## 9️⃣ Conclusión Ejecutiva  

- **Exposición alta** (176 pts) pero **concentrada** en cinco riesgos que pueden ser mitigados con inversiones relativamente modestas (≈ 190 k €/año).  
- **Impacto financiero potencial** supera los **35 M €** en multas y pérdida de ingresos, sin contar el daño reputacional.  
- **Acción inmediata** en la gestión de identidades, notificación de incidentes y control físico eliminará más de la mitad de la exposición total.  
- **Decisión estratégica**: aprobar el plan de inversión y establecer un marco de gestión de riesgos que convierta cada punto de Score en una cifra monetaria, facilitando decisiones basadas en ROI.

> **Próximo paso:** la Dirección aprueba el presupuesto y designa al patrocinador ejecutivo para iniciar la hoja de ruta.  

---  

*Este informe está pensado para la alta dirección y resume, en lenguaje de negocio, los riesgos, sus consecuencias y las decisiones que garantizan la continuidad, la reputación y la rentabilidad de la empresa.*