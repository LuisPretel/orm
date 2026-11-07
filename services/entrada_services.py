from flask import jsonify, request, abort
from models import Entrada, Producto, db

def entrada_list():
    entradas = db.session.execute(db.select(Entrada)).scalars().all()
    return jsonify([e.to_dict() for e in entradas]), 200

def entrada_detail(entrada_id):
    entrada = db.session.get(Entrada, entrada_id)
    if not entrada:
        abort(404, description="Entrada no encontrada")
    return jsonify(entrada.to_dict()), 200

def entrada_add():
    data = request.get_json()
    if not data:
        abort(400, description="No se recibió información en formato JSON")

    required_fields = ["entrada_producto_id", "entrada_cantidad"]
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Falta el campo obligatorio: {field}")

    producto = db.session.get(Producto, data["entrada_producto_id"])
    if not producto:
        abort(400, description="El producto no existe")

    nueva_entrada = Entrada(
        entrada_producto_id=data["entrada_producto_id"],
        entrada_cantidad=data["entrada_cantidad"],
        entrada_stand=data.get("entrada_stand", "N/A"),
        entrada_ubicacion=data.get("entrada_ubicacion", "N/A"),
        entrada_factura=data.get("entrada_factura", "S/F")
    )
    db.session.add(nueva_entrada)
    db.session.commit()
    return jsonify(nueva_entrada.to_dict()), 201

def entrada_update(entrada_id):
    data = request.get_json()
    if not data:
        abort(400, description="No se recibió información en formato JSON")
    
    entrada = db.session.get(Entrada, entrada_id)
    if not entrada:
        abort(404, description="Entrada no encontrada")

    entrada.entrada_cantidad = data.get("entrada_cantidad", entrada.entrada_cantidad)
    entrada.entrada_stand = data.get("entrada_stand", entrada.entrada_stand)
    entrada.entrada_ubicacion = data.get("entrada_ubicacion", entrada.entrada_ubicacion)
    entrada.entrada_factura = data.get("entrada_factura", entrada.entrada_factura)
    db.session.commit()
    return jsonify(entrada.to_dict()), 200

def entrada_delete(entrada_id):
    entrada = db.session.get(Entrada, entrada_id)
    if not entrada:
        abort(404, description="Entrada no encontrada")
    db.session.delete(entrada)
    db.session.commit()
    return jsonify({"mensaje": "Entrada eliminada correctamente"}), 200