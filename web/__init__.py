from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#CONFIGURACION DE BBDD
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from web.views import base
from web.project.views import project
# import web.views
app.register_blueprint(base)
app.register_blueprint(project)

#cargar todas las consultas
db.create_all()