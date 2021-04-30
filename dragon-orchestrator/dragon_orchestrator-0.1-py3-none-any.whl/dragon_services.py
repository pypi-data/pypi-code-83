import json
import logging
import os

import docker
import grpc
import requests

import dragon.dragon_client as dragon_client
import dragon.dragon_constants as dragon_constants
import dragon.dragon_pb2 as dragon_pb2
import dragon.dragon_pb2_grpc as dragon_pb2_grpc


class DragonService(dragon_pb2_grpc.DragonServicer):
    """
    Dragon grpc service handlers
    """

    def StartContainer(
        self, request: dragon_pb2.StartContainerRequest, context: grpc.ServicerContext,
    ) -> dragon_pb2.Response:

        command = request.command or None
        port_mappings = request.port_mappings or {}

        if port_mappings:
            try:
                port_mappings = json.loads(port_mappings)
            except Exception as e:
                return dragon_pb2.Response(
                    status=dragon_constants.STATUS_ERROR,
                    message=json.dumps(
                        {
                            "code": "DS_INVALID_ARG",
                            "message": "Port mapping are not valid",
                            "exception": str(e),
                        }
                    ),
                )
        try:
            container_id = dragon_client.start_container(
                request.image,
                request.name,
                command=command,
                port_mappings=port_mappings,
            )
            msg = {"id": container_id}
            return dragon_pb2.Response(
                status=dragon_constants.STATUS_OK, message=json.dumps(msg)
            )
        except Exception as e:
            return dragon_pb2.Response(
                status=dragon_constants.STATUS_ERROR,
                message=json.dumps(
                    {
                        "code": "DS_START_FAILED",
                        "message": "Failed to start the container",
                        "exception": str(e),
                    }
                ),
            )

    def CommitContainer(
        self, request: dragon_pb2.CommitContainerRequest, context: grpc.ServicerContext,
    ) -> dragon_pb2.Response:

        try:
            dragon_pb2.commit_container(
                request.container_id, request.repository, request.tag
            )
        except docker.errors.NotFound as e:
            return dragon_pb2.Response(
                status=dragon_constants.STATUS_ERROR,
                message=json.dumps(
                    {
                        "code": "DS_INVALID_CONTAINER",
                        "message": "Unable to find the container to commit",
                        "exception": str(e),
                    }
                ),
            )
        except Exception as e:
            return dragon_pb2.Response(
                status=dragon_constants.STATUS_ERROR,
                message=json.dumps(
                    {
                        "code": "DS_COMMIT_FAILED",
                        "message": "Failed to commit the container",
                        "exception": str(e),
                    }
                ),
            )

        return dragon_pb2.Response(
            status=dragon_constants.STATUS_OK, message=json.dumps({})
        )

    def StopContainer(
        self, request: dragon_pb2.StopContainerRequest, context: grpc.ServicerContext
    ) -> dragon_pb2.Response:

        try:
            dragon_client.stop_container(request.container_id)
        except docker.errors.NotFound as e:
            return dragon_pb2.Response(
                status=dragon_constants.STATUS_ERROR,
                message=json.dumps(
                    {
                        "code": "DS_INVALID_CONTAINER",
                        "message": "Unable to find the container to commit",
                        "exception": str(e),
                    }
                ),
            )
        except Exception as e:
            return dragon_pb2.Response(
                status=dragon_constants.STATUS_ERROR,
                message=json.dumps(
                    {
                        "code": "DS_STOP_FAILED",
                        "message": "Failed to stop the container",
                        "exception": str(e),
                    }
                ),
            )

        return dragon_pb2.Response(
            status=dragon_constants.STATUS_OK, message=json.dumps({})
        )

    def RemoveContainer(
        self, request: dragon_pb2.RemoveContainerRequest, context: grpc.ServicerContext
    ) -> dragon_pb2.Response:

        try:
            dragon_client.remove_container(request.container_id)
        except docker.errors.NotFound as e:
            return dragon_pb2.Response(
                status=dragon_constants.STATUS_ERROR,
                message=json.dumps(
                    {
                        "code": "DS_INVALID_CONTAINER",
                        "message": "Unable to find the container to commit",
                        "exception": str(e),
                    }
                ),
            )
        except Exception as e:
            return dragon_pb2.Response(
                status=dragon_constants.STATUS_ERROR,
                message=json.dumps(
                    {
                        "code": "DS_REMOVE_FAILED",
                        "message": "Failed to stop the container",
                        "exception": str(e),
                    }
                ),
            )

        return dragon_pb2.Response(
            status=dragon_constants.STATUS_OK, message=json.dumps({})
        )

    def PingPong(
        self, request: dragon_pb2.PingPongRequest, context: grpc.ServicerContext
    ) -> dragon_pb2.PingPongResponse:
        server_address = os.environ.get("SERVER_ADDRESS", "http://localhost:8000")
        res = requests.get(f"{server_address}/api/clients/ping/")
        client_id = 0

        if res.status_code == 200:
            client_id = res.json().get("client_id")
            if request.client_id != client_id:
                logging.info("Client id mismatch on pingpong")
            else:
                logging.info(f"Pinged the server on {server_address}")

        return dragon_pb2.PingPongResponse(client_id=client_id)
