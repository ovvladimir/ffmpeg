# https://habr.com/ru/companies/flashphoner/articles/338098/
from subprocess import Popen, PIPE
# yt-dlp или youtube-dl (устарел) - в Path
# C:/Users/Lenovo/Documents/Distr/youtube
# Запуск только ᐅ

stream_id = 'ovStream1967'
destination = 'rtmp://wcs5-eu.flashphoner.com:1935/live'

url = 'https://www.youtube.com/watch?v=9cQT4urTlXM'

# 22/18 - это, если есть mp4(1280х720), а если нет - то mp4(640х360)                                -f 22/18 (если ошибка с -f best*, т.к. это может оказаться формат webm)
youtube_process = Popen(f'yt-dlp -f "" --prefer-ffmpeg --no-color --no-cache-dir --no-progress -o - -f best*[ext=mp4] {url} --reject-title {stream_id}', stdout=PIPE)
ffmpeg_process = Popen(f'ffmpeg -hide_banner -re -i - -preset ultrafast -vcodec copy -acodec copy -threads 1 -f flv {destination}/{stream_id}', stdin=youtube_process.stdout)

# Смотреть здесь:
# https://wcs5-eu.flashphoner.com/admin/demo.html или в webrtc_player

"""
youtube_process = Popen(['youtube-dl', ... '-f', '22/18', ...
"""