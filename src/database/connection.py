from peewee import PostgresqlDatabase
from params import db_params


class DatabaseConnection:
	'''
	Classe que provê a connexão com o banco de dados
	'''

	def __init__(self, params):
		assert params['database'], 'Falta informar parâmetro "database"'
		assert params['host'], 'Falta informar parâmetro "host"'
		assert params['port'], 'Falta informar parâmetro "port"'
		assert params['user'], 'Falta informar parâmetro "user"'
		assert params['password'], 'Falta informar parâmetro "password"'

		self.params = params

	def get_connection(self):
		'''
		Retorna a conexão realizada com o banco
		'''
		connection = PostgresqlDatabase(
			self.params['database'],
			host = self.params['host'],
			port = int(self.params['port']),
			user = self.params['user'],
			password = self.params['password']
		)

		return connection

db = DatabaseConnection(db_params).get_connection()
