// Generado por generar_sim.py a partir de FrmMain.designer.vb. No editar a mano.
window.SIM = {
 "rama": "main",
 "version": "156e39a del 2026-11-03 07:38:19 -0600",
 "paginas": [
  {
   "id": "rpProcesos",
   "texto": "PROCESOS",
   "icono": {
    "tipo": "recurso",
    "nombre": "ListaTareas",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/ListaTareas.svg",
    "proyecto": "iconos_proyecto/ListaTareas.svg",
    "cambia": false
   },
   "grupos": [
    {
     "id": "rpgC_Procesos",
     "texto": "Catálogos",
     "visible": true,
     "items": [
      {
       "id": "bsiC_Procesos",
       "tipo": "BarSubItem",
       "texto": "Catálogos de Procesos",
       "icono": {
        "tipo": "embebido",
        "nombre": "bsiC_Procesos",
        "embebido": "iconos_embebidos/bsiC_Procesos.svg",
        "copiaDeKit": null
       },
       "menu": [
        {
         "id": "bbiCompradores",
         "tipo": "BarButtonItem",
         "texto": "Programadores",
         "icono": {
          "tipo": "recurso",
          "nombre": "usuarios",
          "kit": "../simulador de control ganadero/Kit_semantico/svg/usuarios.svg",
          "proyecto": "iconos_proyecto/usuarios.svg",
          "cambia": false
         },
         "menu": []
        },
        {
         "id": "bbiDueños",
         "tipo": "BarButtonItem",
         "texto": "Dueños",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiDueños",
          "embebido": "iconos_embebidos/bbiDueños.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiTransportistas",
         "tipo": "BarButtonItem",
         "texto": "Transportistas",
         "icono": {
          "tipo": "raster",
          "nombre": "bbiTransportistas",
          "embebido": "iconos_embebidos/bbiTransportistas.png",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiCategoriasVenta",
         "tipo": "BarButtonItem",
         "texto": "Categorias de Venta",
         "icono": {
          "tipo": "recurso",
          "nombre": "billete",
          "kit": "../simulador de control ganadero/Kit_semantico/svg/billete.svg",
          "proyecto": "iconos_proyecto/billete.svg",
          "cambia": false
         },
         "menu": []
        },
        {
         "id": "bbiCompradoresVenta",
         "tipo": "BarButtonItem",
         "texto": "Compradores de Venta",
         "icono": {
          "tipo": "recurso",
          "nombre": "usuario",
          "kit": "../simulador de control ganadero/Kit_semantico/svg/usuario.svg",
          "proyecto": "iconos_proyecto/usuario.svg",
          "cambia": false
         },
         "menu": []
        }
       ],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgCompraVenta",
     "texto": "Entradas y Salidas de Ganado",
     "visible": true,
     "items": [
      {
       "id": "bbiCompras",
       "tipo": "BarButtonItem",
       "texto": "Compras de Ganado",
       "icono": {
        "tipo": "recurso",
        "nombre": "documento-vaca",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/documento-vaca.svg",
        "proyecto": "iconos_proyecto/documento-vaca.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiFotosLotes",
       "tipo": "BarButtonItem",
       "texto": "Clasificaciones",
       "icono": {
        "tipo": "recurso",
        "nombre": "identificaciones-cedula-vaca",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/identificaciones-cedula-vaca.svg",
        "proyecto": "iconos_proyecto/identificaciones-cedula-vaca.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiVentas",
       "tipo": "BarButtonItem",
       "texto": "Venta de Ordinarios",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-dinero",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca-dinero.svg",
        "proyecto": "iconos_proyecto/vaca-dinero.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgTrasladoReses",
     "texto": "Recepción y Remisiones",
     "visible": true,
     "items": [
      {
       "id": "bbiListaRecepciones",
       "tipo": "BarButtonItem",
       "texto": "Lista de Recepcion",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-carrito",
        "kit": null,
        "proyecto": "iconos_proyecto/vaca-carrito.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiRemisiones",
       "tipo": "BarButtonItem",
       "texto": "Remisiones",
       "icono": {
        "tipo": "recurso",
        "nombre": "camion",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/camion.svg",
        "proyecto": "iconos_proyecto/camion.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiLiquidaciones",
       "tipo": "BarButtonItem",
       "texto": "Liquidaciones",
       "icono": {
        "tipo": "recurso",
        "nombre": "documento-dinero",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/documento-dinero.svg",
        "proyecto": "iconos_proyecto/documento-dinero.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgCalibraciones",
     "texto": "Básculas",
     "visible": true,
     "items": [
      {
       "id": "bbiCalibraciones",
       "tipo": "BarButtonItem",
       "texto": "Calibraciones",
       "icono": {
        "tipo": "recurso",
        "nombre": "bascula-check",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/bascula-check.svg",
        "proyecto": "iconos_proyecto/bascula-check.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgPesaje",
     "texto": "Báscula Camionera",
     "visible": true,
     "items": [
      {
       "id": "bbiPesajeMateriaPrima",
       "tipo": "BarButtonItem",
       "texto": "Pesaje de Materia Prima",
       "icono": {
        "tipo": "recurso",
        "nombre": "bascula",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/bascula.svg",
        "proyecto": "iconos_proyecto/bascula.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiReportePesaje",
       "tipo": "BarButtonItem",
       "texto": "Reporte de Pesaje",
       "icono": {
        "tipo": "recurso",
        "nombre": "bascula-reporte",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/bascula-reporte.svg",
        "proyecto": "iconos_proyecto/bascula-reporte.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  },
  {
   "id": "rpReses2",
   "texto": "RESES",
   "icono": {
    "tipo": "recurso",
    "nombre": "vaca",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca.svg",
    "proyecto": "iconos_proyecto/vaca.svg",
    "cambia": true
   },
   "grupos": [
    {
     "id": "rpgC_Reses",
     "texto": "Catálogos",
     "visible": true,
     "items": [
      {
       "id": "BarSubItem1",
       "tipo": "BarSubItem",
       "texto": "Catálogos de Reses",
       "icono": {
        "tipo": "embebido",
        "nombre": "BarSubItem1",
        "embebido": "iconos_embebidos/BarSubItem1.svg",
        "copiaDeKit": null
       },
       "menu": [
        {
         "id": "bbiZonas",
         "tipo": "BarButtonItem",
         "texto": "Zonas",
         "icono": {
          "tipo": "raster",
          "nombre": "bbiZonas",
          "embebido": "iconos_embebidos/bbiZonas.png",
          "copiaDeKit": null
         },
         "menu": []
        }
       ],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgC_Listas",
     "texto": "Listas de Reses",
     "visible": true,
     "items": [
      {
       "id": "bbiListaReses",
       "tipo": "BarButtonItem",
       "texto": "Lista de Reses",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-lista",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca-lista.svg",
        "proyecto": "iconos_proyecto/vaca-lista.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiResesVenta",
       "tipo": "BarButtonItem",
       "texto": "Reses Vendidas",
       "icono": {
        "tipo": "recurso",
        "nombre": "billete",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/billete.svg",
        "proyecto": "iconos_proyecto/billete.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiBuscadorReses",
       "tipo": "BarButtonItem",
       "texto": "Buscador de Reses",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiBuscadorReses",
        "embebido": "iconos_embebidos/bbiBuscadorReses.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiListaResesInactivos",
       "tipo": "BarButtonItem",
       "texto": "Reses Inactivas",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-menos",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca-menos.svg",
        "proyecto": "iconos_proyecto/vaca-menos.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiResesSinRegistro",
       "tipo": "BarButtonItem",
       "texto": "Reses Sin Registro",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-alerta",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca-alerta.svg",
        "proyecto": "iconos_proyecto/vaca-alerta.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  },
  {
   "id": "rpLotes",
   "texto": "FEEDLOT",
   "icono": {
    "tipo": "recurso",
    "nombre": "cerca",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/cerca.svg",
    "proyecto": "iconos_proyecto/cerca.svg",
    "cambia": false
   },
   "grupos": [
    {
     "id": "RibbonPageGroup4",
     "texto": "Administración",
     "visible": true,
     "items": [
      {
       "id": "BarSubItem2",
       "tipo": "BarSubItem",
       "texto": "Catálogos de Feedlot",
       "icono": {
        "tipo": "embebido",
        "nombre": "BarSubItem2",
        "embebido": "iconos_embebidos/BarSubItem2.svg",
        "copiaDeKit": null
       },
       "menu": [
        {
         "id": "btnCierreFormacion",
         "tipo": "BarButtonItem",
         "texto": "Cierres de Formacion",
         "icono": {
          "tipo": "embebido",
          "nombre": "btnCierreFormacion",
          "embebido": "iconos_embebidos/btnCierreFormacion.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "btnProtocolosInicio",
         "tipo": "BarButtonItem",
         "texto": "Protocolos de Inicio",
         "icono": {
          "tipo": "embebido",
          "nombre": "btnProtocolosInicio",
          "embebido": "iconos_embebidos/btnProtocolosInicio.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "btnAreasTrabajo",
         "tipo": "BarButtonItem",
         "texto": "Areas de Trabajo",
         "icono": {
          "tipo": "embebido",
          "nombre": "btnAreasTrabajo",
          "embebido": "iconos_embebidos/btnAreasTrabajo.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiImplantes",
         "tipo": "BarButtonItem",
         "texto": "Implantes",
         "icono": {
          "tipo": "raster",
          "nombre": "bbiImplantes",
          "embebido": "iconos_embebidos/bbiImplantes.png",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiImplantadores",
         "tipo": "BarButtonItem",
         "texto": "Implantadores",
         "icono": {
          "tipo": "raster",
          "nombre": "bbiImplantadores",
          "embebido": "iconos_embebidos/bbiImplantadores.png",
          "copiaDeKit": null
         },
         "menu": []
        }
       ],
       "separador": false
      },
      {
       "id": "BarButtonItem1",
       "tipo": "BarButtonItem",
       "texto": "Resumen",
       "icono": {
        "tipo": "recurso",
        "nombre": "GraficaMapaArbol",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/GraficaMapaArbol.svg",
        "proyecto": "iconos_proyecto/GraficaMapaArbol.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "RibbonPageGroup1",
     "texto": "Reses Feedlot",
     "visible": true,
     "items": [
      {
       "id": "bbiListaResesFeedLot",
       "tipo": "BarButtonItem",
       "texto": "Lista de Reses Feedlot",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca.svg",
        "proyecto": "iconos_proyecto/vaca.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgCorrales",
     "texto": "Manejo de Corrales",
     "visible": true,
     "items": [
      {
       "id": "bbiFormacionCorrales",
       "tipo": "BarButtonItem",
       "texto": "Formacion de Corrales",
       "icono": {
        "tipo": "recurso",
        "nombre": "corral-perspectiva-estrella",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/corral-perspectiva-estrella.svg",
        "proyecto": "iconos_proyecto/corral-perspectiva-estrella.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiListaCorrales",
       "tipo": "BarButtonItem",
       "texto": "Lista de Corrales",
       "icono": {
        "tipo": "recurso",
        "nombre": "corral-perspectiva",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/corral-perspectiva.svg",
        "proyecto": "iconos_proyecto/corral-perspectiva.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiMovimientosPorLote",
       "tipo": "BarButtonItem",
       "texto": "Movimientos por Lote",
       "icono": {
        "tipo": "recurso",
        "nombre": "corral-perspectiva-intercambio",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/corral-perspectiva-intercambio.svg",
        "proyecto": "iconos_proyecto/corral-perspectiva-intercambio.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgAretesRFID",
     "texto": "Aretes RFID",
     "visible": true,
     "items": [
      {
       "id": "bbiDeteccionesElectronicos",
       "tipo": "BarButtonItem",
       "texto": "Detecciones de Aretes",
       "icono": {
        "tipo": "recurso",
        "nombre": "arete-rfid-lista",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/arete-rfid-lista.svg",
        "proyecto": "iconos_proyecto/arete-rfid-lista.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiDistancias",
       "tipo": "BarButtonItem",
       "texto": "Distancias",
       "icono": {
        "tipo": "recurso",
        "nombre": "regla",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/regla.svg",
        "proyecto": "iconos_proyecto/regla.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgImplante",
     "texto": "Implantes",
     "visible": true,
     "items": [
      {
       "id": "bbiHistoricoImplantes",
       "tipo": "BarButtonItem",
       "texto": "Historico de Implantes",
       "icono": {
        "tipo": "recurso",
        "nombre": "implantador-lista",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/implantador-lista.svg",
        "proyecto": "iconos_proyecto/implantador-lista.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiEvaluacionImplantes",
       "tipo": "BarButtonItem",
       "texto": "Evaluacion de Implantes",
       "icono": {
        "tipo": "recurso",
        "nombre": "implantador-alerta",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/implantador-alerta.svg",
        "proyecto": "iconos_proyecto/implantador-alerta.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  },
  {
   "id": "rpPlanta",
   "texto": "P. ALIMENTOS",
   "icono": {
    "tipo": "recurso",
    "nombre": "saco-alimento",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/saco-alimento.svg",
    "proyecto": "iconos_proyecto/saco-alimento.svg",
    "cambia": false
   },
   "grupos": [
    {
     "id": "rpgC_PlantaAlimentos",
     "texto": "Catálogos",
     "visible": true,
     "items": [
      {
       "id": "bsiC_PlantaAlimentos",
       "tipo": "BarSubItem",
       "texto": "Catálogos de Planta",
       "icono": {
        "tipo": "embebido",
        "nombre": "bsiC_PlantaAlimentos",
        "embebido": "iconos_embebidos/bsiC_PlantaAlimentos.svg",
        "copiaDeKit": null
       },
       "menu": [
        {
         "id": "bbiAlimentos",
         "tipo": "BarButtonItem",
         "texto": "Alimentos",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiAlimentos",
          "embebido": "iconos_embebidos/bbiAlimentos.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiDietas",
         "tipo": "BarButtonItem",
         "texto": "Lista de Dietas",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiDietas",
          "embebido": "iconos_embebidos/bbiDietas.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiListaRutasDieta",
         "tipo": "BarButtonItem",
         "texto": "Rutas de Dietas",
         "icono": {
          "tipo": "raster",
          "nombre": "bbiListaRutasDieta",
          "embebido": "iconos_embebidos/bbiListaRutasDieta.png",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiListaEquipos",
         "tipo": "BarButtonItem",
         "texto": "Lista de Equipos",
         "icono": {
          "tipo": "raster",
          "nombre": "bbiListaEquipos",
          "embebido": "iconos_embebidos/bbiListaEquipos.png",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiCorralesAux",
         "tipo": "BarButtonItem",
         "texto": "Corrales Auxiliares",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiCorralesAux",
          "embebido": "iconos_embebidos/bbiCorralesAux.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiPorcentajes",
         "tipo": "BarButtonItem",
         "texto": "Porcentajes de Servicio",
         "icono": {
          "tipo": "raster",
          "nombre": "bbiPorcentajes",
          "embebido": "iconos_embebidos/bbiPorcentajes.png",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiOperadores",
         "tipo": "BarButtonItem",
         "texto": "Operadores",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiOperadores",
          "embebido": "iconos_embebidos/bbiOperadores.svg",
          "copiaDeKit": null
         },
         "menu": []
        }
       ],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgCalidad",
     "texto": "Calidad",
     "visible": true,
     "items": [
      {
       "id": "bbiControlCalidad",
       "tipo": "BarButtonItem",
       "texto": "Control de Calidad",
       "icono": {
        "tipo": "recurso",
        "nombre": "matraz-check",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/matraz-check.svg",
        "proyecto": "iconos_proyecto/matraz-check.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiReporteCalidad",
       "tipo": "BarButtonItem",
       "texto": "Pruebas a Fórmulas",
       "icono": {
        "tipo": "recurso",
        "nombre": "matraz-espiga",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/matraz-espiga.svg",
        "proyecto": "iconos_proyecto/matraz-espiga.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgReparto",
     "texto": "Reparto de Alimento",
     "visible": true,
     "items": [
      {
       "id": "bbiListaIndicadores",
       "tipo": "BarButtonItem",
       "texto": "Indicadores de Reparto",
       "icono": {
        "tipo": "recurso",
        "nombre": "indicador",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/indicador.svg",
        "proyecto": "iconos_proyecto/indicador.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiReparto",
       "tipo": "BarButtonItem",
       "texto": "Reparto",
       "icono": {
        "tipo": "recurso",
        "nombre": "camion-mixer",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/camion-mixer.svg",
        "proyecto": "iconos_proyecto/camion-mixer.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiConsumo",
       "tipo": "BarButtonItem",
       "texto": "Consumo",
       "icono": {
        "tipo": "recurso",
        "nombre": "medidor",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/medidor.svg",
        "proyecto": "iconos_proyecto/medidor.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "RibbonPageGroup7",
     "texto": "Lecturas",
     "visible": true,
     "items": [
      {
       "id": "bbiListaLecturas",
       "tipo": "BarButtonItem",
       "texto": "Lista de Lectura",
       "icono": {
        "tipo": "recurso",
        "nombre": "comedero-concreto-perspectiva",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/comedero-concreto-perspectiva.svg",
        "proyecto": "iconos_proyecto/comedero-concreto-perspectiva.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiGraficaAlimento",
       "tipo": "BarButtonItem",
       "texto": "Vista de Lectura",
       "icono": {
        "tipo": "recurso",
        "nombre": "GraficaCombinada",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/GraficaCombinada.svg",
        "proyecto": "iconos_proyecto/GraficaCombinada.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgEquipos",
     "texto": "Equipos",
     "visible": true,
     "items": [
      {
       "id": "bbiParoEquipos",
       "tipo": "BarButtonItem",
       "texto": "Paro de Equipos",
       "icono": {
        "tipo": "recurso",
        "nombre": "cargador-frontal-hexagono-integrado",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/cargador-frontal-hexagono-integrado.svg",
        "proyecto": "iconos_proyecto/cargador-frontal-hexagono-integrado.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgGraficasPlantaAlimentos",
     "texto": "Reportes y Dietas",
     "visible": true,
     "items": [
      {
       "id": "bbiReporteReparto",
       "tipo": "BarButtonItem",
       "texto": "Reporte de Reparto",
       "icono": {
        "tipo": "recurso",
        "nombre": "GraficaLineas",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/GraficaLineas.svg",
        "proyecto": "iconos_proyecto/GraficaLineas.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiPlanDietas",
       "tipo": "BarButtonItem",
       "texto": "Plan de Dietas",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiPlanDietas",
        "embebido": "iconos_embebidos/bbiPlanDietas.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiGraficasGerencial",
       "tipo": "BarButtonItem",
       "texto": "Graficas Gerenciales",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiGraficasGerencial",
        "embebido": "iconos_embebidos/bbiGraficasGerencial.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  },
  {
   "id": "rpSanidad",
   "texto": "SANIDAD",
   "icono": {
    "tipo": "recurso",
    "nombre": "cruz",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/cruz.svg",
    "proyecto": "iconos_proyecto/cruz.svg",
    "cambia": false
   },
   "grupos": [
    {
     "id": "rpgC_Sanidad",
     "texto": "Catálogos",
     "visible": true,
     "items": [
      {
       "id": "bsiC_Sanidad",
       "tipo": "BarSubItem",
       "texto": "Catálogos de Sanidad",
       "icono": {
        "tipo": "embebido",
        "nombre": "bsiC_Sanidad",
        "embebido": "iconos_embebidos/bsiC_Sanidad.svg",
        "copiaDeKit": null
       },
       "menu": [
        {
         "id": "bbiProductos",
         "tipo": "BarButtonItem",
         "texto": "Productos",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiProductos",
          "embebido": "iconos_embebidos/bbiProductos.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiProtocolos",
         "tipo": "BarButtonItem",
         "texto": "Protocolos",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiProtocolos",
          "embebido": "iconos_embebidos/bbiProtocolos.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiCausasSanidad",
         "tipo": "BarButtonItem",
         "texto": "Causas de Deteccion",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiCausasSanidad",
          "embebido": "iconos_embebidos/bbiCausasSanidad.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiCausaOrdinarioVenta",
         "tipo": "BarButtonItem",
         "texto": "Causas de Ordinarios/Venta",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiCausaOrdinarioVenta",
          "embebido": "iconos_embebidos/bbiCausaOrdinarioVenta.svg",
          "copiaDeKit": null
         },
         "menu": []
        },
        {
         "id": "bbiCausasMuerte",
         "tipo": "BarButtonItem",
         "texto": "Causas de Muerte",
         "icono": {
          "tipo": "embebido",
          "nombre": "bbiCausasMuerte",
          "embebido": "iconos_embebidos/bbiCausasMuerte.svg",
          "copiaDeKit": null
         },
         "menu": []
        }
       ],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgDeteccion",
     "texto": "Enfermería y Detección",
     "visible": true,
     "items": [
      {
       "id": "bbiEnfermeria",
       "tipo": "BarButtonItem",
       "texto": "Enfermeria",
       "icono": {
        "tipo": "recurso",
        "nombre": "botiquin",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/botiquin.svg",
        "proyecto": "iconos_proyecto/botiquin.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiDeteccion",
       "tipo": "BarButtonItem",
       "texto": "Detección",
       "icono": {
        "tipo": "recurso",
        "nombre": "jeringa-lista",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/jeringa-lista.svg",
        "proyecto": "iconos_proyecto/jeringa-lista.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiTraslado",
       "tipo": "BarButtonItem",
       "texto": "Traslado",
       "icono": {
        "tipo": "recurso",
        "nombre": "jeringa-reloj",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/jeringa-reloj.svg",
        "proyecto": "iconos_proyecto/jeringa-reloj.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgBienestar",
     "texto": "Bienestar",
     "visible": true,
     "items": [
      {
       "id": "bbiEvaluacionDeteccion",
       "tipo": "BarButtonItem",
       "texto": "Evaluacion de Deteccion",
       "icono": {
        "tipo": "recurso",
        "nombre": "matraz-lupa",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/matraz-lupa.svg",
        "proyecto": "iconos_proyecto/matraz-lupa.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiCalidadAgua",
       "tipo": "BarButtonItem",
       "texto": "Calidad de Agua",
       "icono": {
        "tipo": "recurso",
        "nombre": "matraz-gota",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/matraz-gota.svg",
        "proyecto": "iconos_proyecto/matraz-gota.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgGraficasSanidad",
     "texto": "Gráficas",
     "visible": true,
     "items": [
      {
       "id": "bbiGraficas",
       "tipo": "BarButtonItem",
       "texto": "Gráficas de Sanidad",
       "icono": {
        "tipo": "recurso",
        "nombre": "GraficaPastel",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/GraficaPastel.svg",
        "proyecto": "iconos_proyecto/GraficaPastel.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgMortalidad",
     "texto": "Mortalidad de Reses",
     "visible": true,
     "items": [
      {
       "id": "bbiMortalidadReses",
       "tipo": "BarButtonItem",
       "texto": "Mortalidad de Reses",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-calavera",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca-calavera.svg",
        "proyecto": "iconos_proyecto/vaca-calavera.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  },
  {
   "id": "rpCrianza",
   "texto": "CRIANZA",
   "icono": {
    "tipo": "recurso",
    "nombre": "adn-frontal",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/adn-frontal.svg",
    "proyecto": "iconos_proyecto/adn-frontal.svg",
    "cambia": false
   },
   "grupos": [
    {
     "id": "RibbonPageGroup5",
     "texto": "Catálogos",
     "visible": true,
     "items": [
      {
       "id": "BarSubItem3",
       "tipo": "BarSubItem",
       "texto": "Catálogos de Crianza",
       "icono": {
        "tipo": "embebido",
        "nombre": "BarSubItem3",
        "embebido": "iconos_embebidos/BarSubItem3.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": true
      }
     ]
    },
    {
     "id": "RibbonPageGroup2",
     "texto": "Listado de Reses",
     "visible": true,
     "items": [
      {
       "id": "bbiListaResesCrianza",
       "tipo": "BarButtonItem",
       "texto": "Lista de Reses Crianza",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca.svg",
        "proyecto": "iconos_proyecto/vaca.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiListaResesDesarrollo",
       "tipo": "BarButtonItem",
       "texto": "Lista de Reses Desarrollo",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-arriba",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca-arriba.svg",
        "proyecto": "iconos_proyecto/vaca-arriba.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiNacimientos",
       "tipo": "BarButtonItem",
       "texto": "Nacimientos",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-mas",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca-mas.svg",
        "proyecto": "iconos_proyecto/vaca-mas.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "RibbonPageGroup6",
     "texto": "Manejo de Crianza",
     "visible": true,
     "items": [
      {
       "id": "bbiLoteCrianza",
       "tipo": "BarButtonItem",
       "texto": "Lote de Crianza",
       "icono": {
        "tipo": "recurso",
        "nombre": "crianza",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/crianza.svg",
        "proyecto": "iconos_proyecto/crianza.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiAltasDestete",
       "tipo": "BarButtonItem",
       "texto": "Altas por Destete",
       "icono": {
        "tipo": "recurso",
        "nombre": "documento-vaca",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/documento-vaca.svg",
        "proyecto": "iconos_proyecto/documento-vaca.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "RibbonPageGroup3",
     "texto": "Sanidad de Crianza",
     "visible": true,
     "items": [
      {
       "id": "bbiSanidadCrianza",
       "tipo": "BarButtonItem",
       "texto": "Sanidad de Crianza",
       "icono": {
        "tipo": "recurso",
        "nombre": "botiquin",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/botiquin.svg",
        "proyecto": "iconos_proyecto/botiquin.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  },
  {
   "id": "rpMaquila",
   "texto": "MAQUILA",
   "icono": {
    "tipo": "recurso",
    "nombre": "corral-manga",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/corral-manga.svg",
    "proyecto": "iconos_proyecto/corral-manga.svg",
    "cambia": false
   },
   "grupos": [
    {
     "id": "rpgMaquila",
     "texto": "Maquila",
     "visible": true,
     "items": [
      {
       "id": "bbiListaResesMaquila",
       "tipo": "BarButtonItem",
       "texto": "Reses de Maquila",
       "icono": {
        "tipo": "recurso",
        "nombre": "vaca-estrella",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/vaca-estrella.svg",
        "proyecto": "iconos_proyecto/vaca-estrella.svg",
        "cambia": true
       },
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  },
  {
   "id": "rpReportes",
   "texto": "REPORTES",
   "icono": {
    "tipo": "recurso",
    "nombre": "grafico-lineas-ambar",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/grafico-lineas-ambar.svg",
    "proyecto": "iconos_proyecto/grafico-lineas-ambar.svg",
    "cambia": false
   },
   "grupos": [
    {
     "id": "rpgReporteCompras",
     "texto": "Reportes de Compras",
     "visible": true,
     "items": [
      {
       "id": "bbiComprasProgramadores",
       "tipo": "BarButtonItem",
       "texto": "Compras de Programadores",
       "icono": {
        "tipo": "raster",
        "nombre": "bbiComprasProgramadores",
        "embebido": "iconos_embebidos/bbiComprasProgramadores.png",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiDinamicoCompras",
       "tipo": "BarButtonItem",
       "texto": "Dinamico de Compras",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiDinamicoCompras",
        "embebido": "iconos_embebidos/bbiDinamicoCompras.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiReciboPagos",
       "tipo": "BarButtonItem",
       "texto": "Recibo de Pagos",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiReciboPagos",
        "embebido": "iconos_embebidos/bbiReciboPagos.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgReporteCorrales",
     "texto": "Reportes de Corrales",
     "visible": true,
     "items": [
      {
       "id": "bbiResumenCorrales",
       "tipo": "BarButtonItem",
       "texto": "Resumen Corrales",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiResumenCorrales",
        "embebido": "iconos_embebidos/bbiResumenCorrales.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiCentroReportes",
       "tipo": "BarButtonItem",
       "texto": "Centro de Reportes",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiCentroReportes",
        "embebido": "iconos_embebidos/bbiCentroReportes.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiReporteImplantes",
       "tipo": "BarButtonItem",
       "texto": "Reporte de Implantes",
       "icono": {
        "tipo": "recurso",
        "nombre": "implantador-reporte",
        "kit": "../simulador de control ganadero/Kit_semantico/svg/implantador-reporte.svg",
        "proyecto": "iconos_proyecto/implantador-reporte.svg",
        "cambia": false
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgReporteReses",
     "texto": "Reportes de Reses",
     "visible": true,
     "items": [
      {
       "id": "bbiFormatosBA",
       "tipo": "BarButtonItem",
       "texto": "Formatos BA",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiFormatosBA",
        "embebido": "iconos_embebidos/bbiFormatosBA.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiImproductivos",
       "tipo": "BarButtonItem",
       "texto": "Reporte de Ordinarios",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiImproductivos",
        "embebido": "iconos_embebidos/bbiImproductivos.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiReporteRechazos",
       "tipo": "BarButtonItem",
       "texto": "Reporte de Rechazos",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiReporteRechazos",
        "embebido": "iconos_embebidos/bbiReporteRechazos.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgReporteGerencial",
     "texto": "Gerencial",
     "visible": true,
     "items": [
      {
       "id": "bbiReporteGerencial",
       "tipo": "BarButtonItem",
       "texto": "Reporte Gerencial",
       "icono": {
        "tipo": "raster",
        "nombre": "bbiReporteGerencial",
        "embebido": "iconos_embebidos/bbiReporteGerencial.png",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  },
  {
   "id": "rpAjustes",
   "texto": "AJUSTES",
   "icono": {
    "tipo": "recurso",
    "nombre": "engranaje",
    "kit": "../simulador de control ganadero/Kit_semantico/svg/engranaje.svg",
    "proyecto": "iconos_proyecto/engranaje.svg",
    "cambia": false
   },
   "grupos": [
    {
     "id": "rpgUsuarios",
     "texto": "Usuarios y Roles",
     "visible": true,
     "items": [
      {
       "id": "bbiRoles",
       "tipo": "BarButtonItem",
       "texto": "Roles",
       "icono": {
        "tipo": "raster",
        "nombre": "bbiRoles",
        "embebido": "iconos_embebidos/bbiRoles.png",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "bbiUsers",
       "tipo": "BarButtonItem",
       "texto": "Usuarios",
       "icono": {
        "tipo": "raster",
        "nombre": "bbiUsers",
        "embebido": "iconos_embebidos/bbiUsers.png",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgOffline",
     "texto": "Offline",
     "visible": true,
     "items": [
      {
       "id": "bbiConfigurarOffline",
       "tipo": "BarButtonItem",
       "texto": "Configurar Offline",
       "icono": {
        "tipo": "embebido",
        "nombre": "bbiConfigurarOffline",
        "embebido": "iconos_embebidos/bbiConfigurarOffline.svg",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      }
     ]
    },
    {
     "id": "rpgGeneral",
     "texto": "Sistema",
     "visible": true,
     "items": [
      {
       "id": "rgbiSkins",
       "tipo": "RibbonGalleryBarItem",
       "texto": "Temas",
       "icono": {
        "tipo": "raster",
        "nombre": "rgbiSkins",
        "embebido": "iconos_embebidos/rgbiSkins.png",
        "copiaDeKit": null
       },
       "menu": [],
       "separador": false
      },
      {
       "id": "iExit",
       "tipo": "BarButtonItem",
       "texto": "Salir",
       "icono": null,
       "menu": [],
       "separador": false
      }
     ]
    }
   ]
  }
 ]
};
