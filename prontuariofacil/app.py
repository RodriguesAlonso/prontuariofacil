from pyexpat import model
from flask import Flask

from prontuariofacil.ext import site
from prontuariofacil.ext import models
from prontuariofacil.ext import database
from prontuariofacil.ext import config
from prontuariofacil.ext import cli


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    database.init_app(app)
    cli.init_app(app)
    models.init_app(app)
    site.init_app(app)
    return app
