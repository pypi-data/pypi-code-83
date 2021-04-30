import json

import grpc

import dragon.dragon_pb2 as dragon_pb2
import dragon.dragon_pb2_grpc as dragon_pb2_grpc


class DragonClient:
    def __init__(self, host="localhost", port=50051):
        self._channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = dragon_pb2_grpc.DragonStub(channel=self._channel)

    def _format_and_return_respose(self, response: dragon_pb2.Response) -> dict:
        return {"status": response.status, "data": json.loads(response.message)}

    def start_container(self, request: dragon_pb2.StartContainerRequest) -> dict:
        return self._format_and_return_respose(self.stub.StartContainer(request))

    def commit_container(self, request: dragon_pb2.CommitContainerRequest) -> dict:
        return self._format_and_return_respose(self.stub.CommitContainer(request))

    def stop_container(self, request: dragon_pb2.StopContainerRequest) -> dict:
        return self._format_and_return_respose(self.stub.StopContainerRequest(request))

    def remove_container(self, request: dragon_pb2.RemoveContainerRequest) -> dict:
        return self._format_and_return_respose(
            self.stub.RemoveContainerRequest(request)
        )

    def ping_service(self, request: dragon_pb2.PingPongRequest) -> dict:
        res = self.stub.PingPong(request)
        return {"id": res.client_id}
