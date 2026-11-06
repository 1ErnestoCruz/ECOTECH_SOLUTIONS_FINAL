import unittest
from ejercicio_3_auditoria_web.emisiones import calcular_emisiones_carbono, obtener_metricas_consumo
class TestCalculoEmisiones(unittest.TestCase):
    def test_valores_nominales(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100),40.0)
        self.assertAlmostEqual(calcular_emisiones_carbono(250,0.5),125.0)
    def test_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0),0.0)
    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-1)
    def test_metricas(self):
        r=obtener_metricas_consumo([{"planta":"A","consumo_kwh":100},{"planta":"B","consumo_kwh":200}])
        self.assertEqual(r["total_emisiones"],120.0)
        self.assertEqual(r["planta_mayor_consumo"],"B")
    def test_sin_registros(self):
        r=obtener_metricas_consumo([])
        self.assertEqual(r["total_emisiones"],0)
        self.assertIsNone(r["planta_mayor_consumo"])
    def test_consumo_invalido_propagado(self):
        with self.assertRaises(ValueError):
            obtener_metricas_consumo([{"planta":"A","consumo_kwh":-1}])
