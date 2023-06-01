class Config:
    DEBUG = True
    TESTING = True
    #configuracion a BBDD
    SQLALCHEMY_DATABASE_URI = 'mysql+pymsql://root:root2616@localhost:3300/flask_db'


class ProductionConfig(Config):
    DEBUG = False




class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True