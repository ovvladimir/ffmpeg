# https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/
# $ scp client.py pi@192.168.1.10:~
# python client.py -s 192.168.100.10
# python client.py -s 127.0.0.1   -> 127.0.0.2, 127.0.0.3 ...
# ipconfig # ip r l
'python client.py'

from usbcamvideostream import USBCamVideoStream
import imagezmq
import argparse
import socket
import time
import msvcrt

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-s", "--server-ip", default="127.0.0.1",  # required=True,
    help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())
# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to=f'tcp://{args["server_ip"]}:5555')

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpiName = socket.gethostname()
# vs = USBCamVideoStream(usePiCamera=True).start()
vs = USBCamVideoStream(src=0).start()
time.sleep(1.0)

while True:
    # read the frame from the camera and send it to the server
    frame = vs.retrieves()
    sender.send_image(rpiName, frame)

    if msvcrt.kbhit():
        key = ord(msvcrt.getch())
        if key == 27:
            print('Выход')
            break
