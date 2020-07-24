import os 

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://maryann:Maryann00*@localhost/notes'
    SECRET_KEY = '\x1a\x8a\xd7:c"\xe0\x84\xc8\xad\x115'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
 'development':DevConfig,
 'production':ProdConfig
}           