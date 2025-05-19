from devices import CAMERA, MICROFONE
import subprocess
from time import sleep

sleep(1)

# рабочая конфигурация
cmd = \
    'ffmpeg -hide_banner -rtbufsize 100M -channel_layout stereo ' \
    f'-f dshow -i "video={CAMERA}:audio={MICROFONE}" ' \
    '-c:v libx264 -b:v 1M ' \
    '-x264-params keyint=15:min-keyint=15 ' \
    '-c:a aac -ac 2 -b:a 128k -ar 44100 ' \
    '-preset ultrafast -tune zerolatency ' \
    '-flags -global_header -fflags flush_packets -http_persistent 1 ' \
    '-hls_time 6 -hls_list_size 2 -hls_delete_threshold 2 -hls_flags delete_segments ' \
    '-f hls master.m3u8'

try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)

"""
ffmpeg -rtsp_transport tcp -i rtsp://LOGIN:PASS@IP:554 -ar 44100 -acodec aac -ac 1 
-strict -2 -crf 18 -c:v copy -preset ultrafast -flags -global_header -fflags flush_packets 
-tune zerolatency -hls_time 5 -hls_list_size 2 -hls_wrap 2 -hls_delete_threshold 2 
-hls_flags delete_segments -start_number 0 /var/www/html/rtsp/index.m3u8 > /dev/null 2>&1 < /dev/null

>> /dev/null - перенаправление stdout в /dev/null
2>&1 - перенаправление stderr в stdout (который пойдет в /dev/null)
в windows - > NUL
"""