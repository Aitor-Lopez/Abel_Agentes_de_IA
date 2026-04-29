
const pptxgen = require("pptxgenjs");

const data = {"titulo": "Análisis de Riesgos de Ciberseguridad", "subtitulo": "Informe de Exposición y Riesgos Críticos", "fecha": "Abril 2026", "empresa": "AuditAI Multi-Agente", "resumen_ejecutivo": {"nivel_riesgo": "ALTO", "score_global": 35, "hallazgos_criticos": 7, "hallazgos_altos": 9, "hallazgos_medios": 3, "frase_impacto": "Exposición crítica que amenaza la continuidad del negocio y la confidencialidad de datos sensibles"}, "top_riesgos": [{"id": "R1", "titulo": "Desactivación tardía de cuentas/VPN", "descripcion": "Las cuentas de usuarios y accesos VPN permanecen activas hasta 72 h tras la baja, exponiendo la red a accesos no autorizados y potenciales exfiltraciones.", "impacto_economico": "Posible multa de 200 000 € y pérdida de confianza que puede afectar 0,5 % de facturación anual (~250 k €)", "probabilidad": "Alta", "criticidad": "Crítico", "normativas": ["ISO 27001", "ENS", "NIS2", "PCI-DSS"], "consecuencia": "Acceso no revocado permite intrusión y posible robo de datos críticos"}, {"id": "R2", "titulo": "Ausencia de procedimiento de notificación de incidentes", "descripcion": "No existe proceso documentado ni pruebas de notificación de brechas, incumpliendo plazos de 72 h exigidos por NIS2 y GDPR, lo que genera sanciones y daño reputacional.", "impacto_economico": "Multa GDPR hasta 10 M € o 2 % de facturación; estimado 1 % de facturación (~500 k €)", "probabilidad": "Alta", "criticidad": "Crítico", "normativas": ["NIS2", "GDPR", "ISO 27001", "PCI-DSS"], "consecuencia": "Incumplimiento de notificación genera multas y pérdida de clientes"}, {"id": "R3", "titulo": "Falta de evidencia de continuidad del negocio y DRP", "descripcion": "No se dispone de planes de continuidad ni pruebas de recuperación, exponiendo a interrupciones prolongadas que pueden paralizar operaciones críticas.", "impacto_economico": "Parada de negocio 48 h → pérdida estimada 1 M €", "probabilidad": "Alta", "criticidad": "Crítico", "normativas": ["NIS2", "ISO 27001", "PCI-DSS"], "consecuencia": "Interrupción prolongada afecta ingresos y reputación"}, {"id": "R4", "titulo": "Tratamiento de datos especiales sin base legal ni DPIA", "descripcion": "Se procesan datos de estado civil sin consentimiento ni evaluación de impacto, vulnerando GDPR Art. 9 y exponiendo a sanciones.", "impacto_economico": "Multa GDPR 4 % de facturación (~2 M €)", "probabilidad": "Alta", "criticidad": "Crítico", "normativas": ["GDPR", "ISO 27001", "NIS2"], "consecuencia": "Sanción regulatoria y demandas de titulares"}, {"id": "R5", "titulo": "Cifrado de datos de tarjetas no evidenciado", "descripcion": "Los datos de tarjetas de pago no están cifrados ni en reposo ni en tránsito, violando PCI‑DSS y GDPR, riesgo de fraude masivo.", "impacto_economico": "Multa PCI‑DSS hasta 500 k USD y costes de fraude estimados 1,5 M €", "probabilidad": "Media", "criticidad": "Alto", "normativas": ["PCI-DSS", "GDPR"], "consecuencia": "Robo de datos de tarjetas genera multas y pérdida de confianza"}], "exposicion_normativa": [{"normativa": "ISO 27001", "nivel": "CRÍTICO", "multa_max": "N/A", "incumplimientos": 84, "descripcion": "Solo 9 % de los controles están evidenciados; exposición a fallos en gestión de incidentes, continuidad y terceros."}, {"normativa": "ENS", "nivel": "ALTO", "multa_max": "300 000 €", "incumplimientos": 2, "descripcion": "Dos controles críticos sin evidencia: desactivación de cuentas y punto ciego CCTV, riesgo de acceso físico y lógico."}, {"normativa": "GDPR", "nivel": "ALTO", "multa_max": "20 M € o 4 % de facturación", "incumplimientos": 5, "descripcion": "Falta DPIA para datos especiales, notificación de brechas y gestión de derechos ARCO, exponiendo a sanciones severas."}, {"normativa": "NIS2", "nivel": "ALTO", "multa_max": "10 M € o 2 % de facturación", "incumplimientos": 5, "descripcion": "Ausencia de proceso de notificación, gestión de cadena suministro y continuidad, vulnerando requisitos críticos."}, {"normativa": "PCI-DSS", "nivel": "ALTO", "multa_max": "500 000 USD por incidente", "incumplimientos": 5, "descripcion": "Cifrado de datos de tarjetas, segmentación y pruebas de penetración no evidenciados, riesgo de pérdida de certificación."}], "metricas_clave": [{"metrica": "Exposición total (Σ Score)", "valor": "176", "contexto": "Indicador acumulado de riesgo; >150 señala exposición alta."}, {"metrica": "Madurez media", "valor": "2.1", "contexto": "Nivel entre 'Definida' y 'Gestionada'; requiere mejoras urgentes."}, {"metrica": "Riesgos críticos (Criticidad 5)", "valor": "7", "contexto": "Casi la mitad de los hallazgos son críticos, prioridad máxima."}, {"metrica": "Porcentaje de controles evidenciados (ISO 27001)", "valor": "9%", "contexto": "Solo 9 % de los controles están documentados, muestra gran brecha de gobernanza."}], "plan_accion": [{"fase": "Inmediato (0-30 días)", "acciones": ["Implementar proceso automatizado de desactivación de cuentas vía AD", "Definir y publicar política de notificación de incidentes con plantilla", "Reorientar cámara CCTV para cubrir punto ciego"], "inversion": "30 000 € – 50 000 €", "riesgo_mitigado": "R01, R02, R03"}, {"fase": "Corto plazo (30-90 días)", "acciones": ["Desarrollar y validar BCP/DRP con pruebas de recuperación", "Realizar DPIA y obtener bases legales para datos especiales", "Implementar cifrado TLS 1.3 y cifrado de discos para datos de tarjetas"], "inversion": "80 000 € – 120 000 €", "riesgo_mitigado": "R04, R05, R11, R12"}, {"fase": "Medio plazo (90-180 días)", "acciones": ["Establecer programa de pruebas de penetración y escaneo trimestral", "Segregar red y aplicar firewall de nueva generación", "Implementar gestión de riesgos de terceros con cuestionario ISO 27005"], "inversion": "150 000 € – 200 000 €", "riesgo_mitigado": "R07, R09, R10"}], "llamada_accion": "Actúe ahora o arriesgue multas millonarias y la continuidad de su negocio."};

