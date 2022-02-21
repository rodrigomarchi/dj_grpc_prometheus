from prometheus_client import REGISTRY
from py_grpc_prometheus.prometheus_server_interceptor import \
    PromServerInterceptor


class PromServerInterceptorWrapper(PromServerInterceptor):
    def __init__(self, legacy=False, skip_exceptions=False,
                 log_exceptions=True, registry=REGISTRY):
        super(PromServerInterceptorWrapper, self).__init__(
            enable_handling_time_histogram=True, legacy=legacy,
            skip_exceptions=skip_exceptions, log_exceptions=log_exceptions,
            registry=registry)
