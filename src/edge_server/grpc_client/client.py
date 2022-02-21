import logging
from contextlib import contextmanager
from typing import Any, Dict, Generator, Type

import grpc
from py_grpc_prometheus.prometheus_client_interceptor import \
    PromClientInterceptor

logger = logging.getLogger(__name__)


class ChannelStateLogger:

    def __init__(self, target):
        self.target = target

    def log_state(self, state):
        logger.info(f"Channel {self.target} state changed to {state}")


class GrpcClient:
    _channels = {}
    _prometheus_interceptor = PromClientInterceptor(
        enable_client_handling_time_histogram=True,)
    DEFAULT_OPTIONS = {
        # Send keepalive ping every 30 seconds, default is 2 hours.
        "grpc.keepalive_time_ms": 30000,
        # Keepalive ping time out after 5 seconds, default is 20 seconds.
        "grpc.keepalive_timeout_ms": 5000,
        # Allow keepalive pings when there's no gRPC calls.
        "grpc.keepalive_permit_without_calls": True,
        # Allow unlimited amount of keepalive pings without data.
        "grpc.http2.max_pings_without_data": 0,
        # Allow grpc pings from client every 30 seconds.
        "grpc.http2.min_time_between_pings_ms": 30000,
        # Allow grpc pings from client without data every 30 seconds.
        "grpc.http2.min_ping_interval_without_data_ms": 30000,
    }

    @classmethod
    @contextmanager
    def stub(
            cls,
            stub_class: Type,
            target: str,
            custom_options: Dict[str, Any] = None
    ) -> Generator:
        if target not in cls._channels:
            state_logger = ChannelStateLogger(target)
            options = cls.DEFAULT_OPTIONS.copy()
            if custom_options:
                options.update(custom_options)
            options = [(k, v) for k, v in options.items()]
            channel = grpc.insecure_channel(target, options=options)
            channel = grpc.intercept_channel(channel,
                                             cls._prometheus_interceptor)
            channel.subscribe(state_logger.log_state)
            cls._channels[target] = channel

        stub = stub_class(cls._channels[target])
        yield stub

    @classmethod
    def _close_all_channels(cls):
        for channel in cls._channels.values():
            channel.close()
        cls._channels = {}

    def __del__(self):
        GrpcClient._close_all_channels()
