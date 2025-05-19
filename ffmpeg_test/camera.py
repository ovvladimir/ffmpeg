import subprocess
from devices import MICROFONE, CAMERA

cmd =                                                      \
    'ffmpeg -y -loglevel error -f dshow -rtbufsize 1000M ' \
    f'-i "video={CAMERA}:audio={MICROFONE}" '           \
    '-vf scale=640:480 -vcodec libx264 -preset ultrafast ' \
    '-vf format=yuv420p test.mp4'
try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)
# CTRL + C - остановить
