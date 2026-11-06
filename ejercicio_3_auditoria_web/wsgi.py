import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ejercicio_3_auditoria_web.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
