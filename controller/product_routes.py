from flask import Blueprint
from flasgger import swag_from
from services import product_list, product_detail, product_add, product_update, product_delete

productos_bp = Blueprint('productos', __name__)

@swag_from({'summary': 'Consulta general de productos', 'tags': ['Productos']})
@productos_bp.route("/products", methods=["GET"])
def get_product_list():
    return product_list()

@swag_from({'summary': 'Consulta individual de producto', 'tags': ['Productos']})
@productos_bp.route("/products/<int:producto_id>", methods=["GET"])
def get_product_detail(producto_id):
    return product_detail(producto_id)

@swag_from({'summary': 'Registro de productos', 'tags': ['Productos']})
@productos_bp.route("/products", methods=["POST"])
def get_product_add():
    return product_add()

@swag_from({'summary': 'Actualización de productos', 'tags': ['Productos']})
@productos_bp.route("/products/<int:producto_id>", methods=["PUT"])
def get_product_update(producto_id):
    return product_update(producto_id)

@swag_from({'summary': 'Eliminación de productos', 'tags': ['Productos']})
@productos_bp.route("/products/<int:producto_id>", methods=["DELETE"])
def get_product_delete(producto_id):
    return product_delete(producto_id)