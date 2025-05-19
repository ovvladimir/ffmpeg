# требуется nodejs для token
# можно почитать - https://habr.com/ru/articles/871202/

from pytubefix import YouTube
from pytubefix.cli import on_progress

# url = "https://www.youtube.com/"
url = "https://www.youtube.com/watch?v=m47wMt-JTNE&t=1611s"

yt = YouTube(url, 'WEB', on_progress_callback=on_progress)
print(f'\n{yt.title}\n')

ys = yt.streams.get_highest_resolution()
# yt.streams.get_lowest_resolution() -> худшее качество или yt.streams.get_highest_resolution() -> лучшее качество
# yt.streams.filter(type='video').order_by('resolution').desc().first() -> webm
ys.download()
