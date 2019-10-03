from peewee import *
from models import Anuncio
from db_connection import db


db.create_tables([Anuncio])

def salvar_dados(data):
    if not possui_duplicidade(data):

        anuncio = Anuncio(
            titulo = data['titulo'],
            preco = data['preco'],
            local = data['local'],
            data_pesquisa = data['data_pesquisa']
        )

        anuncio.save()

def possui_duplicidade(data):
    duplicados = Anuncio.select().where(Anuncio.titulo == data['titulo'])
    return len(duplicados) > 0

def get_anuncios_salvos():
    return Anuncio.select()
