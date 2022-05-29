from flask_admin import Admin
from prontuariofacil.ext.database import db
from prontuariofacil.ext.models import tables
from .admin import UserAdmin

admin = Admin()


def init_app(app):
    admin.name = "ProntuarioFacil"
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.add_view(UserAdmin(tables.Medico, db.session))
    admin.add_view(UserAdmin(tables.Prontuario, db.session))
    
