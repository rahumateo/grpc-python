from concurrent import futures
import time
import logging

import grpc

import generated.greeter_pb2_grpc as greeter_grpc
import generated.photofeed_pb2_grpc as photo_feed_grpc

from service.GreeterService import GreeterService
from service.PhotoFeedService import PhotoFeedService

_ONE_DAY = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    greeter_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    photo_feed_grpc.add_PhotoServiceServicer_to_server(PhotoFeedService(), server)

    server.add_insecure_port('localhost:50051')
    server.start()
    print('Server started, listening on 50051')
    try:
        while True:
            time.sleep(_ONE_DAY)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
