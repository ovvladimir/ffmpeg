import urllib.request as urllib
import webbrowser

# 1
link = "http://127.0.0.1:1234"
f = urllib.urlopen(link)
result = f.read().decode('utf-8')
print(result)

# 2
webbrowser.open(link)
