from concurrent import futures

import grpc
import command_pb2
import command_pb2_grpc

from packet_manager import PacketManager

class ServerCommandServiver(command_pb2_grpc.CommandServiceServicer):
    def CheckCommand(self, request, context):
        response = PacketManager.checker(request)
        
        return command_pb2.Response(
            message=response
        )
        
server = grpc.server(
    futures.ThreadPoolExecutor(max_workers=10)
)

command_pb2_grpc.add_CommandServiceServicer_to_server(
    ServerCommandServiver(),
    server
)
server.add_insecure_port("localhost:4000")
server.start()
server.wait_for_termination