import tornado.web
from model import model
import datetime
import json

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        model.Person.create_table()
        book=model.Person(name='lily',birthday=datetime.date(2018,1,6))
        book.save()
        model.User.create_table()
        user=model.User(username='tom',password=123456)
        user.save()
        data = [{"name": "lily", "age" :18}, {"name": "lily", "age" :18}, {"name": "lily", "age" :18}]
        self.write(json.dumps(data))
        
