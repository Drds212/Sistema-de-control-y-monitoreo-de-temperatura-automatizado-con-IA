from flask import Flask, jsonify, request
#from Models.UserModel import User
#from Models.UserModel import db




def getUsuarioId (idUsuario):
    usuario = User.query.get(idUsuario)
    
    if usuario:
        return jsonify({"id": usuario.id, "nombre": usuario.nombreUsuario,
                        "apellido": usuario.apellidoUsiario, "cargo": usuario.cargoUsuario})
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404




def getUsuarioNombre (nombreUsuario):
    usuarios = User.query.filter_by(nombreUsuario=nombreUsuario).all()  
    if usuarios:
        return jsonify([{"id": u.id, "nombre": u.nombreUsuario, "apellido": u.apellidoUsiario,
                         "cargo": u.cargoUsuario} for u in usuarios])
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404




def setUsuario ():
    datos = request.json
    nuevoUsuario = User(
        nombreUsuario=datos["nombre"],
        apellidoUsuario=datos["apellido"],
        cargoUsuario=datos["cargo"]
        )
    db.session.add(nuevoUsuario)
    db.session.commit()

    return jsonify({"mensaje" : "usuario agregado"})

