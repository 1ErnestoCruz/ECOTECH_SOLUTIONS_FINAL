from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "clave-solo-para-desarrollo-local-no-usar-en-produccion"
DEBUG = True  # Uso local de demostración; no desplegar a Internet así.
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]
INSTALLED_APPS = ["django.contrib.staticfiles", "ejercicio_3_auditoria_web.sustentabilidad"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware", "django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "ejercicio_3_auditoria_web.urls"
TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [], "APP_DIRS": True, "OPTIONS": {"context_processors": []}}]
WSGI_APPLICATION = "ejercicio_3_auditoria_web.wsgi.application"
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Mendoza"
USE_I18N = True
USE_TZ = True
