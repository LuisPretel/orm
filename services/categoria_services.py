from flask import jsonify, request, abort
from models import Categoria, db

def categoria_list():
    categorias = db.session.execute(db.select(Categoria)).scalars().all()
    return jsonify([c.to_dict() for c in categorias]), 200

def categoria_detail(categoria_id):
    categoria = db.session.get(Categoria, categoria_id)
    if not categoria:
        abort(404, description="Categoria no encontrada")
    return jsonify(categoria.to_dict()), 200

def categoria_add():
    data = request.get_json()
    if not data:
        abort(400, description="No se recibió información en formato JSON")
    if "nombre" not in data:
        abort(400, description="El campo nombre es obligatorio")

    nueva_categoria = Categoria(
        categoria_nombre=data["nombre"],
        description=data.get("descripcion", "Sin descripción")
    )
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify(nueva_categoria.to_dict()), 201

def categoria_update(categoria_id):
    data = request.get_json()
    if not data:
        abort(400, description="No se recibió información en formato JSON")
    
    categoria = db.session.get(Categoria, categoria_id)
    if not categoria:
        abort(404, description="Categoria no encontrada")

    categoria.categoria_nombre = data.get("nombre", categoria.categoria_nombre)
    categoria.description = data.get("descripcion", categoria.description)
    db.session.commit()
    return jsonify(categoria.to_dict()), 200

def categoria_delete(categoria_id):
    categoria = db.session.get(Categoria, categoria_id)
    if not categoria:
        abort(404, description="Categoria no encontrada")
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({"mensaje": "Categoria eliminada correctamente"}), 200