# pip install git+https://github.com/kinshuk-h/pytube
import os
import time
from pytube import YouTube as YT
from pytube.cli import on_progress

print('\n[INFO] Press Enter to convert from mkv to mp4')
url = input('Download URL: ')

path = os.path.dirname(os.path.abspath(__file__))
path_in = os.path.join(path, 'in')
path_out = os.path.join(path, 'out')
symbols = '-=/:*?<>+%!()@|[]&,^$# '
os.chdir(path_in)


def converter(file_download):
    file_in = file_download
    for symbol in symbols:
        file_in = file_in.replace(symbol, '_')
    if file_in != file_download:
        os.rename(file_download, file_in)
    file_out = f"{file_in[:file_in.index('.')]}.mp4"
    print('[INFO]', file_in, file_out, '[END INFO]', sep='\n')
    os.system(f"ffmpeg -i {file_in} {os.path.join(path_out, file_out)}")


if url != '':  # not Enter
    try:
        YT(url, on_progress_callback=on_progress).streams.get_highest_resolution().download(path_in)
        # print(YT(url).streams)
        # print(YT(url).streams.filter(subtype='mp4', progressive=True).all())
    except Exception as e:
        print('[ERROR]', e)
    else:
        time.sleep(3)
        print('\n')
        file_download = os.listdir(path_in)[0]
        if file_download[file_download.index('.'):] == '.mkv':
            converter(file_download)
else:
    for file_download in os.listdir(path_in):
        converter(file_download)
        time.sleep(3)

# os.system('pause')
input("[EXIT] Press Enter to close")

# from os import path
# print(path.splitext(file_name)[0])
