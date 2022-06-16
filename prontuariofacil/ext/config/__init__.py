def init_app(app):
    app.config["SECRET_KEY"] = "123"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/prontfacil"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://nmczvuzkezzqla:6c4b9a152a6dbf13bee7b666e0be8c2203407485e9bf107d32a19998283f65c8@ec2-52-204-195-41.compute-1.amazonaws.com:5432/d8e13lsedup1ao
"
    #app.config["FLASK_ADMIN_SWATCH"] = "yeti"