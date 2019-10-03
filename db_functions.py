from peewee import *
from models import *
from db_connection import db


db.create_tables([Anuncio, Solicitacao])

def salvar_dados_solicitante(data):
    solicitante = Solicitacao.create(
        chat_id = data['chat_id'],
        produto = data['produto']
    )

    return solicitante

def salvar_dados_anuncio(data, solicitante):
    if not possui_duplicidade(data):

        anuncio = Anuncio(
            titulo = data['titulo'],
            preco = data['preco'],
            local = data['local'],
            data_pesquisa = data['data_pesquisa'],
            solicitante = solicitante
        )

        anuncio.save()

def possui_duplicidade(data):
    duplicados = Anuncio.select().where(Anuncio.titulo == data['titulo'])
    return len(duplicados) > 0

def get_anuncios_salvos():
    return Anuncio.select()
