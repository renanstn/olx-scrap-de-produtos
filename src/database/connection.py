from peewee import PostgresqlDatabase


class DatabaseConnection:
	def __init__(self, params):
		assert params['database'], 'Falta informar parâmetro "database"'
		assert params['host'], 'Falta informar parâmetro "host"'
		assert params['port'], 'Falta informar parâmetro "port"'
		assert params['user'], 'Falta informar parâmetro "user"'
		assert params['password'], 'Falta informar parâmetro "password"'

		self.params = params

	def get_connection(self):
		conn = PostgresqlDatabase(
			self.params['database'],
			host = self.params['host'],
			port = int(self.params['port']),
			user = self.params['user'],
			password = self.params['password']
		)

		return conn
