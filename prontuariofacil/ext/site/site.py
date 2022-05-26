from flask import Blueprint, render_template
from prontuariofacil.ext.models.form import Form_pront, Form_medico
from prontuariofacil.ext.models.models import submit_pront, submit_medico
from prontuariofacil.ext.models.tables import Prontuario, Medico

site = Blueprint('site', __name__, static_folder='static',  template_folder='templates', static_url_path='/static/site')

@site.route('/')
def index():
    return render_template("index.html")

@site.route("/login")
def login():
    return render_template("login.html")

@site.route('/recuperar-senha')
def recupera_senha():
    return render_template('recuperar_senha.html')

@site.route('/cadastro-prontuario', methods=["GET", "POST"])
def cadastro_pront():
    name = None
    form = Form_pront()
    prontuario = Prontuario()    
    submit_pront(prontuario, form)
    return render_template("cadastro_prontuario.html", prontuario=form, name = name)

@site.route("/cadastro-medico", methods=["GET", "POST"])
def cadastro_medic():
    medico = Medico()
    name = None
    form = Form_medico()
    submit_medico(medico, form)
    return render_template("cadastro_medico.html",form = form, name = name, medico=medico)