import os
import sys

from celery import maybe_patch_concurrency
from prometheus_client import start_http_server


def main():
    if 'multi' not in sys.argv:
        maybe_patch_concurrency()
    from celery.bin.celery import main as _main

    sys.exit(_main())


if __name__ == '__main__':
    main()
