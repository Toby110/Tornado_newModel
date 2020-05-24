import itsdangerous
import uuid
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadData
settings={
    'template_path':'template',
    'static_path':'static',
    'debug':True,
}
options={
    "port":8000,
}
class Token():
    def __init__(self, user, psw):
        self.user=user
        self.psw=psw
        self.secrect = "mymarry"
        self.serializer = Serializer(secret_key=self.secrect, expires_in=50)   
    def settoken(self):
        self.token = self.serializer.dumps({"username": self.user, "password": self.psw}).decode()
        return self.token
    def gettoken(self,token):
        try:
            self.data = self.serializer.loads(token)
        except BadData:
            print("超时")
        else:
            return self.data
        
