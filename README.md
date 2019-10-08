# olx-scrap-de-produtos

### @OlxScrapperBot

Script feito para facilitar a vida de quem busca diariamente itens específicos no OLX.

- Ele identifica os itens encontrados e extrai o título do produto, valor, e localidade do vendedor.
- Salva os anuncios encontrados no banco de dados.
- Identifica se algum destes anúncios é novo, ou seja, se ele **não** existia na busca realizada anteriormente.
- Caso seja um anúncio **novo** detectado pelo item acima, um bot no Telegram irá te avisar que uma nova pessoa anunciou o produto em questão.

Atualmente utilizo o **Beautiful Soup** para fazer o web scrap e o **Peewee** para manipular o banco.

Screenshots:

<img src="https://github.com/Doc-McCoy/olx-scrap-de-produtos/blob/master/screenshots/screenshot_01.jpg" width="360" height="640"/>

<img src="https://github.com/Doc-McCoy/olx-scrap-de-produtos/blob/master/screenshots/screenshot_02.jpg" width="360" height="640"/>
