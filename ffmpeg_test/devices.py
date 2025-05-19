import subprocess

dev = subprocess.run(
    # список оборудования
    'ffmpeg -hide_banner -list_devices true -f dshow -i dummy',
    stderr=subprocess.PIPE, encoding='utf-8').stderr

index = dev[:dev.find('(video)')]
CAMERA = index[index.rfind(' "'):].strip(' " ')
index = dev[:dev.find('(audio)')]
MICROFONE = index[index.rfind(' "'):].strip(' " ')