// ── Paleta: Midnight Executive con acento rojo peligro ──
const C = {
  bg:       "0D1117",
  bg2:      "161B22",
  bg3:      "21262D",
  red:      "FF4757",
  orange:   "FFA502",
  green:    "00E5A0",
  blue:     "5B9FFF",
  white:    "E8EAF0",
  gray:     "8892A4",
  darkgray: "4A5568",
  border:   "21262D",
};

const CRIT_COLOR = { "Crítico": C.red, "Alto": C.orange, "Medio": "FFD700", "Bajo": C.green };
const NIVEL_COLOR = { "CRÍTICO": C.red, "ALTO": C.orange, "MEDIO": "FFD700", "BAJO": C.green };

let pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.3" x 7.5"
pres.title = data.titulo;
pres.author = "AuditAI";

const W = 13.3, H = 7.5;

// ════════════════════════════════════════════════
// SLIDE 1 — PORTADA
// ════════════════════════════════════════════════
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  // Bloque rojo izquierdo
  s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:0.5, h:H, fill:{ color: C.red } });

  // Nivel de riesgo badge grande
  const nivel = data.resumen_ejecutivo.nivel_riesgo;
  const nivelColor = NIVEL_COLOR[nivel] || C.red;
  s.addShape(pres.shapes.RECTANGLE, { x:0.9, y:1.0, w:3.2, h:0.65,
    fill:{ color: nivelColor }, rectRadius:0.05 });
  s.addText("NIVEL DE RIESGO: " + nivel, { x:0.9, y:1.0, w:3.2, h:0.65,
    fontSize:14, bold:true, color:C.bg, align:"center", valign:"middle", margin:0 });

  // Título principal
  s.addText(data.titulo, { x:0.9, y:1.85, w:9, h:1.3,
    fontSize:44, bold:true, color:C.white, fontFace:"Arial Black" });
  s.addText(data.subtitulo, { x:0.9, y:3.1, w:9, h:0.6,
    fontSize:20, color:nivelColor, fontFace:"Arial" });

  // Frase impacto
  s.addShape(pres.shapes.RECTANGLE, { x:0.9, y:3.9, w:8.5, h:0.8,
    fill:{ color: C.bg2 } });
  s.addText("⚠  " + data.resumen_ejecutivo.frase_impacto, { x:0.9, y:3.9, w:8.5, h:0.8,
    fontSize:16, color:C.red, italic:true, align:"center", valign:"middle", margin:0 });

  // Métricas rápidas en fila
  const mets = [
    { label: "Hallazgos Críticos", val: String(data.resumen_ejecutivo.hallazgos_criticos), color: C.red },
    { label: "Hallazgos Altos",    val: String(data.resumen_ejecutivo.hallazgos_altos),    color: C.orange },
    { label: "Hallazgos Medios",   val: String(data.resumen_ejecutivo.hallazgos_medios),   color: "FFD700" },
    { label: "Score Global",       val: data.resumen_ejecutivo.score_global + "/100",      color: nivelColor },
  ];
  mets.forEach((m, i) => {
    const bx = 0.9 + i * 2.9;
    s.addShape(pres.shapes.RECTANGLE, { x:bx, y:4.9, w:2.6, h:1.3,
      fill:{ color:C.bg2 } });
    s.addShape(pres.shapes.RECTANGLE, { x:bx, y:4.9, w:2.6, h:0.07,
      fill:{ color:m.color } });
    s.addText(m.val, { x:bx, y:5.0, w:2.6, h:0.65,
      fontSize:32, bold:true, color:m.color, align:"center", valign:"middle", margin:0 });
    s.addText(m.label, { x:bx, y:5.7, w:2.6, h:0.4,
      fontSize:10, color:C.gray, align:"center", valign:"middle", margin:0 });
  });

  // Fecha y empresa
  s.addText(data.empresa + "  ·  " + data.fecha, { x:0.9, y:H-0.5, w:10, h:0.35,
    fontSize:10, color:C.darkgray });
}

