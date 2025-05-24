from flask import Blueprint, jsonify, request
from Models.ServidorModel import Servidor
from data_base import db 

servidor_bp = Blueprint('servidor',__name__)


@servidor_bp.route("/getServidores", methods=["GET"])
def getServidores():
    servidores = Servidor.query.all()
    servidores_list = [
        {
            "id": servidor.id,
            "modelo": servidor.modelo,
            "codigo_ubicacion": servidor.codigo_ubicacion,
            "temperatura_maxima_celsius": servidor.temperatura_maxima_celsius
        } for servidor in servidores
    ]
    
    return jsonify(servidores_list), 200


@servidor_bp.route("/getServidor/<int:id>", methods=["GET"])
def getServidorPorId(id):
    servidor = Servidor.query.get(id)

    if servidor is None:
        return jsonify({"mensaje": "Servidor no encontrado"}), 404

    servidor_data ={
        "id": servidor.id,
        "modelo": servidor.modelo,
        "codigo_ubicacion": servidor.codigo_ubicacion,
        "temperatura_maxima_celsius": servidor.temperatura_maxima_celsius
    }
    
    return jsonify(servidor_data), 200




@servidor_bp.route("/setServidor", methods=["POST"])
def setServidor() :
    datos = request.json

    if not all(key in datos for key in ("modelo", "codigo_ubicacion")):
        return jsonify({"mensaje": "Faltan datos requeridos"}), 400

    nuevoServidor = Servidor(
        modelo=datos["modelo"],
        codigo_ubicacion=datos["codigo_ubicacion"]
    )
    
    db.session.add(nuevoServidor)
    db.session.commit()

    return jsonify({"mensaje": "nuevo servidor agregado"}), 201


@servidor_bp.route("/eliminarServidor/<int:id>", methods=["DELETE"])
def eliminarServidor(id):
    servidor = Servidor.query.get(id)  

    if servidor is None:
        return jsonify({"mensaje": "Servidor no encontrado"}), 404

    db.session.delete(servidor)  
    db.session.commit() 

    return jsonify({"mensaje": "Servidor eliminado"}), 200