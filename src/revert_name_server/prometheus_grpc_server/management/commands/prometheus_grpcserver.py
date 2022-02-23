import datetime

from django.utils import autoreload
from django_grpc.utils import extract_handlers, create_server
from prometheus_client import start_http_server
from django_grpc.management.commands import grpcserver


class Command(grpcserver.Command):

    def add_arguments(self, parser):
        parser.add_argument('--max_workers', type=int, help="Number of workers")
        parser.add_argument('--port', type=int, default=50051, help="Port number to listen")
        parser.add_argument('--prometheus_port', type=int, default=9999, help="Prometheus port number")
        parser.add_argument('--autoreload', action='store_true', default=False)
        parser.add_argument('--list-handlers', action='store_true', default=False, help="Print all registered endpoints")

    def _serve(self, max_workers, port, prometheus_port, *args, **kwargs):
        autoreload.raise_last_exception()
        self.stdout.write("Starting server at %s" % datetime.datetime.now())

        server = create_server(max_workers, port)
        server.start()

        start_http_server(prometheus_port)

        self.stdout.write("Server is listening port %s" % port)
        self.stdout.write("Prometheus is listening port %s" % prometheus_port)

        if kwargs['list_handlers'] is True:
            self.stdout.write("Registered handlers:")
            for handler in extract_handlers(server):
                self.stdout.write("* %s" % handler)

        server.wait_for_termination()
