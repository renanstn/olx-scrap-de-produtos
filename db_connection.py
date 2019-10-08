from peewee import MySQLDatabase #, SqliteDatabase
from params import db_params


# db = SqliteDatabase('database.db')
db = MySQLDatabase(
    db_params['database'],
    host = db_params['host'],
    port = int(db_params['port']),
    user = db_params['user'],
    password = db_params['password']
)
