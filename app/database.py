from mongoengine import *
import configparser

db_config = configparser.ConfigParser()
db_config.read('app/app.config')

db_host = db_config.get("database", "host")
db_port = db_config.get("database", "port")
db_user = db_config.get("database", "user")
db_pass = db_config.get("database", "pass")
db_name = db_config.get("database", "name")


database = connect(db_name, username=db_user, password=db_pass, host=db_host, port=int(db_port))

def get_db():
    return database.dummy_db