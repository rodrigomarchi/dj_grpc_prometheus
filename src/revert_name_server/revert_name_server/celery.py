import os

from celery import Celery
from celery.signals import worker_init
from django.conf import settings
from prometheus_client import start_http_server


@worker_init.connect
def prometheus_celeryd_init(**kwargs):
    port = os.environ.get('CELERY_PROMETHEUS_PORT', None)
    prometheus_multiproc_dir = os.environ.get('PROMETHEUS_MULTIPROC_DIR', None)
    if port and prometheus_multiproc_dir:
        start_http_server(int(port), registry=settings.PROMETHEUS_REGISTRY)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "revert_name_server.settings")
app = Celery("revert_name_server")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
