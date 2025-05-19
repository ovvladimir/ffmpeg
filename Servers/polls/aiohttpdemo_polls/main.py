from aiohttp import web

from settings import config
from routes import setup_routes

app = web.Application()
setup_routes(app)
app['config'] = config
web.run_app(app)  # , host='127.0.0.1', port=1234)
