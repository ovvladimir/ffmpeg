import subprocess
from devices import MICROFONE

cmd =                                                                       \
    'ffmpeg -y -loglevel error -rtbufsize 100M -f dshow '                   \
    f'-i audio="{MICROFONE}" '                                              \
    '-f gdigrab -framerate 30 -probesize 10M -draw_mouse 1 '                \
    '-i desktop -vcodec libx264 -preset ultrafast -pix_fmt yuv420p test.mp4'

try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)
# CTRL + C - остановить
