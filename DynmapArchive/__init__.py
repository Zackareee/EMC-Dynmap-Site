from flask import Flask
from flask_bootstrap import Bootstrap
from . import routes

def create_app():
    app=Flask(__name__)
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = 'bootsandcats'
    bootstrap = Bootstrap(app)

    app.register_blueprint(routes.mainbp)


    return app