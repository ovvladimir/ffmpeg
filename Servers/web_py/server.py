# https://webpy.org/docs/0.3/tutorial
# https://iximiuz.com/ru/posts/over-9000-ways-to-make-web-server-in-python/
# https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/
# python server.py 1234
import web

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        return "Hello, world!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
