from flask import Blueprint, render_template, request
from prontuariofacil.ext.models.tables import Prontuario, Medico
from prontuariofacil.ext.database import db



models = Blueprint(
    "models",
    __name__,
)


@models.route("/models")
def index():
    return "MODELS"


@models.route("/submit", methods=["GET", "POST"])
def submit_pront(prontuario, form):
    if request.method == "POST":
        prontuario = Prontuario(
            nome=form.nome.data,
            cpf=form.cpf.data,
            nascimento=form.nasc.data,
            numsus=form.sus.data,
            alergia=form.alergia.data,
            doencas=form.doenca.data,
            historico_fami=form.historico.data,
        )
        db.session.add(prontuario)
        db.session.commit()
    return "Prontuario adicionado"


@models.route("/submit_medico", methods=["GET", "POST"])
def submit_medico(medico, form):
    if request.method == "POST":
        medico = Medico(
            nome=form.nome.data,
            crm=form.crm.data,
            email=form.email.data,
            senha=form.senha.data,
        )
        db.session.add(medico)
        db.session.commit()
    return "Medico adicionado"
