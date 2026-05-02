# Registro de las rutas de la API manda a llamar a la clase
from flask import Flask
from flask_cors import CORS 
from .routes import main

def main_app_aeropuerto():
    app = Flask(__name__)

    #configuracion de cors para que pueda consultar
    CORS(app)
    app.register_blueprint(main)
    return app