// ════════════════════════════════════════════════
// SLIDE 2 — TOP 5 RIESGOS CRÍTICOS (tabla visual)
// ════════════════════════════════════════════════
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:W, h:0.8, fill:{ color:C.bg2 } });
  s.addText("TOP 5 RIESGOS CRÍTICOS", { x:0.5, y:0, w:W-1, h:0.8,
    fontSize:22, bold:true, color:C.white, valign:"middle", margin:0 });
  s.addText("Impacto directo sobre el negocio si no se actúa", { x:0.5, y:0, w:W-1, h:0.8,
    fontSize:12, color:C.gray, align:"right", valign:"middle", margin:0 });

  const risks = (data.top_riesgos || []).slice(0, 5);
  risks.forEach((r, i) => {
    const ry = 0.95 + i * 1.28;
    const color = CRIT_COLOR[r.criticidad] || C.orange;

    // Fondo fila
    s.addShape(pres.shapes.RECTANGLE, { x:0.3, y:ry, w:W-0.6, h:1.15,
      fill:{ color:C.bg2 } });
    // Borde izquierdo color criticidad
    s.addShape(pres.shapes.RECTANGLE, { x:0.3, y:ry, w:0.08, h:1.15,
      fill:{ color:color } });
    // Badge ID
    s.addShape(pres.shapes.RECTANGLE, { x:0.55, y:ry+0.25, w:0.5, h:0.5,
      fill:{ color:color } });
    s.addText(r.id, { x:0.55, y:ry+0.25, w:0.5, h:0.5,
      fontSize:12, bold:true, color:C.bg, align:"center", valign:"middle", margin:0 });
    // Título riesgo
    s.addText(r.titulo, { x:1.2, y:ry+0.08, w:5.5, h:0.4,
      fontSize:14, bold:true, color:C.white, margin:0 });
    // Descripción
    s.addText(r.descripcion, { x:1.2, y:ry+0.5, w:5.5, h:0.55,
      fontSize:10, color:C.gray, margin:0 });
    // Impacto económico
    s.addText("💰 " + r.impacto_economico, { x:6.9, y:ry+0.1, w:3.5, h:0.4,
      fontSize:11, bold:true, color:color, margin:0 });
    // Consecuencia
    s.addText("⚡ " + r.consecuencia, { x:6.9, y:ry+0.55, w:3.5, h:0.45,
      fontSize:10, color:C.gray, margin:0 });
    // Badge criticidad
    s.addShape(pres.shapes.RECTANGLE, { x:10.6, y:ry+0.3, w:1.5, h:0.4,
      fill:{ color:color } });
    s.addText(r.criticidad.toUpperCase(), { x:10.6, y:ry+0.3, w:1.5, h:0.4,
      fontSize:10, bold:true, color:C.bg, align:"center", valign:"middle", margin:0 });
    // Normativas
    const normsText = (r.normativas || []).join(" · ");
    s.addText(normsText, { x:10.55, y:ry+0.75, w:1.6, h:0.3,
      fontSize:8, color:C.darkgray, align:"center", margin:0 });
  });
}

