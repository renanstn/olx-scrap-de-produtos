from peewee import *
from models import *
from db_connection import db


db.create_tables([Anuncio, Solicitacao])

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

def salvar_anuncio(data, solicitante):
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

def get_solicitacoes():
    return Solicitacao.select()

def get_anuncios_salvos(id_solicitante):
    return Anuncio.select().where(Anuncio.solicitante == id_solicitante)
