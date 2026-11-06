import unittest
from ejercicio_1_sensores.sensores import limpiar_registro_sensor, generar_resumen_sensores
class TestSensores(unittest.TestCase):
    def test_limpieza_y_no_mutacion(self):
        raw = {"sensor_id":" S-1 ","temperatura":" 31.2°C ","ubicacion":" "}
        self.assertEqual(limpiar_registro_sensor(raw), {"sensor_id":"S-1","temperatura":31.2,"ubicacion":"Área No Asignada"})
        self.assertEqual(raw["temperatura"], " 31.2°C ")
    def test_numeros_y_errores(self):
        self.assertEqual(limpiar_registro_sensor({"temperatura":24})["temperatura"],24.0)
        self.assertEqual(limpiar_registro_sensor({"temperatura":"error"})["temperatura"],0.0)
    def test_sin_registros(self):
        self.assertEqual(generar_resumen_sensores([],30),([],0.0))
    def test_alerta_umbral_estricto_y_promedio(self):
        datos=[{"sensor_id":"A","temperatura":30.0},{"sensor_id":"B","temperatura":31.125}]
        self.assertEqual(generar_resumen_sensores(datos,30),(["B"],30.56))
