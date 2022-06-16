def init_app(app):
    app.config["SECRET_KEY"] = "123"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/prontfacil"
    #app.config["FLASK_ADMIN_SWATCH"] = "yeti"