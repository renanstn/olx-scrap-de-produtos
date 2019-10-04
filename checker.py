from db_functions import get_anuncios_salvos, get_solicitacoes
from scrapper import web_scrap


# Acessar os produtor que precisam ser buscados:
solicitacoes = get_solicitacoes()

for i in solicitacoes:
    produto = i.produto
    anuncios_salvos = get_anuncios_salvos(i.id)
    teste = [i.titulo for i in anuncios_salvos]
    print(teste)

    anuncios = web_scrap(produto)
    teste2 = [i['titulo'] for i in anuncios]
    print(teste2)



# Fazer o web scrap

# Verificar resulados com os já existentes

# Caso haja diferença, enviar a mensagem pelo bot

# Fazer o web_scrap
# anuncios_encontrados = web_scrap(produto_buscado)

# Listar os anuncios salvos anteriormente
# anuncios_salvos = get_anuncios_salvos()

# Comparar se teve anuncios novos
# if len(anuncios_encontrados) != len(anuncios_salvos):
#     print('Tem anúncio novo!')

# Salvar no banco de dados
# for item in anuncios_encontrados:
#     salvar_dados(item)