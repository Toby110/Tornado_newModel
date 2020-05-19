import tornado.web
import config
from views import index

def make_app():
    return tornado.web.Application([
        (r'/',index.IndexHandler),
        ],**config.settings)