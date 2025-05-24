from flask import Blueprint, jsonify, request
from datetime import datetime
from Models.TemperaturaModel import Temperatura
from data_base import db

temperatura_bp = Blueprint('temperatura', __name__)

@temperatura_bp.route("/monitorear", methods=["GET"])
def monitorear_temperatura():
    temperaturas = Temperatura.query.all()
    temperaturas_list = [
        {
            "id": temp.id,
            "valor": temp.valor,
            "timestamp": temp.timestamp.isoformat()
        } for temp in temperaturas
    ]
    return jsonify(temperaturas_list), 200

@temperatura_bp.route("/ajustar", methods=["POST"])
def ajustar_temperatura():
    datos = request.json
    nuevo_valor = datos.get("valor")

    if nuevo_valor is None:
        return jsonify({"mensaje": "Se requiere un valor de temperatura"}), 400

    # Aquí se podría agregar lógica para interactuar con un sistema de control
    # como un termostato, por ejemplo.

    nueva_temperatura = Temperatura(valor=nuevo_valor, timestamp=datetime.now())
    db.session.add(nueva_temperatura)
    db.session.commit()

    return jsonify({"mensaje": "Temperatura ajustada", "valor": nuevo_valor}), 201

@temperatura_bp.route("/controlar_ia", methods=["POST"])
def controlar_temperatura_ia():
    # Este endpoint podría recibir comandos de la IA para ajustar la temperatura
    datos = request.json
    comando = datos.get("comando")

    if comando == "ajustar":
        nuevo_valor = datos.get("valor")
        if nuevo_valor is None:
            return jsonify({"mensaje": "Se requiere un valor de temperatura"}), 400

        # Aquí se podría agregar lógica para ajustar la temperatura
        nueva_temperatura = Temperatura(valor=nuevo_valor, timestamp=datetime.now())
        db.session.add(nueva_temperatura)
        db.session.commit()

        return jsonify({"mensaje": "Temperatura ajustada por IA", "valor": nuevo_valor}), 200

    return jsonify({"mensaje": "Comando no reconocido"}), 400