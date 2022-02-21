from generated import heartbeat_pb2, heartbeat_pb2_grpc
from heartbeat.models import HeartBeat


def grpc_hook(server):
    heartbeat_pb2_grpc.add_HeartBeatApiServicer_to_server(
        HeartBeatServicer(), server)


class HeartBeatServicer(heartbeat_pb2_grpc.HeartBeatApiServicer):
    def BeatHeart(self, request, context):
        beat = HeartBeat()
        beat.service = request.service_name
        beat.save()
        return heartbeat_pb2.BeatResponse()
