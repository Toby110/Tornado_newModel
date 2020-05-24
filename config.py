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
class Token:
    def settoken(self):
        self.secrect=uuid.uuid4()
        self.serializer = Serializer(secret_key=str(self.secrect), expires_in=5)
        self.token = self.serializer.dumps({"id": 5, "name": "itsdangerous"}).decode()
        return self.token
    def gettoken(self,token):
        try:
            self.data = self.serializer.loads(token)
        except BadData:
            print("超时")
        else:
            print(self.data)
        

# t=Token()
# token=t.settoken()
# print(token)
