import configparser, telegram
from scrapper import *
from db_functions import *

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    token = config['bot']['token']
    bot = telegram.Bot(token=token)

    produto_buscado = 'bittboy'

    # Fazer o web_scrap
    anuncios_encontrados = web_scrap(produto_buscado)

    # Listar os anuncios salvos anteriormente
    anuncios_salvos = get_anuncios_salvos()

    # Comparar se teve anuncios novos
    if len(anuncios_encontrados) != len(anuncios_salvos):
        print('Tem anúncio novo!')

    # Salvar no banco de dados
    for item in anuncios_encontrados:
        salvar_dados(item)

    for anuncio in get_anuncios_salvos():
        print(anuncio.titulo)

if __name__ == '__main__':
    main()
