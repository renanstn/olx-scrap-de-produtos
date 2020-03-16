from params import token
from database.connection import db
from database.models import Anuncio, Solicitacao
from listener import Listener


def create_models():
    '''
    Cria as models necessárias para o funcionamento do app.
    '''
    db.create_tables([Anuncio, Solicitacao])
    db.close()

def main():
    create_models()

    listener = Listener(token)
    listener.listen()
    db.close()


if __name__ == "__main__":
    main()
