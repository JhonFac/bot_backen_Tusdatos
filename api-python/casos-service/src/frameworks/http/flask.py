import os
from datetime import timedelta

from enviame.inputvalidation import flask_error_handler
from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required


def create_flask_app(blueprints):

    # Función para crear una aplicación de Flask con todos sus blueprints (endpoints) asociados.
    # Asocia además el manejador de errores encontrado en la librería de validaciones.
    
    app = Flask(__name__)

    app.register_error_handler(Exception, flask_error_handler)
    
    # Configuración de JWT
    # app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]# "Enviame"
    app.config["JWT_SECRET_KEY"] = "Tus Datos"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
    JWTManager(app)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
