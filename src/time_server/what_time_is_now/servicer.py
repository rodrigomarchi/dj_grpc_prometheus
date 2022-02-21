from datetime import datetime

from generated import time_pb2_grpc, time_pb2


def grpc_hook(server):
    time_pb2_grpc.add_TimeProcedureApiServicer_to_server(
        TimeProcedureApiServicer(), server)


class TimeProcedureApiServicer(time_pb2_grpc.TimeProcedureApiServicer):
    def WhatTimeIs(self, request, context):
        return time_pb2.TimeResponse(time=datetime.now().isoformat())
