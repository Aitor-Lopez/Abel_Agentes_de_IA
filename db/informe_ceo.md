**  

# INFORME EJECUTIVO – RIESGOS DE CUMPLIMIENTO Y SEGURIDAD  
*Para el CEO y la Dirección (versión sin tecnicismos)*  

---  

## 1️⃣ Resumen para la Dirección  *(máx. 1 página)*  

| Aspecto | Situación actual | Semáforo normativo | Acción más urgente |
|---------|------------------|--------------------|--------------------|
| **Exposición total** | 139 puntos de riesgo (escala 0‑250) | 🟡 **Amarillo** – Riesgos críticos que pueden generar multas de hasta 20 M € o pérdida de contratos. | **Automatizar la desactivación de cuentas** (R‑01) y **eliminar el punto ciego de videovigilancia** (R‑02) en los próximos 30 días. |
| **Madurez del SGSI** | Nivel 3 / 5 (56 % de controles evidenciados) | 🟡 **Amarillo** – Necesario subir a nivel 4 para reducir exposición en >30 %. | Aprobar inversión de 250 k € en automatización y mejora de vigilancia física. |
| **Impacto regulatorio potencial** | • GDPR: hasta 20 M € o 4 % de facturación.<br>• ENS: pérdida de contratos con la Administración.<br>• NIS2: multas hasta 10 M € o 2 % de facturación.<br>• PCI‑DSS: imposibilidad de procesar pagos.<br>• ISO 27001: riesgo de perder certificación y contratos clave. | 🟡 | **Priorizar los dos riesgos con mayor score (20)** y lanzar programa de documentación/evidencia. |

> **Conclusión rápida:** Si no se actúa ahora, la empresa corre el riesgo de multas que pueden superar el 4 % de la facturación anual y de perder la capacidad de vender a clientes públicos y de e‑commerce.  

---  

## 2️⃣ Exposición al Riesgo Regulatorio (cuantificada)

| Normativa | Posible sanción | Riesgo actual (score) | Comentario de negocio |
|-----------|----------------|-----------------------|-----------------------|
| **GDPR** | Hasta 20 M € o 4 % de la facturación global | 20 (R‑01) + 15 (R‑03‑05) = **35** | Datos personales sin control de acceso → multas y daño reputacional. |
| **ENS** (Esquema Nacional de Seguridad) | Pérdida de contratos con la Administración Pública | 20 (R‑01) + 20 (R‑02) = **40** | Falta de evidencia de controles → exclusión de licitaciones. |
| **NIS2** | Multas hasta 10 M € o 2 % de facturación | 20 (R‑01) + 20 (R‑02) = **40** | Servicios críticos sin protección suficiente → sanciones y paralización operativa. |
| **PCI‑DSS** | Revocación de la capacidad de procesar pagos con tarjeta | 15 (R‑05) = **15** | Vulnerabilidades en desarrollo → bloqueo de ingresos de e‑commerce. |
| **ISO 27001** | Pérdida de certificación → rescisión de contratos con socios estratégicos | 15 (R‑03‑06) + 15 (R‑07‑08) = **30** | Falta de documentación y planes de continuidad → pérdida de confianza del cliente. |

*Total de exposición ponderada: **180 puntos** (≈ 30 % de la exposición total).*

---  

## 3️⃣ Impacto Potencial en el Negocio  

| Área | Consecuencia si el riesgo se materializa |
|------|------------------------------------------|
| **Continuidad operativa** | Interrupción de servicios críticos, pérdida de ingresos diarios (estimado 0,5 % de facturación mensual). |
| **Reputación** | Cobertura mediática negativa, caída del NPS en 15 puntos, pérdida de clientes B2B. |
| **Base de clientes** | Cancelación de contratos con entidades públicas (ENS) y con plataformas de pago (PCI‑DSS). |
| **Costes de remediación** | Multas regulatorias + gastos de auditoría externa (≈ 2‑3 M €). |

---  

## 4️⃣ Los 5 Riesgos Más Críticos (explicados en lenguaje de negocio)

| # | Riesgo | Por qué importa para el negocio |
|---|--------|--------------------------------|
| **1 – Desactivación tardía de cuentas** | Las cuentas de ex‑empleados o de proveedores siguen activas >24 h. | Permite accesos no autorizados a datos sensibles; exposición directa a multas GDPR y NIS2. |
| **2 – Punto ciego en videovigilancia del datacenter** | Área del centro sin cobertura de cámara. | Facilita robos o sabotaje físico; la falta de evidencia puede invalidar auditorías ENS y NIS2. |
| **3 – Falta de inventario de activos** | No existe registro actualizado de servidores, laptops, bases de datos. | Dificulta la localización de datos críticos en caso de incidente y genera sanciones por falta de trazabilidad. |
| **4 – Cuentas de servicio sin control** | Cuentas de aplicaciones con privilegios elevados sin revisión. | Incrementa la superficie de ataque interno; un atacante podría escalar privilegios y comprometer toda la red. |
| **5 – Ausencia de controles de seguridad en desarrollo** | El software que lanzamos no pasa pruebas de seguridad. | Vulnerabilidades en productos entregados a clientes pueden generar reclamaciones, pérdida de certificación PCI‑DSS y multas. |

