from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/app'

from app import db 



class Sensor(db.Model):
    idSensor = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Integer, nullable=False)
    encendido = db.Column(db.Boolean, default = False, nullable=False)
    ubicacion = db.Column(db.String(80), nullable=False)