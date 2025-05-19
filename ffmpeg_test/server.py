import subprocess
from devices import MICROFONE, CAMERA
from time import sleep
sleep(1)
"""
cmd = \
    'ffmpeg -hide_banner -rtbufsize 100M -channel_layout stereo ' \
    f'-f dshow -i "video={CAMERA}:audio={MICROFONE}" ' \
    '-c:v libx264 -b:v 2800k -qp 0 -g 24 ' \
    '-c:a aac -ac 2 -b:a 128k -ar 44100 ' \
    '-preset ultrafast -tune zerolatency -async 1 ' \
    '-f mpegts udp://127.0.0.1:1234'
"""
"""
cmd = \
    'ffmpeg -hide_banner -rtbufsize 100M -channel_layout stereo ' \
    f'-f dshow -i "video={CAMERA}:audio={MICROFONE}" ' \
    '-c:v libaom-av1 -b:v 2M -usage realtime -row-mt 1 -cpu-used 8 ' \
    '-c:a libopus -b:a 128k ' \
    '-f flv udp://127.0.0.1:1234'
"""
"""
cmd = \
    'ffmpeg -hide_banner -rtbufsize 100M -channel_layout stereo ' \
    f'-f dshow -i "video={CAMERA}:audio={MICROFONE}" ' \
    '-c:v libaom-av1 -b:v 2M -usage realtime -row-mt 1 -cpu-used 8 ' \
    '-c:a libopus -b:a 128k ' \
    '-strict experimental ' \
    '-f rtsp -rtsp_transport tcp rtsp://127.0.0.1:1234/live.sdp'
"""
"""
cmd = \
    'ffmpeg -hide_banner -rtbufsize 100M -channel_layout stereo ' \
    f'-f dshow -i "video={CAMERA}:audio={MICROFONE}" ' \
    '-c:v libx264 -b:v 2800k -qp 0 ' \
    '-c:a aac -ac 2 -b:a 128k -ar 44100 ' \
    '-preset ultrafast -tune zerolatency ' \
    '-f rtsp -rtsp_transport tcp rtsp://127.0.0.1:1234/live.sdp'
"""
# наименьшая задержка
cmd = \
    'ffmpeg -hide_banner -rtbufsize 100M ' \
    f'-f dshow -i "video={CAMERA}" ' \
    '-c:v libvpx -crf 10 -b:v 1M -quality realtime ' \
    '-f webm -an udp://127.0.0.1:1234'
# со звуком убрать -an и использовать -c:a libopus для webm
"""
# new
cmd = \
    'ffmpeg -hide_banner -rtbufsize 100M ' \
    f'-f dshow -i "video={CAMERA}" ' \
    '-c:v libvpx-vp9 -crf 30 -b:v 0 -cpu-used 8 -quality realtime ' \
    '-f webm -an udp://127.0.0.1:1234'
"""
try:
    subprocess.run(cmd)
except BaseException as e:
    print(e)

'CTRL + C - остановить'

# для -vcodec (-c:v) libx264 -preset ultrafast -tune zerolatency или -vcodec h264_qsv
# еще опции: -cpu-used -5 -deadline realtime -vf "scale=w=trunc(oh*a/2)*2:h=720 -pix_fmt yuv420p"
# -f dash dash.mpd -> воспроизводится index2.html, но работает с прерываниями и создается куча файлов
# -strict experimental - т.к. av1 пока экспериментальный, нужно для rtsp

'ffplay udp://127.0.0.1:1234'
'ffplay -probesize 32 -sync ext udp://127.0.0.1:1234' # уменьшает задержку плеера (не для av1), но выдает несущественную ошибку
'ffplay -rtsp_flags listen rtsp://127.0.0.1:1234/live.sdp?tcp'
