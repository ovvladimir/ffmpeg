from devices import CAMERA, MICROFONE
import subprocess
from time import sleep

sleep(1)

stream_id = 'ovStream1967'
destination = 'rtmp://127.0.0.1:1935/live'

# рабочая конфигурация
cmd = \
    'ffmpeg -hide_banner -rtbufsize 100M -channel_layout stereo ' \
    f'-f dshow -i "video={CAMERA}:audio={MICROFONE}" ' \
    '-c:v libx264 -b:v 1M ' \
    '-c:a aac -ac 2 -b:a 128k -ar 44100 ' \
    '-preset ultrafast -tune zerolatency ' \
    f'-f flv {destination}/{stream_id}'

try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)
