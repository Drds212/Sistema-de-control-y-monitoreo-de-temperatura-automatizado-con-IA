from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/app'

from app import db 



class Servidor(db.Model):
    idServidor = db.Column(db.Integer, primary_key = True)
    ServidorActivo = db.Column(db.Boolean, default = False, nullable = False)
    tempMaXCelsius = db.Column(db.Integer, default = 85, nullable = False)
    ubicacionSer = db.Column(db.String(125), nullable = False)
    