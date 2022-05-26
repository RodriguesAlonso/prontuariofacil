from .models import models

def init_app(app):
    app.register_blueprint(models)