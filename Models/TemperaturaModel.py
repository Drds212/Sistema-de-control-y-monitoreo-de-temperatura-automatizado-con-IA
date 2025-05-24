from data_base import db

class Temperatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

def __init__(self, valor, timestamp):
    self.valor = valor
    self.timestamp = timestamp