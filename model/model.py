from peewee import *

db = SqliteDatabase('./model/people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db 
        