// ════════════════════════════════════════════════
// SLIDE 3 — EXPOSICIÓN NORMATIVA
// ════════════════════════════════════════════════
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:W, h:0.8, fill:{ color:C.bg2 } });
  s.addText("EXPOSICIÓN NORMATIVA Y SANCIONES", { x:0.5, y:0, w:W-1, h:0.8,
    fontSize:22, bold:true, color:C.white, valign:"middle", margin:0 });

  const norms = (data.exposicion_normativa || []).slice(0, 5);
  norms.forEach((n, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const cx = 0.4 + col * 4.3;
    const cy = 1.0 + row * 2.8;
    const cw = 3.9, ch = 2.5;
    const color = NIVEL_COLOR[n.nivel] || C.orange;

    s.addShape(pres.shapes.RECTANGLE, { x:cx, y:cy, w:cw, h:ch, fill:{ color:C.bg2 } });
    s.addShape(pres.shapes.RECTANGLE, { x:cx, y:cy, w:cw, h:0.07, fill:{ color:color } });

    // Nombre normativa
    s.addText(n.normativa, { x:cx+0.15, y:cy+0.12, w:cw-0.6, h:0.45,
      fontSize:16, bold:true, color:C.white, margin:0 });
    // Badge nivel
    s.addShape(pres.shapes.RECTANGLE, { x:cx+cw-0.9, y:cy+0.12, w:0.75, h:0.35,
      fill:{ color:color } });
    s.addText(n.nivel, { x:cx+cw-0.9, y:cy+0.12, w:0.75, h:0.35,
      fontSize:8, bold:true, color:C.bg, align:"center", valign:"middle", margin:0 });
    // Multa
    s.addText("Multa máx: " + n.multa_max, { x:cx+0.15, y:cy+0.65, w:cw-0.3, h:0.35,
      fontSize:11, bold:true, color:color, margin:0 });
    // Incumplimientos
    s.addText(String(n.incumplimientos) + " incumplimientos detectados", { x:cx+0.15, y:cy+1.0, w:cw-0.3, h:0.3,
      fontSize:10, color:C.gray, margin:0 });
    // Descripción
    s.addText(n.descripcion, { x:cx+0.15, y:cy+1.35, w:cw-0.3, h:0.95,
      fontSize:9, color:C.gray, margin:0 });
  });
}

