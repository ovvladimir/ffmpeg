from flask import Flask
from waitress import serve
import webbrowser

app = Flask(__name__)
host, port = '127.0.0.1', 1234


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


if __name__ == '__main__':
    webbrowser.open(f'http://{host}:{port}/', new=2, autoraise=True)
    serve(app, host=host, port=port)
    # app.run(host=host, port=port)
    # curl localhost:1234

# pip install gevent
# from gevent.pywsgi import WSGIServer
# http_server = WSGIServer((host, port), app)
# http_server.serve_forever()
