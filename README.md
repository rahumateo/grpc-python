# grpc-python
GRPC implementation (server and client) using Python.

A part of grpc implementations:
- java: https://github.com/rahumateo/grpc-java
- python: https://github.com/rahumateo/grpc-python

Note that as gRPC supports multi-language, you can run the server on one language and the client on the other.
For more info, read on https://grpc.io/.


For this example, there are two functionalities:
1. Greetings. A simple function as seen in many tutorials for grpc
2. A Flickr public photo feed. A (little bit more) complex functionality (in server side). Does not really matter in terms of `grpc` example, but it pretty much gives an idea about how it might work and the usage in "real" project.
   To use this, you have to have `API_KEY` and `SECRET_KEY` from *Flickr*. See https://www.flickr.com/services/api/ in (API Keys) for more info.
   Put the keys in `/component/FlickrConfig`
   

Server
```
app/app_server.py
```


Client
```
app/app_client.py
```