// ════════════════════════════════════════════════
// SLIDE 4 — MÉTRICAS CLAVE (big numbers)
// ════════════════════════════════════════════════
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:W, h:0.8, fill:{ color:C.bg2 } });
  s.addText("MÉTRICAS CLAVE DE EXPOSICIÓN", { x:0.5, y:0, w:W-1, h:0.8,
    fontSize:22, bold:true, color:C.white, valign:"middle", margin:0 });

  const metrics = (data.metricas_clave || []).slice(0, 4);
  const mColors = [C.red, C.orange, C.blue, C.green];
  metrics.forEach((m, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const mx = 0.5 + col * 6.4, my = 1.0 + row * 2.8;
    const mw = 6.0, mh = 2.5;
    s.addShape(pres.shapes.RECTANGLE, { x:mx, y:my, w:mw, h:mh, fill:{ color:C.bg2 } });
    s.addShape(pres.shapes.RECTANGLE, { x:mx, y:my, w:mw, h:0.07, fill:{ color:mColors[i] } });
    s.addText(m.valor, { x:mx, y:my+0.15, w:mw, h:1.2,
      fontSize:56, bold:true, color:mColors[i], align:"center", valign:"middle", margin:0 });
    s.addText(m.metrica, { x:mx+0.2, y:my+1.4, w:mw-0.4, h:0.45,
      fontSize:16, bold:true, color:C.white, align:"center", margin:0 });
    s.addText(m.contexto, { x:mx+0.2, y:my+1.88, w:mw-0.4, h:0.45,
      fontSize:11, color:C.gray, align:"center", margin:0 });
  });
}

// ════════════════════════════════════════════════
// SLIDE 5 — PLAN DE ACCIÓN
// ════════════════════════════════════════════════
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:W, h:0.8, fill:{ color:C.bg2 } });
  s.addText("PLAN DE ACCIÓN RECOMENDADO", { x:0.5, y:0, w:W-1, h:0.8,
    fontSize:22, bold:true, color:C.white, valign:"middle", margin:0 });

  const faseColors = [C.red, C.orange, C.blue];
  const fases = (data.plan_accion || []).slice(0, 3);
  fases.forEach((f, i) => {
    const fx = 0.4 + i * 4.3;
    const fy = 1.0, fw = 4.0, fh = 5.8;
    const color = faseColors[i];

    s.addShape(pres.shapes.RECTANGLE, { x:fx, y:fy, w:fw, h:fh, fill:{ color:C.bg2 } });
    s.addShape(pres.shapes.RECTANGLE, { x:fx, y:fy, w:fw, h:0.07, fill:{ color:color } });

    // Fase header
    s.addShape(pres.shapes.RECTANGLE, { x:fx+0.15, y:fy+0.15, w:fw-0.3, h:0.6,
      fill:{ color:color } });
    s.addText(f.fase, { x:fx+0.15, y:fy+0.15, w:fw-0.3, h:0.6,
      fontSize:12, bold:true, color:C.bg, align:"center", valign:"middle", margin:0 });

    // Acciones
    const acciones = (f.acciones || []).slice(0, 4);
    acciones.forEach((a, j) => {
      const ay = fy + 0.95 + j * 0.75;
      s.addShape(pres.shapes.OVAL, { x:fx+0.15, y:ay+0.1, w:0.3, h:0.3, fill:{ color:color } });
      s.addText(String(j+1), { x:fx+0.15, y:ay+0.1, w:0.3, h:0.3,
        fontSize:9, bold:true, color:C.bg, align:"center", valign:"middle", margin:0 });
      s.addText(a, { x:fx+0.55, y:ay, w:fw-0.75, h:0.6,
        fontSize:10, color:C.white, margin:0 });
    });

    // Inversión
    s.addShape(pres.shapes.RECTANGLE, { x:fx+0.15, y:fy+fh-1.05, w:fw-0.3, h:0.45,
      fill:{ color:"0D1117" } });
    s.addText("💶 " + f.inversion, { x:fx+0.15, y:fy+fh-1.05, w:fw-0.3, h:0.45,
      fontSize:11, bold:true, color:color, align:"center", valign:"middle", margin:0 });
    s.addText(f.riesgo_mitigado, { x:fx+0.15, y:fy+fh-0.55, w:fw-0.3, h:0.45,
      fontSize:9, color:C.gray, align:"center", margin:0 });
  });
}

