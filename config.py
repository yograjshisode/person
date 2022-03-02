from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv()


class Config(object):
    DEBUG = False
    TESTING = False
    FLASK_DEBUG = 1
    LOG_TO_STDOUT = environ.get('LOG_TO_STDOUT', False)


class DevelopmentConfig(Config):
    """
    Staging URL Details and configs
    """
    load_dotenv(path.join(basedir, 'dev.env'))
    MYSQL_HOST = environ['MYSQL_HOST']
    MYSQL_USER_NAME = environ['MYSQL_USER_NAME']
    MYSQL_PASSWORD = environ['MYSQL_PASSWORD']
    MYSQL_DATABASE_NAME = environ['MYSQL_DATABASE_NAME']
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(MYSQL_USER_NAME, MYSQL_PASSWORD, MYSQL_HOST,
                                                           MYSQL_DATABASE_NAME)
    DEBUG = True


class ProductionConfig(Config):
    load_dotenv(path.join(basedir, 'prod.env'))
    DEBUG = False


config_data = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

config_name = environ.get('APP_CONFIG', 'development')
config = config_data[config_name]
