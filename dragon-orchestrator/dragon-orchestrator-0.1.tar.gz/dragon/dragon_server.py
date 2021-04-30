import logging
from concurrent import futures

import grpc

import dragon.dragon_pb2_grpc as dragon_pb2_grpc
import dragon.dragon_services as dragon_services


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dragon_pb2_grpc.add_DragonServicer_to_server(
        dragon_services.DragonService(), server
    )
    server.add_insecure_port("[::]:50051")
    logging.info("Client listening on port 50051")
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s - %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    serve()
