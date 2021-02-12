from database.functions import DatabaseFunctions
from scrapper import web_scrap
from telegram import Bot
from params import token


def check():
    """
    Função principal, que, a partir das solicitações cadastradas, faz o web scrap,
    identifica novos anúncios, apaga anúncios finalizados, e envia a mensagem pelo bot
    notificando o usuário.
    Este script deve ser chamado periodicamente.
    """

    bot = Bot(token=token)

    solicitacoes = DatabaseFunctions.get_solicitacoes()

    for solicitacao in solicitacoes:
        # Trocar os espaços por + para construir a URL corretamente
        produto = solicitacao.produto.replace(' ', '+')

        anuncios_salvos = DatabaseFunctions.get_anuncios_salvos(solicitacao.id)

        anuncios_encontrados = web_scrap(produto)

        titulos_produtos_salvos = [i.titulo for i in anuncios_salvos]
        titulos_anuncios_encontrados = [i['titulo'] for i in anuncios_encontrados]

        novos_anuncios = [x for x in anuncios_encontrados if x['titulo'] not in titulos_produtos_salvos]
        anuncios_apagados = [x for x in anuncios_salvos if x.titulo not in titulos_anuncios_encontrados]

        # Remover anúncios que não existem mais
        for anuncio in anuncios_apagados:
            DatabaseFunctions.apagar_anuncio(anuncio)

        # Salvar novos anúncios no banco e enviar notificações
        for anuncio in novos_anuncios:
            DatabaseFunctions.salvar_anuncio(anuncio, solicitacao.id)

            mensagem = "Novo produto encontrado:\n\n- {}\n- Valor: R$ {:.2f}\n- Local: {}\n- Link: {}\n".format(
                anuncio['titulo'],
                int(anuncio['preco']),
                anuncio['local'],
                anuncio['link']
            )

            bot.send_message(solicitacao.chat_id, mensagem)


if __name__ == '__main__':
    check()
