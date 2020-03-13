from peewee import MySQLDatabase, SqliteDatabase
from params import db_params


if db_params['type'] == 'sqlite':
	db = SqliteDatabase('database.db')

elif db_params['type'] == 'mysql':
	db = MySQLDatabase(
		db_params['database'],
		host = db_params['host'],
		port = int(db_params['port']),
		user = db_params['user'],
		password = db_params['password']
	)
