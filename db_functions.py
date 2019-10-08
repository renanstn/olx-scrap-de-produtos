from peewee import *
from models import *
from db_connection import db


#db.create_tables([Anuncio, Solicitacao])

def salvar_solicitante(data):
    solicitante = Solicitacao.create(
        chat_id = data['chat_id'],
        produto = data['produto']
    )
    return solicitante

def apagar_solicitante(data):
    para_apagar = Solicitacao.get(
        Solicitacao.chat_id == data['chat_id'],
        Solicitacao.produto == data['produto']
    )
    para_apagar.delete_instance()

def salvar_anuncio(data, id_solicitante):
    if not possui_duplicidade(data):

        anuncio = Anuncio(
            titulo          = data['titulo'],
            preco           = data['preco'],
            local           = data['local'],
            link            = data['link'],
            data_pesquisa   = data['data_pesquisa'],
            solicitante     = id_solicitante
        )

        anuncio.save()

def apagar_anuncio(anuncio):
    anuncio.delete_instance()

def possui_duplicidade(data):
    duplicados = Anuncio.select().where(Anuncio.titulo == data['titulo'])
    possui_duplicados = len(duplicados) > 0
    return possui_duplicados

def get_solicitacoes():
    solicitacoes = Solicitacao.select()
    return solicitacoes

def get_anuncios_salvos(id_solicitante):
    anuncios = Anuncio.select().where(Anuncio.solicitante == id_solicitante)
    return anuncios
