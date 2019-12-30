from db_functions import salvar_solicitacao, apagar_solicitacao, apagar_todos_os_anuncios
from checker import check


def welcome(update, context):
    ''' Mensagem de boas vindas do bot e instruções de uso. '''
    
    text = ("Seja bem vindo ao scrapperOLX.\n\n"
        "Cadastre um produto para ser buscado com o comando:\n /busca <nome_do_produto>\n\n"
        "Após cadastrar, buscas diárias serão feitas por este produto e eu te avisarei "
        "sempre que aparecer uma novidade.\n\nPara cancelar uma busca, use:\n /cancela <nome_do_produto>.\n\n"
        "Para fazer manualmente a busca pelos produtos cadastrados, utilize o comando:\n /scrap"
    )
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=text
    )

def cadastra_produto(update, context):
    ''' Cadastra um novo produto para ser buscado periodicamente. '''

    chat_id = update.message.chat_id
    produto = ' '.join(context.args)

    if produto:
        dados = {
            'chat_id' : chat_id,
            'produto' : produto
        }
        salvar_solicitacao(dados)
        context.bot.send_message(
            chat_id = chat_id,
            text = 'O produto "{}" foi cadastrado. Buscas periódicas serão feitas a partir de agora.'.format(produto)
        )
        db.close()

    else:
        context.bot.send_message(
            chat_id = chat_id,
            text = 'Envie após o /busca o nome do produto que deseja buscar periodicamente.'
        )

def cancela_produto(update, context):
    ''' Exclui um produto cadastrado para que não seja mas buscado. '''

    chat_id = update.message.chat_id
    produto = ' '.join(context.args)

    if produto:
        dados = {
            'chat_id' : chat_id,
            'produto' : produto
        }
        try:
            apagar_solicitacao(dados)
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
            text = 'Envie o comando, seguido do nome do produto que deseja cancelar as buscas periódicas.\n'
            'Exemplo: /cancela relógio'
        )

def run_scrap(update, context):
    ''' Executa manualmente o web scrap. '''

    chat_id = update.message.chat_id

    context.bot.send_message(
        chat_id = chat_id,
        text = 'Buscando...'
    )

    check()

    context.bot.send_message(
        chat_id = chat_id,
        text = 'Busca finalizada.'
    )
