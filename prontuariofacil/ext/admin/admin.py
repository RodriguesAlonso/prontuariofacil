from flask_admin.contrib.sqla import ModelView
from prontuariofacil.ext.models.tables import Medico, Prontuario
from prontuariofacil.ext.database import db

#def format_email(self, request, medico, *args):
#    return medico.email.split('@')[0]
    
class UserAdmin(ModelView):
    """interface do admim
    column_formatters = {
        "email": format_email
    }
    column_list = ["nome", "email", "crm"]
    column_filters = ["nome", "alergia", "doencas"]
    column_searchable_list=["email"]
    """