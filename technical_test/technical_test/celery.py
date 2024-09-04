from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer el entorno de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'technical_test.settings')

app = Celery('technical_test')

# Cargar la configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubrir tareas automáticamente en las aplicaciones Django
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'update-drivers-every-30-seconds': {
        'task': 'your_app_name.tasks.update_available_drivers',
        'schedule': 30.0,
    },
}