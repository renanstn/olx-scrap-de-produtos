from peewee import *
from db_connection import db

class Anuncio(Model):

    titulo = CharField()
    preco = CharField()
    local = CharField()
    data_pesquisa = DateField()

    class Meta:
        database = db
