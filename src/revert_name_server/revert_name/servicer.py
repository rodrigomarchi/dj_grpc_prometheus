from time import sleep

import grpc

from generated import revert_pb2_grpc, revert_pb2

STATUS_CODE_ERROR_STR = [x.name for x in grpc.StatusCode]


def grpc_hook(server):
    revert_pb2_grpc.add_RevertApiServicer_to_server(RevertApiServicer(), server)


class RevertApiServicer(revert_pb2_grpc.RevertApiServicer):
    def RevertName(self, request, context):
        name = request.name
        delay = request.delay

        sleep(delay)

        if name == 'key_error':
            print(name[len(name) + 1])

        if name == 'exception':
            raise Exception('Help!!!')

        if name.upper() in STATUS_CODE_ERROR_STR:
            context.set_code(grpc.StatusCode[name.upper()])

        response = revert_pb2.RevertResponse(name=name[::-1])
        return response
