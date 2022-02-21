import os
import sys

from celery import maybe_patch_concurrency
from prometheus_client import start_http_server


def main():
    if 'multi' not in sys.argv:
        maybe_patch_concurrency()
    from celery.bin.celery import main as _main

    celery_prometheus_port = os.environ.get('CELERY_PROMETHEUS_PORT', None)
    if celery_prometheus_port and celery_prometheus_port.isdigit():
        start_http_server(int(celery_prometheus_port))

    sys.exit(_main())


if __name__ == '__main__':
    main()
