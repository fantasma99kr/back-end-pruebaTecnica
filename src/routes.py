from flask import Blueprint, jsonify
from .stack import stackOver
from .aeropuerto import datosaeropuerto

main = Blueprint('main', __name__)

#Ruta inicial
@main.route('/', methods=['GET'])
def home():
    return jsonify({"mensaje": "API Funcionando correctamente"}),200

#obtener los puntos de la api de las preguntas de stackoverflow
@main.route('/stack', methods=['GET'])
def stack():
    return stackOver()

#obtener los puntos de la api de las preguntas de stackoverflow
@main.route('/aeropuerto', methods=['GET'])
def aeropuerto():
    return datosaeropuerto()

