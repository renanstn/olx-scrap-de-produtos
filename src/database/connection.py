from peewee import PostgresqlDatabase
from params import db_params


db = PostgresqlDatabase(
	db_params['database'],
	host = db_params['host'],
	port = int(db_params['port']),
	user = db_params['user'],
	password = db_params['password']
)