// ════════════════════════════════════════════════
// SLIDE 6 — CIERRE / LLAMADA A LA ACCIÓN
// ════════════════════════════════════════════════
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  // Fondo rojo dramático mitad superior
  s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:W, h:H*0.45, fill:{ color:"1A0A0A" } });
  s.addShape(pres.shapes.RECTANGLE, { x:0, y:0, w:0.5, h:H, fill:{ color:C.red } });

  s.addText("⚠", { x:1, y:0.3, w:W-1.5, h:1.0,
    fontSize:48, align:"center", color:C.red });
  s.addText("EL RIESGO ES REAL. EL MOMENTO ES AHORA.", { x:1, y:1.2, w:W-1.5, h:1.0,
    fontSize:28, bold:true, color:C.white, align:"center", fontFace:"Arial Black", margin:0 });

  s.addText(data.llamada_accion, { x:1.5, y:2.4, w:W-2.5, h:0.9,
    fontSize:18, color:C.red, italic:true, align:"center", margin:0 });

  // Línea divisoria
  s.addShape(pres.shapes.LINE, { x:1, y:3.5, w:W-2, h:0,
    line:{ color:C.border, width:1 } });

  // Score final grande
  s.addText(String(data.resumen_ejecutivo.score_global), { x:1, y:3.7, w:3, h:2.0,
    fontSize:96, bold:true, color:C.red, align:"center", valign:"middle", margin:0 });
  s.addText("/100", { x:4.0, y:4.8, w:1.5, h:0.7,
    fontSize:24, color:C.gray, valign:"middle", margin:0 });
  s.addText("Score de Riesgo Global", { x:1, y:5.65, w:4, h:0.4,
    fontSize:11, color:C.gray, align:"center", margin:0 });

  // CTA texto
  s.addText("Próximos pasos:", { x:6, y:3.7, w:W-6.5, h:0.45,
    fontSize:14, bold:true, color:C.white, margin:0 });

  const ctas = [
    "Aprobar presupuesto de remediación urgente",
    "Designar responsable de seguimiento (CISO / DPO)",
    "Iniciar acciones críticas en los próximos 30 días",
    "Programar revisión de progreso en 60 días"
  ];
  ctas.forEach((c, i) => {
    s.addShape(pres.shapes.OVAL, { x:6.1, y:4.25+i*0.72, w:0.3, h:0.3, fill:{ color:C.red } });
    s.addText(c, { x:6.55, y:4.2+i*0.72, w:W-7.1, h:0.45,
      fontSize:12, color:C.white, margin:0 });
  });

  s.addText("Generado por AuditAI  ·  " + data.fecha, { x:1, y:H-0.45, w:W-2, h:0.35,
    fontSize:9, color:C.darkgray, align:"center", margin:0 });
}

pres.writeFile({ fileName: "/app/db/informe_riesgos.pptx" })
  .then(() => { console.log("OK:" + "/app/db/informe_riesgos.pptx"); })
  .catch(e => { console.error("ERROR:" + e); process.exit(1); });
