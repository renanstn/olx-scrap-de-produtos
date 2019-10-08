from peewee import *
from db_connection import db


class Solicitacao(Model):

    chat_id = CharField()
    produto = CharField()

    class Meta():
        database = db


class Anuncio(Model):

    titulo = CharField()
    preco = CharField()
    local = CharField()
    link = CharField()
    data_pesquisa = DateField()
    solicitante = ForeignKeyField(Solicitacao)

    class Meta:
        database = db
