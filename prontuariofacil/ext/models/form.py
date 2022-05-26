import wtforms as wtf

from flask_wtf import FlaskForm


class Form_pront(FlaskForm):
    nome = wtf.StringField(
        "Nome completo do paciente", validators=[wtf.validators.DataRequired()]
    )
    cpf = wtf.StringField("CPF")
    nasc = wtf.DateField("Data de nascimento")
    sus = wtf.StringField("SUS")
    alergia = wtf.StringField("Alergias")
    doenca = wtf.StringField("Doenças pré existentes")
    historico = wtf.StringField("Histórico familiar")
    submit = wtf.SubmitField("Confirmar cadastro")


class Form_medico(FlaskForm):
    nome = wtf.StringField("Nome completo", validators=[wtf.validators.DataRequired()])
    crm = wtf.StringField("CRM")
    email = wtf.EmailField("E-mail", id="email", default="Seu e-mail...")
    senha = wtf.PasswordField(
        "senha",
        id="password",
        default="Sua senha...",
        validators=[wtf.validators.DataRequired()],
    )
    confirmar_senha = wtf.PasswordField("Confirme a senha")
    submit = wtf.SubmitField("Confirmar cadastro")
