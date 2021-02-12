from telegram.ext import Updater, CommandHandler
from bot.actions import BotActions


class Listener:

    def __init__(self, token):
        self.token = token

    def listen(self):
        """
        Script que fica sempre em execução, aguardando comandos do bot.
        """

        updater     = Updater(token=self.token, use_context=True)
        dispatcher  = updater.dispatcher

        start_handler   = CommandHandler('start', BotActions.welcome)
        busca_handler   = CommandHandler('busca', BotActions.cadastra_produto)
        cancela_handler = CommandHandler('cancela', BotActions.cancela_produto)
        scrap_handler   = CommandHandler('scrap', BotActions.run_scrap)
        lista_handler   = CommandHandler('lista', BotActions.lista_produtos)

        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(busca_handler)
        dispatcher.add_handler(cancela_handler)
        dispatcher.add_handler(scrap_handler)
        dispatcher.add_handler(lista_handler)

        updater.start_polling()
