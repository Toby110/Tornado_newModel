import tornado.web
from model import model
import datetime
import json
import config
import time

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")
    
    def post(self):
        data=json.loads(self.request.body)
        if data['user']=='tom' and data['psw']=='123456':
            model.Token.create_table()
            t = config.Token(data['user'],data['psw'])
            mytoken = t.settoken()
            try:
                token = model.Token(token=mytoken, username=data["user"], password=data["psw"])
            except :
                self.write("token超时")
            else:
                token.save()
                self.set_header("token",mytoken)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
                
            
        
