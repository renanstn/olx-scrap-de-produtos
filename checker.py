

# Fazer o web scrap

# Verificar resulados com os já existentes

# Caso haja diferença, enviar a mensagem pelo bot

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