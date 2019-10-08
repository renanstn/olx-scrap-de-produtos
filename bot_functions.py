from db_functions import salvar_solicitante, apagar_solicitante


def start(update, context):
    ''' Mensagem de boas vindas do bot e instruções de uso. '''
    
    text = ("Seja bem vindo ao scrapperOLX.\n\n"
        "Cadastre um produto para ser buscado com o comando:\n /busca <nome_do_produto>\n\n"
        "Após cadastrar, buscas diárias serão feitas por este produto e eu te avisarei "
        "sempre que aparecer uma novidade.\n\nPara cancelar uma busca, use:\n /cancelar <nome_do_produto>.\n\n"
    )
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=text
    )

def busca(update, context):
    ''' Cadastra um novo produto para ser buscado periodicamente. '''

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
        db.close()

    else:
        context.bot.send_message(
            chat_id = chat_id,
            text = 'Envie após o /busca o nome do produto que deseja buscar periodicamente.'
        )

def cancela(update, context):
    ''' Exclui um produto cadastrado para que não seja mas buscado. '''

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
