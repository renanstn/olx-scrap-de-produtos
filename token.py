import configparser

config = configparser.ConfigParser()
config.read('config.ini')

token = config['bot']['token']
