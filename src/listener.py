from telegram.ext import Updater, CommandHandler
from params import token
from bot.bot_functions import welcome, cadastra_produto, cancela_produto, run_scrap, lista_produtos
from database.connection import db
from database.models import *
from database.connection import db


def listener():
    ''' Script que fica sempre em execução, aguardando comandos do bot. '''

    updater     = Updater(token=token, use_context=True)
    dispatcher  = updater.dispatcher

    start_handler   = CommandHandler('start', welcome)
    busca_handler   = CommandHandler('busca', cadastra_produto)
    cancela_handler = CommandHandler('cancela', cancela_produto)
    scrap_handler   = CommandHandler('scrap', run_scrap)
    lista_handler   = CommandHandler('lista', lista_produtos)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(busca_handler)
    dispatcher.add_handler(cancela_handler)
    dispatcher.add_handler(scrap_handler)
    dispatcher.add_handler(lista_handler)

    updater.start_polling()


if __name__ == '__main__':
    db.create_tables([Anuncio, Solicitacao])
    db.close()

    print('listening pra caralho...')
    listener()
    db.close()
