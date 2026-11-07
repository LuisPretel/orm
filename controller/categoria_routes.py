from flask import Blueprint
from flasgger import swag_from
from services import categoria_list, categoria_detail, categoria_add, categoria_update, categoria_delete

categoria_bp = Blueprint("categorias", __name__)

@swag_from({'summary': 'Consulta general de categorías', 'tags': ['Categorias']})
@categoria_bp.route("/categorias", methods=["GET"])
def get_categoria_list():
    return categoria_list()

@swag_from({'summary': 'Consulta individual de categoría', 'tags': ['Categorias']})
@categoria_bp.route("/categorias/<int:categoria_id>", methods=["GET"])
def get_categoria_detail(categoria_id):
    return categoria_detail(categoria_id)

@swag_from({'summary': 'Registro de categoría', 'tags': ['Categorias']})
@categoria_bp.route("/categorias", methods=["POST"])
def get_categoria_add():
    return categoria_add()

@swag_from({'summary': 'Actualizar categoría', 'tags': ['Categorias']})
@categoria_bp.route("/categorias/<int:categoria_id>", methods=["PUT"])
def get_categoria_update(categoria_id):
    return categoria_update(categoria_id)

@swag_from({'summary': 'Eliminar categoría', 'tags': ['Categorias']})
@categoria_bp.route("/categorias/<int:categoria_id>", methods=["DELETE"])
def get_categoria_delete(categoria_id):
    return categoria_delete(categoria_id)