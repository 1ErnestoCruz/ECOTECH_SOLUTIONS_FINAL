import json
from pathlib import Path
from django.shortcuts import render
from ejercicio_3_auditoria_web.emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    """Vista FBV exigida: prepara métricas y renderiza sustentabilidad/panel.html."""
    ruta = Path(__file__).resolve().parent.parent / "data" / "consumos.json"
    with ruta.open(encoding="utf-8") as archivo:
        registros = json.load(archivo)
    contexto = obtener_metricas_consumo(registros)
    contexto["titulo"] = "Panel de Sustentabilidad"
    return render(request, "sustentabilidad/panel.html", contexto)
