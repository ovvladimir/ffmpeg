import subprocess

cmd = \
    f'ffmpeg -re -rtbufsize 2000M -f dshow -i video="Integrated Camera" ' \
    '-vcodec h264_qsv -b:v 8000k -vf "scale=w=trunc(oh*a/2)*2:h=720" ' \
    '-f mpegts zmq:tcp://127.0.0.1:5555'

try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)
# CTRL + C - остановить

# В cmd:
# ffplay zmq:tcp://127.0.0.1:5555
# ffplay -autoexit -nodisp zmq:tcp://127.0.0.1:5555