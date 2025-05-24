from flask import Blueprint, jsonify, request
from Models.UserModel import User
from data_base import db 

usuario_bp = Blueprint('usuario', __name__)


@usuario_bp.route("/getUsuarios", methods=["GET"])
def getUsuarios():
    usuarios = User.query.all()
    usuarios_list = [
        {
            "id": usuario.id,
            "nombre": usuario.nombreUsuario,
            "apellido": usuario.apellidoUsuario,
            "cargo": usuario.cargoUsuario
        } for usuario in usuarios
    ]
    
    return jsonify(usuarios_list), 200


@usuario_bp.route("/getUsuario/<int:id>", methods=["GET"])
def getUsuarioPorId(id):
    usuario = User.query.get(id)  

    if usuario is None:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    usuario_data = {
        "id": usuario.id,
        "nombre": usuario.nombreUsuario,
        "apellido": usuario.apellidoUsuario,
        "cargo": usuario.cargoUsuario
    }

    return jsonify(usuario_data), 200




@usuario_bp.route("/setUsuario", methods=["POST"])
def setUsuario():
    datos = request.json

    if not all(key in datos for key in ("nombre", "apellido", "cargo")):
        return jsonify({"mensaje": "Faltan datos requeridos"}), 400

    nuevoUsuario = User(
        nombreUsuario=datos["nombre"],
        apellidoUsuario=datos["apellido"],
        cargoUsuario=datos["cargo"]
    )
    
    db.session.add(nuevoUsuario)
    db.session.commit()

    return jsonify({"mensaje": "usuario agregado"}), 201


@usuario_bp.route("/eliminarUsuario/<int:id>", methods=["DELETE"])
def eliminarUsuario(id):
    usuario = User.query.get(id)  

    if usuario is None:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    db.session.delete(usuario)  
    db.session.commit() 

    return jsonify({"mensaje": "Usuario eliminado"}), 200