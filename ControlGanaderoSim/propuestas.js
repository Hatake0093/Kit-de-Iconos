// Cambios de icono que se quieren probar antes de tocar el proyecto.
// Clave: nombre del control en FrmMain (bbi..., bsi..., rp...). Valor: icono del kit (sin .svg) y motivo.
// Se ven con el modo "Kit + propuestas" de index.html. Editar a mano y recargar la página.
// { texto: "..." } propone además otro texto para el botón (solo se ve en ese modo). Una entrada
// con solo texto no cambia el icono.
// { falta: "..." } marca un icono que todavía no existe: se ve como hueco punteado hasta que
// se diseñe y se cambie por { icono: "nombre" }.
// Meta: ningún control con icono embebido en FrmMain.resx (todos pasan a My.Resources del kit).
const CARPETA = { icono: "carpeta-abierta", motivo: "Misma carpeta abierta de DevExpress que se usaba, llevada al kit con el ámbar de la paleta (trasera #F6C272, frente #F3AD43). Aplica igual a los cinco «Catálogos»." };

window.PROPUESTAS = {
  // ---------- Pestañas ----------
  rpCrianza:   { icono: "crianza",           motivo: "La hélice de ADN se lee como genética; el kit tiene madre y cría." },
  rpLotes:     { icono: "corral-perspectiva", motivo: "La cerca a tamaño de pestaña se lee como «#»; además, dentro de FEEDLOT todo usa corral-perspectiva." },
  rpReportes:  { icono: "GraficaTendencia",  motivo: "grafico-lineas-ambar es de trazo fino y se ve más ligero que las demás pestañas." },

  // ---------- PROCESOS (auditoría 1) ----------
  bsiC_Procesos:       CARPETA,
  bbiCompradores:      { icono: "usuario-reloj",    motivo: "Hoy usa usuarios, que se propone para Usuarios en AJUSTES; la insignia morada de reloj es programar." },
  bbiDueños:           { icono: "usuario-estrella", motivo: "Grupo de personas gris de DevExpress, embebido; la estrella ámbar marca al propietario." },
  bbiTransportistas:   { icono: "camion-usuario",  motivo: "PNG de autobús escolar ajeno al kit; el transportista es un camión con persona." },
  bbiCompradoresVenta: { icono: "usuario-dinero",  motivo: "Era la misma silueta que Programadores; la insignia $ distingue al comprador." },
  bbiCategoriasVenta:  { icono: "etiqueta-dinero", texto: "Categorías de Venta", motivo: "El billete se lee como dinero, no como categoría; la etiqueta clasifica." },
  // bbiCompras se queda con documento-vaca: el rediseño puso la vaca dentro del documento y ya se lee a 16 px.
  // Recepción y Remisiones: las dos son remisiones; misma base camión, cambia la dirección.
  bbiListaRecepciones: { icono: "camion-descarga", texto: "Remisiones de Entrada", motivo: "Son las remisiones de entrada: el camión que descarga ganado. Antes usaba vaca-carrito, que se confundía con Venta de Ordinarios." },
  bbiRemisiones:       { icono: "camion-flecha",   texto: "Remisiones de Salida",  motivo: "Traslados entre fincas, salidas a matadero, ventas y ajustes: el camión que sale. Hace pareja con Remisiones de Entrada." },

  // ---------- Tildes (solo texto; el icono no cambia) ----------
  bbiFormacionCorrales:   { texto: "Formación de Corrales" },
  bbiHistoricoImplantes:  { texto: "Histórico de Implantes" },
  bbiEvaluacionImplantes: { texto: "Evaluación de Implantes" },
  bbiEnfermeria:          { texto: "Enfermería" },
  bbiEvaluacionDeteccion: { texto: "Evaluación de Detección" },

  // ---------- RESES ----------
  BarSubItem1:      CARPETA,
  bbiZonas:         { icono: "mapa-pin",    motivo: "PNG ajeno al kit; una zona es un lugar en el mapa." },
  bbiBuscadorReses: { icono: "vaca-lupa",   motivo: "Lupa gris genérica de DevExpress; vaca-lupa sigue la familia de la pestaña." },
  bbiResesVenta:    { icono: "vaca-salida", motivo: "El billete no dice «reses» y ya se usa en Categorías de Venta; la res vendida es una salida." },

  // ---------- FEEDLOT ----------
  BarSubItem2:        CARPETA,
  btnCierreFormacion: { icono: "corral-perspectiva-check", texto: "Cierres de Formación", motivo: "Reloj rojo de DevExpress; cerrar la formación es confirmar el corral." },
  btnProtocolosInicio: { icono: "jeringa-flecha", motivo: "Calendario de DevExpress; el protocolo de inicio es el tratamiento de entrada (flecha) al feedlot." },
  btnAreasTrabajo:    { icono: "mapa", texto: "Áreas de Trabajo", motivo: "Ventana azul de DevExpress; un área es un lugar del mapa (Zonas usa mapa-pin)." },
  bbiImplantes:       { icono: "implante", motivo: "Cartucho morado con tres cavidades claras. En el mismo menú, Implantadores se reconoce por la silueta del aplicador." },
  bbiImplantadores:   { icono: "implantador", motivo: "PNG ajeno al kit; la familia de implantes ya usa implantador." },
  // BarButtonItem1 «Resumen»: reservado para un dashboard de Feedlot (aún sin ItemClick en main).
  // Se queda con GraficaMapaArbol, que ya es del kit y se lee como tablero de mosaicos; no se toca hasta que exista el dashboard.

  // ---------- P. ALIMENTOS ----------
  bsiC_PlantaAlimentos: CARPETA,
  bbiAlimentos:   { icono: "saco-alimento", motivo: "Letra «A» en un cuadro de DevExpress; no dice alimento." },
  bbiDietas:      { icono: "saco-lista",    motivo: "Hojas apiladas de DevExpress; la lista de dietas es una lista sobre el saco." },
  bbiListaRutasDieta: { icono: "mapa-flecha", motivo: "PNG ajeno al kit; una ruta es un recorrido en el mapa." },
  bbiListaEquipos:    { icono: "equipo", motivo: "El cargador frontal identifica la maquinaria del catálogo. La señal roja queda reservada para Paro de Equipos." },
  bbiCorralesAux:     { icono: "corral-frontal", motivo: "Embebido de DevExpress; la vista frontal lo separa de los corrales de engorda (corral-perspectiva)." },
  bbiPorcentajes:     { icono: "porcentaje", motivo: "PNG ajeno al kit; el kit tiene porcentaje." },
  bbiOperadores:  { icono: "usuario",       motivo: "Silueta de DevExpress; el kit tiene usuario." },
  bbiPlanDietas:  { icono: "calendario",    motivo: "Cuadrícula azul de DevExpress; un plan es un calendario." },
  bbiGraficasGerencial: { icono: "GraficaTendencia", texto: "Gráficas Gerenciales", motivo: "Línea punteada de DevExpress; es la cuarta gráfica de línea con estilo distinto en el sistema." },

  // ---------- SANIDAD ----------
  bsiC_Sanidad: CARPETA,
  bbiProductos: { icono: "jeringa",          motivo: "Caja de DevExpress; los productos de sanidad son medicamentos." },
  bbiProtocolos:          { icono: "jeringa-check",   motivo: "Lista con casillas de DevExpress; el protocolo es el tratamiento aprobado." },
  bbiCausasSanidad:       { icono: "cruz-lupa", texto: "Causas de Detección", motivo: "La cruz identifica Sanidad y la lupa representa la detección de un problema de salud en la res." },
  bbiCausaOrdinarioVenta: { icono: "vaca-dinero", motivo: "Comparte el icono de Venta de Ordinarios en Procesos. Aquí se clasifican los motivos de venta de una res en riesgo de morir." },
  bbiCausasMuerte:        { icono: "lapida",          motivo: "Calavera de DevExpress que competía con vaca-calavera de Mortalidad de Reses." },
  bbiTraslado:  { icono: "vaca-intercambio", motivo: "Jeringa con reloj se lee como «vacuna programada», no como mover reses." },

  // ---------- CRIANZA ----------
  BarSubItem3:      { icono: "carpeta-abierta", motivo: "Mismo caso que los demás «Catálogos». Además, en main este menú no tiene opciones." },
  bbiNacimientos:   { icono: "ternero-mas", motivo: "vaca-mas no distingue cría de adulto; el kit tiene ternero." },
  bbiAltasDestete:  { icono: "ternero-reloj-registro", motivo: "documento-vaca se queda para Compras de Ganado; el destete es de la cría." },

  // ---------- REPORTES ----------
  bbiComprasProgramadores: { icono: "barras-dinero",   motivo: "PNG de DevExpress (carrito con estrella) que se ve borroso al escalar; la familia carrito se eliminó del kit." },
  bbiDinamicoCompras:      { icono: "tabla-dinero", texto: "Dinámico de Compras",    motivo: "Tabla dinámica de DevExpress con check verde, fuera del kit." },
  bbiReciboPagos:          { icono: "moneda-check",    motivo: "Signo $ verde suelto de DevExpress; moneda-check = pago hecho." },
  bbiResumenCorrales:      { icono: "corral-perspectiva-reporte", texto: "Resumen de Corrales", motivo: "Lista con lupa de DevExpress; el kit tiene el corral con insignia de reporte." },
  bbiImproductivos:        { icono: "vaca-reporte",    motivo: "Cuadrícula gris con X de DevExpress; casi igual a Formatos BA y Centro de Reportes." },
  bbiReporteRechazos:      { icono: "vaca-x",          motivo: "Gráfica con X roja de DevExpress; el rechazo es una res cancelada." },
  bbiCentroReportes:       { icono: "Archivero",       motivo: "Cuadrícula de colores de DevExpress, casi igual a Formatos BA. En la rama del buscador este botón desaparece." },
  bbiFormatosBA:           { icono: "Plantilla", texto: "Formatos de Bienestar Animal", motivo: "BA = Bienestar Animal: imprime los formatos del Manual de Procedimientos Operativos de Bienestar Animal (Reportes/Bienestar/FrmFormatosBA). Cuadrícula de DevExpress casi igual a Centro de Reportes; un formato es una plantilla." },
  bbiReporteGerencial:     { icono: "GraficaBarrasAscendentes", motivo: "PNG de maletín; el reporte gerencial resume resultados." },

  // ---------- AJUSTES ----------
  bbiRoles:             { icono: "escudo-check-verde", motivo: "PNG de persona con máscara; un rol es un permiso." },
  bbiUsers:             { icono: "usuarios",           motivo: "PNG de DevExpress; el kit tiene usuarios." },
  bbiConfigurarOffline: { icono: "BaseDatos-flecha", texto: "Configurar modo sin conexión",   motivo: "Base de datos amarilla con engranaje de DevExpress; el kit tiene la familia BaseDatos." },
  rgbiSkins:            { falta: "temas: paleta de pintor plana con 4 manchas de la paleta del kit (azul, verde, ámbar, rosa) y contorno marino.", motivo: "PNG de paleta con pincel de DevExpress. Es una galería de skins (RibbonGalleryBarItem): en la app real se ven las miniaturas de los temas y este icono solo aparece cuando el grupo se colapsa por falta de ancho." },
  iExit:                { icono: "salida", motivo: "Usa una imagen de la lista de imágenes del ribbon (ImageIndex 6), fuera del kit." },
};
