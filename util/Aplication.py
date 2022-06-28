from flask import Flask
from flask_cors import CORS
from util.Config import Config

class Aplication:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['MYSQL_DATABASE_HOST'] = Config.MYSQL_HOST
        self.app.config['MYSQL_DATABASE_USER'] = Config.MYSQL_USER
        self.app.config['MYSQL_DATABASE_PASSWORD'] = Config.MYSQL_PASS
        self.app.config['MYSQL_DATABASE_DB'] = Config.MYSQL_DB
        self.app.config['UPLOAD_FOLDER'] = './upload'
        self.cors = CORS(self.app)