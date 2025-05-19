# https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/client_server.html
import zmq
import time
from multiprocessing import Process

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")
for request in range(20):
    print("Sending request ", request, "...")
    socket.send_string("Parsed_overlay_2 x 200")
    message = socket.recv()
    print("Received reply ", request, "[", message, "]")
    time.sleep(1)
