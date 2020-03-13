from database.models import *
from database.connection import db


db.create_tables([Anuncio, Solicitacao])
db.close()
