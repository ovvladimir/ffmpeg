"""
# Звук в виртуалку
pactl load-module module-null-sink sink_name=remote - ищет имя источника звука (remote.monitor)
ffmpeg -f pulse -i "remote.monitor" -ac 2 -acodec libmp3lame -ar 44100 -ab 128000 -f rtp rtp://168.254.171.209:18181
ffplay -nodisp rtp://0.0.0.0:18181
"""

"""
ffmpeg -list_devices true -f dshow -i dummy

[dshow @ 0000021250860b40] "Integrated Camera" (video)
[dshow @ 0000021250860b40]   Alternative name "@device_pnp_\\?\usb#vid_30c9&pid\global"
[dshow @ 0000021250860b40] "Микрофон (Realtek(R) Audio)" (audio)
[dshow @ 0000021250860b40]   Alternative name "@device_cm_{33D9A7}"
"""

# # subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
#  python -m http.server 1234 --bind 127.0.0.1