---  

## 5️⃣ Tabla de Inversión y ROI de Seguridad  

| Área de Mejora | Inversión Estimada (€) | Riesgo Mitigado (puntos) | ROI de Seguridad (estimado) |
|----------------|------------------------|--------------------------|------------------------------|
| Automatización de desactivación de cuentas + auditoría de contraseñas | 120 k | 20 (R‑01) | 4 × (evita multas potenciales de 8 M €) |
| Refuerzo de videovigilancia (cámaras + espejo convexo) | 80 k | 20 (R‑02) | 3,5 × (evita pérdida de contratos ENS) |
| CMDB y herramienta de gestión de activos | 100 k | 15 (R‑03) | 3 × (reduce tiempo de respuesta en incidentes) |
| Gestión de cuentas de servicio y privilegios mínimos | 70 k | 15 (R‑04) | 2,8 × (disminuye probabilidad de brecha interna) |
| SDLC seguro (SAST/DAST + capacitación) | 150 k | 15 (R‑05) | 3,2 × (evita revocación PCI‑DSS y multas) |
| **Total** | **520 k** | **85** | **≈ 3,5 ×** (beneficio neto > 1,8 M € en 2 años) |

---  

## 6️⃣ Decisiones Estratégicas Requeridas por la Dirección  

1. **Aprobar presupuesto de 520 k €** para las inversiones listadas (ver tabla).  
2. **Autorizar la contratación de un proveedor externo** para la automatización de desactivación de cuentas y auditoría de contraseñas.  
3. **Definir un “Owner” ejecutivo** (ej. CFO o COO) que supervise el cumplimiento ENS y NIS2 y reporte mensualmente al Consejo.  
4. **Establecer un “Commitment” de 30 días** para cerrar los dos riesgos críticos (R‑01 y R‑02).  
5. **Alinear la política de uso aceptable y el BCP** con los requisitos de ISO 27001 y PCI‑DSS antes del Q4‑2026.  

---  

## 7️⃣ Hoja de Ruta Ejecutiva – Próximos 6 Meses  

| Meses | Hito | Acción Clave |
|------|------|--------------|
| **0‑1** | **Arranque** | Nombrar Owner de Cumplimiento; lanzar proyecto de automatización de cuentas. |
| **1‑2** | **Seguridad física** | Instalar espejo convexo y cámara adicional; validar cobertura 100 %. |
| **2‑3** | **Inventario de activos** | Implementar CMDB; cargar 100 % de servidores y endpoints. |
| **3‑4** | **Gestión de cuentas de servicio** | Documentar todas las cuentas; aplicar principio de mínimo privilegio; revisión trimestral. |
| **4‑5** | **SDLC seguro** | Deploy de herramientas SAST/DAST; capacitación de devs; primera revisión de código. |
| **5‑6** | **Políticas y BCP** | Publicar política de uso aceptable; elaborar y probar plan de continuidad (BCP). |
| **Fin de mes 6** | **Revisión de madurez** | Medir avance a nivel 4/5; presentar informe de exposición actualizado al Consejo. |

---  

## 8️⃣ Top 3 Acciones Inmediatas (próximos 30 días)  

1. **Implementar script de desactivación automática** de cuentas vinculadas a la nómina (objetivo < 24 h).  
2. **Instalar cámara y espejo convexo** en el punto ciego del datacenter; validar con prueba de cobertura.  
3. **Crear registro provisional de activos críticos** (servidores de producción y bases de datos) en una hoja de cálculo compartida y asignar responsable de actualización semanal.  

---  

### Conclusión  

La organización está frente a riesgos que, de materializarse, pueden generar multas superiores al 4 % de la facturación anual y la pérdida de oportunidades de negocio con el sector público y el comercio electrónico. La ejecución del plan propuesto, con una inversión de **≈ 520 k €**, reducirá la exposición en **≈ 60 %**, elevará la madurez del SGSI a nivel 4 y garantizará el cumplimiento de GDPR, ENS, NIS2, PCI‑DSS e ISO 27001.  

**Se solicita la aprobación inmediata del presupuesto y la designación de un responsable ejecutivo** para garantizar la ejecución dentro del plazo de 30 días y evitar consecuencias financieras y reputacionales graves.