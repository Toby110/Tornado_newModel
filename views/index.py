import tornado.web
from model import model
import datetime

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        model.Person.create_table()
        book=model.Person(name='lily',birthday=datetime.date(2018,1,6))
        book.save()
        