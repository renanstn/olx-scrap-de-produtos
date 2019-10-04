from telegram.ext import Updater, CommandHandler
from params import token
from db_functions import salvar_solicitante, apagar_solicitante

def listener():
    updater     = Updater(token=token, use_context=True)
    dispatcher  = updater.dispatcher

    def start(update, context):
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text='Seja bem vindo ao WebScrapper OLX'
        )

    def busca(update, context):
        chat_id = update.message.chat_id
        produto = ' '.join(context.args)
        if produto:
            dados = {
                'chat_id' : chat_id,
                'produto' : produto
            }
            salvar_solicitante(dados)
            context.bot.send_message(
                chat_id = chat_id,
                text = 'O produto "{}" foi cadastrado. Buscas periódicas serão feitas a partir de agora.'.format(produto)
            )
        else:
            context.bot.send_message(
                chat_id = chat_id,
                text = 'Envie após o /busca o nome do produto que deseja buscar periodicamente.'
            )

    def cancela(update, context):
        chat_id = update.message.chat_id
        produto = ' '.join(context.args)
        if produto:
            dados = {
                'chat_id' : chat_id,
                'produto' : produto
            }
            try:
                apagar_solicitante(dados)
                context.bot.send_message(
                    chat_id = chat_id,
                    text = 'O produto "{}" foi excluído da sua lista de buscas periódicas.'.format(produto)
                )
            except:
                context.bot.send_message(
                    chat_id = chat_id,
                    text = 'Não foi encontrado produto com este nome na sua lista de cadastros.'
                )
        else:
            context.bot.send_message(
                chat_id = chat_id,
                text = 'Envie o nome do produto que deseja cancelar as buscas periódicas.'
            )


    start_handler   = CommandHandler('start', start)
    busca_handler   = CommandHandler('busca', busca)
    cancela_handler = CommandHandler('cancela', cancela)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(busca_handler)
    dispatcher.add_handler(cancela_handler)

    updater.start_polling()


if __name__ == '__main__':
    listener()
