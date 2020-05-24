import tornado.web
import config
from views import view

def make_app():
    return tornado.web.Application([
        (r'/',view.LoginHandler),
        (r'/index/', view.IndexHandler),
        ],**config.settings)
