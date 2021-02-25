from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from model.models import db, Botiquin, LiquidoLaboratorio
app = Flask(__name__)
app.secret_key = 'ERP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Admin:hola.123@localhost/ERP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER']='static/uploads/'
# Configuración para el manejo de la sesion de los usuarios
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "inicio"


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
