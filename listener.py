from telegram.ext import Updater, CommandHandler
from params import token
from bot_functions import welcome, cadastra_produto, cancela_produto, run_scrap
from db_connection import db


def listener():
    ''' Script que fica sempre em execução, aguardando comandos do bot. '''

    updater     = Updater(token=token, use_context=True)
    dispatcher  = updater.dispatcher

    start_handler   = CommandHandler('start', welcome)
    busca_handler   = CommandHandler('busca', cadastra_produto)
    cancela_handler = CommandHandler('cancela', cancela_produto)
    scrap_handler   = CommandHandler('scrap', run_scrap)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(busca_handler)
    dispatcher.add_handler(cancela_handler)
    dispatcher.add_handler(scrap_handler)

    updater.start_polling()


if __name__ == '__main__':
    listener()
    db.close()
