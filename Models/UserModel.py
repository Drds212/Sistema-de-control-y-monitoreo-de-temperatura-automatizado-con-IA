from data_base import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(80), nullable=False)
    apellidoUsuario = db.Column(db.String(80), nullable=False)
    cargoUsuario = db.Column(db.String(80), nullable=False)
