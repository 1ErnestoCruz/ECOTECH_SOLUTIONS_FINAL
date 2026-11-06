import json
import tempfile
import unittest
from pathlib import Path
from ejercicio_2_productos.productos import DispositivoEcologico, PanelSolar, GestorInventario, StockInvalidoError
class TestProductos(unittest.TestCase):
    def test_stock_invalido_constructor_y_setter(self):
        with self.assertRaises(StockInvalidoError):
            DispositivoEcologico("1","X",100,-1)
        producto=DispositivoEcologico("1","X",100,2)
        with self.assertRaises(StockInvalidoError):
            producto.stock=-5
        self.assertEqual(producto.stock,2)
    def test_herencia_polimorfismo(self):
        panel=PanelSolar("1","Solar",100.5,3,20.0,400)
        self.assertIsInstance(panel,DispositivoEcologico)
        ficha=panel.generar_ficha_tecnica()
        self.assertEqual(ficha["precio"],"$100.50")
        self.assertEqual(ficha["potencia_w"],400)
    def test_persistencia(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta=Path(carpeta)/"catalogo_ecotech.json"
            GestorInventario().guardar_catalogo_json([PanelSolar("1","Solar",100.5,3,20.0,400)],ruta)
            datos=json.loads(ruta.read_text(encoding="utf-8"))
            self.assertEqual(datos[0]["stock"],3)
            self.assertEqual(datos[0]["tipo"],"PanelSolar")
