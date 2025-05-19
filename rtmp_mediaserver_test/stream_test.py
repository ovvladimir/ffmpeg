# https://developers.google.com/media/vp9/live-encoding?hl=ru
import subprocess

stream_id = 'ovStream1967'
destination = 'rtmp://127.0.0.1:1935/live'
"""
cmd = \
    'ffmpeg -hide_banner -rtbufsize 1000M -f dshow -i video="Integrated Camera" -c:v libvpx-vp9 -b:v 1M ' \
    f'-f webm -an {destination}/{stream_id}'
"""
"""
cmd = 'ffmpeg -rtbufsize 100M -f dshow -i video="Integrated Camera:audio=Микрофон (Realtek(R) Audio)" ' \
  '-r 30 -g 90 -quality realtime -speed 7 -threads 8 -row-mt 1 ' \
  '-tile-columns 3 -frame-parallel 1 -qmin 4 -qmax 48 -b:v 2800k -c:v vp9 ' \
  f'-b:a 128k -c:a libopus -f webm {destination}/{stream_id}'
"""

cmd = \
    'ffmpeg -rtbufsize 100M -f dshow -i video="Integrated Camera" ' \
    '-c:v libvpx -crf 10 -b:v 1M -quality realtime ' \
    f'-f webm -an {destination}/{stream_id}'
    # 'out.webm'

try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)
# остановить - CTRL + C
# проверить - ffplay udp://127.0.0.1:1234

# НУЖЕН НАСТРОЕННЫЙ ffserver (ffserver.conf)
'''
<Stream mystream.webm>
   Feed mystream.ffm
   Format webm
   VideoSize 640x480
   VideoCodec libvpx
   NoAudio
   AVOptionVideo flags +global_headers
</Stream>
'''