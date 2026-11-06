"""Prueba de integración, ejecutable cuando se instala Django."""
import os
import unittest
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ejercicio_3_auditoria_web.settings")
try:
    import django
    django.setup()
    from django.test import Client
except ImportError:
    django = None

@unittest.skipIf(django is None, "Django no está instalado")
class TestVistaDjango(unittest.TestCase):
    def test_renderizado_y_contexto(self):
        respuesta=Client().get("/panel/")
        self.assertEqual(respuesta.status_code,200)
        self.assertIn(b"Panel de Sustentabilidad",respuesta.content)
        self.assertIn(b"Planta Este",respuesta.content)
