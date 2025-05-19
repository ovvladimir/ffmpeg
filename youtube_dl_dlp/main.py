# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
"""
import youtube_dl
import subprocess

url = 'https://www.youtube.com/watch?v=5RlkhQadnh4'

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# subprocess.run('ffmpeg -i Metallica_Nothing_else_matters_2.mkv -c:v libx264 -c:a aac -c:s mov_text Metallica_Nothing_else_matters_2.mp4')
"""

# https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file
# yt-dlp.exe - в Path (C:\Users\Lenovo\Documents\Distr\youtube)
from yt_dlp import YoutubeDL

urls = ['https://www.youtube.com/watch?v=5RlkhQadnh4']
with YoutubeDL() as ydl:
    ydl.download(urls)
