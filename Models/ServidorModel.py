from data_base import db

class Servidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    codigo_ubicacion = db.Column(db.String(100), nullable=False)
    temperatura_maxima_celsius = db.Column(db.Integer, default= 85, nullable=False)
