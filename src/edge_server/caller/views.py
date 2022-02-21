from django.http import JsonResponse

from generated.revert_pb2 import RevertRequest
from generated.revert_pb2_grpc import RevertApiStub
from generated.time_pb2 import TimeRequest
from generated.time_pb2_grpc import TimeProcedureApiStub
from grpc_client.client import GrpcClient


def get_time():
    with GrpcClient.stub(TimeProcedureApiStub, 'time-server-grpc:50051') as stub:
        req = TimeRequest()
        response = stub.WhatTimeIs(req, timeout=5)
        return response.time


def get_reverted_name(name):
    with GrpcClient.stub(RevertApiStub, 'revert-name-server-grpc:50052') as stub:
        req = RevertRequest(name=name, delay=0)
        response = stub.RevertName(req, timeout=5)
        return response.name


def reverse_name(request, name):
    return JsonResponse({
        'name': name,
        'reversed_name': get_reverted_name(name),
        'time': get_time()
    })
