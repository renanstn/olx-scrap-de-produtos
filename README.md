# olx-scrap-de-produtos [projeto deprecado]

--------------------

Bot desenvolvido para facilitar a vida de quem busca diariamente itens específicos no OLX.

- Ele identifica os itens encontrados e extrai o título do produto, valor, e localidade do vendedor.
- Salva os anuncios encontrados no banco de dados.
- Identifica se algum destes anúncios é novo.
- Caso seja um anúncio **novo** detectado pelo item acima, um bot no Telegram irá te avisar que uma nova pessoa anunciou o produto em questão.

Atualmente utilizo o **Beautiful Soup** para fazer o web scrap e o **Peewee** para manipular o banco.

Screenshots:

<img src="https://github.com/Doc-McCoy/olx-scrap-de-produtos/blob/master/screenshots/screenshot_01.jpg" width="360" height="640"/>

<img src="https://github.com/Doc-McCoy/olx-scrap-de-produtos/blob/master/screenshots/screenshot_02.jpg" width="360" height="640"/>

-------------------------------

## Como utilizar o bot
- Para utilizar somente o bot pronto, basta acessá-lo [neste link](https://t.me/OlxScrapperBot) e começar a cadastrar seus produtos com o comando `/busca <nome_do_produto>`

## Como fazer seu próprio bot
Caso queira subir seu próprio servidor e criar seu próprio bot, siga os passos:

- Crie um bot no telegram [clique aqui caso não saiba como](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
- Clone o projeto
- Inicialize um ambiente virtual com o comando: `python -m venv venv`
- Ative o ambiente virtual com: `source venv/bin/activate`
- Instale as dependências: `pip install -r requirements.txt`
- Crie um arquivo chamado `config.ini` na raíz do projeto, e coloque nele o token do seu bot e as configurações do banco de dados seguindo o modelo:

![config.ini](https://github.com/Doc-McCoy/olx-scrap-de-produtos/blob/master/screenshots/config.png)

- Inicialize o banco de dados com o comando `python initialize_db.py`
- Para manter o código sempre "escutando", mantenha sempre executando o arquivo: `python listener.py`
- Para procurar pelos produtos cadastrados, rode o arquivo: `python checker.py` (geralmente programo uma cron para rodar este comando todos os dias automaticamente)

-------------------------------

#### TODO:
- Organizar estrutura de arquivos e pastas pois está uma zona
