"""Cálculo verificable de emisiones industriales en kg de CO2 equivalente."""


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo eléctrico no puede ser negativo")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    """Calcula emisiones globales y planta de mayor consumo (primer empate)."""
    total_emisiones = 0.0
    planta_mayor_consumo = None
    mayor_consumo = -1
    total_consumo = 0.0
    detalle = []
    for registro in registros:
        consumo = registro["consumo_kwh"]
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        total_consumo += consumo
        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor_consumo = registro["planta"]
        detalle.append({"planta": registro["planta"], "consumo_kwh": consumo, "emisiones_kg": emisiones})
    return {
        "total_emisiones": round(total_emisiones, 2),
        "planta_mayor_consumo": planta_mayor_consumo,
        "total_consumo_kwh": round(total_consumo, 2),
        "cantidad_plantas": len(registros),
        "detalle_plantas": detalle,
        "factor_emision": 0.4,
    }
