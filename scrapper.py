import re
from datetime import date
from requests import get
from bs4 import BeautifulSoup
from store import *

produto_buscado = 'bittboy'

url = 'https://sp.olx.com.br/grande-campinas?q={}'.format(produto_buscado)

# Regex que remove os \n, \r e \t dos textos
regex = re.compile('[\n\r\t]')

html = get(url)

soup = BeautifulSoup(html.text, 'html.parser')

lista_resultados = soup.find('ul', id='main-ad-list')
itens = lista_resultados.find_all('li')

itens_encontrados = []

for item in itens:
    if item.has_attr('data-list_id'):
        link = item.find('a')
        # Titulo do produto
        obj_titulo = link.find('h2', class_='OLXad-list-title')
        titulo = regex.sub('', obj_titulo.text)
        # Preço do produto
        obj_preco = link.find('p', class_='OLXad-list-price')
        preco = regex.sub('', obj_preco.text)
        # Local do vendedor
        obj_local = link.find('p', class_='text detail-region')
        local = regex.sub('', obj_local.text)

        itens_encontrados.append({
            'titulo' : titulo,
            'preco' : preco,
            'local' : local,
            'data_pesquisa' : date.today()
        })

# Salvar no banco de dados
for item in itens_encontrados:
    salvar_dados(item)
