from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from Controllers.UserController import setUsuario, getUsuarioId, getUsuarioNombre


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/app'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from Models.UserModel import User
from Models.SensorModel import Sensor
from Models.SistemaEnfriamientoModel import SistemaEnfriamiento
from Models.ServidorModel import Servidor

@app.route("/")
def hello_world():
    return render_template('index.html')

"""
@app.route("/getUsuarioPorId/<int:idUsuario>", methods=["GET"])
def getUsuarioId(idUsuario):
    return getUsuarioId(idUsuario)


@app.route("/getUsuarioPorNombre/<nombreUsuario>", methods=["GET"])
def getUsuarioNombre(nombreUsuario):
    return getUsuarioNombre(nombreUsuario)


@app.route("/setUsuario", methods=["POST"])
def set_usuario():
    return setUsuario()"""



if __name__ == '__main__':
    app.run(debug=True)
