# from web import app
from flask import render_template, Blueprint

base = Blueprint("base", __name__)


@base.route("/")
def index():
    return render_template("index.html")


@base.route("/portafolio")
def portafolio():
    return render_template("portafolio.html")


@base.route("/contact")
def contacto():
    return render_template("contacto.html")