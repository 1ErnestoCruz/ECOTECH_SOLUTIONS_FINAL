"""Ejercicio 1: normalización y análisis de sensores térmicos."""
import math


def limpiar_registro_sensor(registro_raw):
    """Retorna un diccionario nuevo; errores de temperatura se convierten a 0.0."""
    if not isinstance(registro_raw, dict):
        raise TypeError("El registro del sensor debe ser un diccionario")
    limpio = {}
    limpio["sensor_id"] = str(registro_raw.get("sensor_id") or "").strip()
    valor = registro_raw.get("temperatura")
    try:
        if isinstance(valor, bool):
            raise ValueError("Los booleanos no son temperaturas")
        if isinstance(valor, (int, float)):
            temperatura = float(valor)
        else:
            texto = str(valor or "").strip().upper()
            for caracter in ("°", "C", "F", " "):
                texto = texto.replace(caracter, "")
            temperatura = float(texto)
        if not math.isfinite(temperatura):
            raise ValueError("La temperatura debe ser finita")
    except (ValueError, TypeError, OverflowError):
        temperatura = 0.0
    limpio["temperatura"] = temperatura
    ubicacion = registro_raw.get("ubicacion")
    limpio["ubicacion"] = (ubicacion.strip() if isinstance(ubicacion, str) and ubicacion.strip() else "Área No Asignada")
    return limpio


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """Devuelve (IDs que superan estrictamente el umbral, promedio redondeado)."""
    if not lista_sensores_limpios:
        return ([], 0.0)
    alertas = []
    acumulado = 0.0
    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        acumulado += temperatura
        if temperatura > umbral_temperatura:
            alertas.append(sensor["sensor_id"])
    return alertas, round(acumulado / len(lista_sensores_limpios), 2)


if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": " Planta Norte "},
        {"sensor_id": " SENSOR-002 ", "temperatura": "35.0 °C", "ubicacion": "  "},
        {"sensor_id": "SENSOR-003", "temperatura": 29, "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-004", "temperatura": "dato corrupto"},
    ]
    sensores_limpios = [limpiar_registro_sensor(r) for r in registros_crudos]
    alertas, promedio = generar_resumen_sensores(sensores_limpios, 30.0)
    print("=== REPORTE ECOTECH: SENSORES ===")
    for sensor in sensores_limpios:
        print(f'{sensor["sensor_id"]:12} | {sensor["temperatura"]:6.2f} °C | {sensor["ubicacion"]}')
    print(f"Umbral: 30.00 °C | Sensores en alerta: {', '.join(alertas) or 'Ninguno'}")
    print(f"Promedio global: {promedio:.2f} °C")
