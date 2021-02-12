from peewee import *
from database.models import *
from database.connection import db


class DatabaseFunctions:
    '''
    Funções básicas que envolvam interações com o banco de dados
    '''

    @staticmethod
    def salvar_solicitacao(data):
        solicitante = Solicitacao.create(
            chat_id = data['chat_id'],
            produto = data['produto']
        )
        return solicitante

    @staticmethod
    def apagar_solicitacao(data):
        solicitacao_para_apagar = Solicitacao.get(
            Solicitacao.chat_id == data['chat_id'],
            Solicitacao.produto == data['produto']
        )
        # DatabaseFunctions.apagar_todos_os_anuncios(solicitacao_para_apagar)
        solicitacao_para_apagar.delete_instance()

    @staticmethod
    def salvar_anuncio(data, id_solicitante):
        if not DatabaseFunctions.possui_duplicidade(data):

            anuncio = Anuncio(
                titulo          = data['titulo'],
                preco           = data['preco'],
                local           = data['local'],
                link            = data['link'],
                data_pesquisa   = data['data_pesquisa'],
                solicitante     = id_solicitante
            )

            anuncio.save()

    @staticmethod
    def apagar_anuncio(anuncio):
        anuncio.delete_instance()

    # @staticmethod
    # def apagar_todos_os_anuncios(solicitante):
    #     Anuncio.delete().where(Anuncio.solicitante == solicitante).execute()

    @staticmethod
    def possui_duplicidade(data):
        duplicados = Anuncio.select().where(Anuncio.titulo == data['titulo'])
        possui_duplicados = len(duplicados) > 0
        return possui_duplicados

    @staticmethod
    def get_solicitacoes():
        solicitacoes = Solicitacao.select()
        return solicitacoes

    @staticmethod
    def get_solicitacoes_usuario(id_solicitante):
        solicitacoes = Solicitacao.select(Solicitacao.produto).where(Solicitacao.chat_id == id_solicitante)
        return solicitacoes

    @staticmethod
    def get_anuncios_salvos(id_solicitante):
        anuncios = Anuncio.select().where(Anuncio.solicitante == id_solicitante)
        return anuncios

    @staticmethod
    def verifica_produto_duplicado(nome_produto):
        produto_existente = Solicitacao.select().where(Solicitacao.produto == nome_produto)
        return len(produto_existente) > 0
