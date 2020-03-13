from models import *
from db_connection import db


db.create_tables([Anuncio, Solicitacao])
db.close()
