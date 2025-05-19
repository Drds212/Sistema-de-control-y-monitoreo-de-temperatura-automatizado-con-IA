from flask import Flask, jsonify, request

def getServidor(idServidor):
    servidor = Servidor.query.get(idServidor)

    if servidor:
        return jsonify({"id": servidor.id, "Activo": servidor.ServidorActivo,
                        "tempMaXCelsius": servidor.tempMaXCelsius, "ubicacion": servidor.ubicacionSer})
    else:
        return jsonify({"error": "no encontrado"}), 404
    


def setServidor():
    datos : request.json
    nuevoServidor = Servidor(
        servidorActivo=datos['activo'],
        ubicacionSer=datos['ubicacion']
    )
    db.session.add(nuevoServidor)
    db.session.commit()
