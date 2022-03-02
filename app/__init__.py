import logging
from flask import Flask
from flask_restful import Api
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.utils.logger import get_logger


app = Flask(__name__)
app.config.from_object(config)
app.logger.setLevel(logging.INFO)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)
logger = get_logger()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
