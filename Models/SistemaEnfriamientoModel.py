from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/app'

from app import db


class SistemaEnfriamiento(db.Model):
    idSE = db.Column(db.Integer, primary_key = True)
    activo = db.Column(db.Boolean, default = False, nullable = False)