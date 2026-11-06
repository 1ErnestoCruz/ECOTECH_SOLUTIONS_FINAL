"""Ejercicio 2: clases, validaciones y persistencia del inventario."""
import json
from pathlib import Path


class StockInvalidoError(Exception):
    def __init__(self, mensaje="El stock no puede ser un valor negativo."):
        super().__init__(mensaje)


class DispositivoEcologico:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self._stock = 0
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("El stock debe ser un número entero")
        if valor < 0:
            raise StockInvalidoError(f"Stock inválido para '{self.nombre}': {valor}. No puede ser negativo.")
        self._stock = valor

    def generar_ficha_tecnica(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": f"${self.precio:.2f}",
            "stock": self.stock,
            "tipo": "Dispositivo ecológico",
        }

    def a_diccionario(self):
        """Formato apto para persistencia, con precio numérico."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "tipo": "DispositivoEcologico",
        }


class PanelSolar(DispositivoEcologico):
    def __init__(self, id_producto, nombre, precio, stock, eficiencia, potencia_w):
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self):
        ficha = super().generar_ficha_tecnica()
        ficha.update({"tipo": "Panel solar", "eficiencia": f"{self.eficiencia:.2f}%", "potencia_w": self.potencia_w})
        return ficha

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos.update({"tipo": "PanelSolar", "eficiencia": self.eficiencia, "potencia_w": self.potencia_w})
        return datos


class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        ruta = Path(ruta_archivo)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        datos = [dispositivo.a_diccionario() for dispositivo in lista_dispositivos]
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
        return ruta


if __name__ == "__main__":
    panel = PanelSolar("SOL-001", "Panel Solar Eco 450", 189999.90, 12, 21.5, 450)
    bateria = DispositivoEcologico("BAT-002", "Batería Sustentable", 85000.0, 8)
    print("=== FICHAS TÉCNICAS ===")
    print(json.dumps(panel.generar_ficha_tecnica(), ensure_ascii=False, indent=2))
    print(json.dumps(bateria.generar_ficha_tecnica(), ensure_ascii=False, indent=2))
    try:
        panel.stock = -5
    except StockInvalidoError as error:
        print(f"Error de stock capturado correctamente: {error}")
    ruta = Path(__file__).with_name("catalogo_ecotech.json")
    GestorInventario().guardar_catalogo_json([panel, bateria], ruta)
    print(f"Catálogo válido exportado: {ruta}")
