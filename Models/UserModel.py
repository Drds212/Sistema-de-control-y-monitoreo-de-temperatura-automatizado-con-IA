from flask import Flask;
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/app'

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(80), nullable=False)
    apellidoUsiario = db.Column(db.String(80), nullable=False)
    cargoUsuario = db.Column(db.String(80), nullable=False)
