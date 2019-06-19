import logging
import grpc

import generated.greeter_pb2 as greeter
import generated.greeter_pb2_grpc as greeter_grpc
import generated.photofeed_pb2 as photo_feed
import generated.photofeed_pb2_grpc as photo_feed_grpc


def run_greeter():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_grpc.GreeterStub(channel)
        request = greeter.HelloRequest(name='Jon Snow')
        response = stub.SayGreeting(request)
    print("Greeter client received: " + response.message)


def run_photo_search():
    tags = "dogs"

    print("Searching photos for: " + tags)
    request = photo_feed.PhotoSearchRequest(tags=tags)

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = photo_feed_grpc.PhotoServiceStub(channel)
        response = stub.GetPublicPhotos(request)
    print("Got " + str(len(response.photos)) + " for tags: " + response.title)
    for photo in response.photos:
        print('title: ' + photo.title)


if __name__ == '__main__':
    logging.basicConfig()
    run_greeter()
    run_photo_search()
