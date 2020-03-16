from peewee import *
from database.connection import db


class BaseModel(Model):
    '''
    Model base com as configurações básicas das models
    para evitar repetição de código
    '''
    class Meta:
        database = db


class Solicitacao(BaseModel):
    '''
    Model que armazena as solicitações de monitoramento
    '''
    chat_id = CharField()
    produto = CharField()


class Anuncio(BaseModel):
    '''
    Model que armazena os anúncios encontrados para cada solicitação
    '''
    titulo = CharField()
    preco = CharField()
    local = CharField()
    link = CharField()
    data_pesquisa = DateField()
    solicitante = ForeignKeyField(Solicitacao, on_delete='CASCADE')
