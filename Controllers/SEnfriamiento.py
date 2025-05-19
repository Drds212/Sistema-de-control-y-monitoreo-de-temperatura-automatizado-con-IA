from flask import Flask, jsonify, request

def getSEnfriamiento(idSE):
    sEnfriamiento = SistemaEnfriamiento.query.get(idSE)

    if sEnfriamiento:
        return jsonify({"id": sEnfriamiento.id, "Activo": sEnfriamiento.sEnfriamiento})
    else:
        return jsonify({"error": "no encontrado"}), 404
    


def setSEnfriamiento():
    datos : request.json
    nuevoSE = SE(
        activo=datos['temperatura']
    )
    db.session.add(nuevoSE)
    db.session.commit()
