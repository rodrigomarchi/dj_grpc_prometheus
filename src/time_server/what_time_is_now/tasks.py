from celery import shared_task

from generated.heartbeat_pb2 import BeatRequest
from generated.heartbeat_pb2_grpc import HeartBeatApiStub
from grpc_client.client import GrpcClient


@shared_task(name="heartbeat_to_edge_server")
def heartbeat():
    with GrpcClient.stub(HeartBeatApiStub, 'edge-server-grpc:50053') as stub:
        req = BeatRequest(service_name='time_server')
        stub.BeatHeart(req, timeout=5)
