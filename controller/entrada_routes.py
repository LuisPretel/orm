from flask import Blueprint
from flasgger import swag_from
from services import entrada_list, entrada_detail, entrada_add, entrada_update, entrada_delete

entrada_bp = Blueprint("entradas", __name__)

@swag_from({'summary': 'Consulta general de entradas', 'tags': ['Entradas']})
@entrada_bp.route("/entradas", methods=["GET"])
def get_entrada_list():
    return entrada_list()

@swag_from({'summary': 'Consulta individual de entrada', 'tags': ['Entradas']})
@entrada_bp.route("/entradas/<int:entrada_id>", methods=["GET"])
def get_entrada_detail(entrada_id):
    return entrada_detail(entrada_id)

@swag_from({'summary': 'Registro de entrada', 'tags': ['Entradas']})
@entrada_bp.route("/entradas", methods=["POST"])
def get_entrada_add():
    return entrada_add()

@swag_from({'summary': 'Actualizar entrada', 'tags': ['Entradas']})
@entrada_bp.route("/entradas/<int:entrada_id>", methods=["PUT"])
def get_entrada_update(entrada_id):
    return entrada_update(entrada_id)

@swag_from({'summary': 'Eliminar entrada', 'tags': ['Entradas']})
@entrada_bp.route("/entradas/<int:entrada_id>", methods=["DELETE"])
def get_entrada_delete(entrada_id):
    return entrada_delete(entrada_id)