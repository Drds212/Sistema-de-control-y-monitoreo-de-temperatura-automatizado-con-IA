from flask import Flask, jsonify, request

def getSensor(idSensor):
    sensor = Sensor.query.get(idSensor)

    if sensor:
        return jsonify({"id": sensor.id, "temperatura": sensor.temperatura,
                        "encendido": sensor.encendido, "ubicacion": sensor.ubicacion})
    else:
        return jsonify({"error": "no encontrado"}), 404
    


def setSensor():
    datos : request.json
    nuevoSensor = Sensor(
        temperatura=datos['temperatura'],
        encendido=datos['encendido'],
        ubicacion=datos['ubicacion']
    )
    db.session.add(nuevoSensor)
    db.session.commit()
