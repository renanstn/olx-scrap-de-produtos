from db_functions import get_anuncios_salvos, get_solicitacoes, apagar_anuncio, salvar_anuncio
from scrapper import web_scrap
from telegram import Bot
from params import token


bot = Bot(token=token)

# Acessar os produtor que precisam ser buscados:
solicitacoes = get_solicitacoes()

for solicitacao in solicitacoes:
    produto = solicitacao.produto
    anuncios_salvos = get_anuncios_salvos(solicitacao.id)

    anuncios_encontrados = web_scrap(produto)

    titulos_produtos_salvos = [i.titulo for i in anuncios_salvos]
    titulos_anuncios_encontrados = [i['titulo'] for i in anuncios_encontrados]

    novos_anuncios = [x for x in anuncios_encontrados if x['titulo'] not in titulos_produtos_salvos]
    anuncios_apagados = [x for x in anuncios_salvos if x not in titulos_anuncios_encontrados]

    # Apagar anuncios que não existem mais
    for anuncio in anuncios_apagados:
        apagar_anuncio(anuncio)
    
    # Salvar novos anúncios no banco e enviar notificações
    for anuncio in novos_anuncios:
        salvar_anuncio(anuncio, solicitacao.id)
        mensagem = "Insira aqui a mensagem de produto encontrado."
        bot.send_message(solicitacao.chat_id, mensagem)
