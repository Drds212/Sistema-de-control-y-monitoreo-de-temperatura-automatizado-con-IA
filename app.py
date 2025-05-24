from flask import Flask, render_template
from flask_migrate import Migrate
from data_base import db
from Models.UserModel import User 
from Models.ServidorModel import Servidor
from Models.TemperaturaModel import Temperatura
from Controllers.UserController import usuario_bp 
from Controllers.ServidorController import servidor_bp
from Controllers.TemperaturaController import temperatura_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/app'
db.init_app(app) 
migrate = Migrate(app, db)

app.register_blueprint(usuario_bp)
app.register_blueprint(servidor_bp)
app.register_blueprint(temperatura_bp)


@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


