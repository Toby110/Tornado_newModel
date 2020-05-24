from peewee import *

db = SqliteDatabase('./model/people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    class Meta:
        database = db 
class User(Model):
    username=CharField()
    password=IntegerField()
    class Meta:
        database = db

        
