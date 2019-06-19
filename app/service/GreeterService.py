import generated.greeter_pb2 as greeter
import generated.greeter_pb2_grpc as greeter_grpc


class GreeterService(greeter_grpc.GreeterServicer):
    def SayGreeting(self, request, context):
        response_string = 'Valar Morghulis, %s!' % request.name
        return greeter.HelloReply(message=response_string)
