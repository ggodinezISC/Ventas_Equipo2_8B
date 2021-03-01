from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from model.models import db, Cliente, Cultivo,Asociacion,Miembro
app = Flask(__name__)
app.secret_key = 'ERP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Admin:hola.123@localhost/ERP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER']='static/uploads/'
# Configuración para el manejo de la sesion de los usuarios
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "inicio"

@loginManager.user_loader
def load_user(Id):
    return Cliente.query.get(int(Id))

@app.route('/')
def hello_world():
    return render_template('Login.html')



@app.route('/index')
def index():
    return render_template('index.html')


#Inicio Crud Asociaciones
@app.route('/Asociaciones')
def consultaAsociaciones():
    a = Asociacion()
    a = a.consultaGeneral()
    return render_template('/Asociaciones/AdministrarAsociacion.html',Asociaciones=a)

@app.route('/AddAsociacion',methods=['POST'])
def guardarAsociacion():
    a = Asociacion()
    a.Nombre = request.form['Nombre']
    a.Estatus = request.form['Estatus']
    a.insertar()
    return redirect(url_for('consultaAsociaciones'))

@app.route('/EditAsociacion/<int:id>')
def consultarAsociacion(id):
    a = Asociacion()
    a.IdAsociacion = id
    a = a.consultaIndividual()
    return render_template('Asociaciones/EditAsociacion.html', Asociacion=a)

@app.route('/Asociacion/modificar', methods=['POST'])
def actualizarAsociacion():
    a = Asociacion()
    a.IdAsociacion = request.form['IdAsociacion']
    a.Nombre = request.form['Nombre']
    a.Estatus = request.form['Estatus']
    a.actualizar()
    return redirect(url_for('consultaAsociaciones'))

@app.route('/DeleteAsociacion/<int:id>')
def eliminarAsociacion(id):
    a = Asociacion()
    a.IdAsociacion = id
    a.eliminar()
    return redirect(url_for('consultaAsociaciones'))        
#Fin Crud Asociaciones

#Inicio Crud Clientes
@app.route('/Clientes')
def consultaClientes():
    c = Cliente()
    c = c.consultaGeneral()
    return render_template('/Clientes/AdministrarCliente.html',Cliente=c)

@app.route('/AddCliente',methods=['POST'])
def guardarCliente():
    c = Cliente()
    c.Nombre = request.form['Nombre']
    c.RazonSocial = request.form['Razon']
    c.LimiteCredito = request.form['Limite']
    c.Rfc = request.form['Rfc']
    c.Telefono = request.form['Telefono']
    c.Email = request.form['Email']
    c.Tipo = request.form['Tipo']
    c.insertar()
    return redirect(url_for('consultaClientes'))

@app.route('/EditCliente/<int:id>')
def consultarCliente(id):
    c = Cliente()
    c.IdCliente = id
    c = c.consultaIndividual()
    return render_template('Clientes/EditCliente.html', Cliente=c)

@app.route('/Clientes/modificar', methods=['POST'])
def actualizarCliente():
    c = Cliente()
    c.IdCliente = request.form['IdCliente']
    c.Nombre = request.form['Nombre']
    c.RazonSocial = request.form['Razon']
    c.LimiteCredito = request.form['Limite']
    c.Rfc = request.form['Rfc']
    c.Telefono = request.form['Telefono']
    c.Email = request.form['Email']
    c.Tipo = request.form['Tipo']
    c.actualizar()
    return redirect(url_for('consultaClientes'))

@app.route('/DeleteCliente/<int:id>')
def eliminarCliente(id):
    c = Cliente()
    c.IdCliente = id
    c.eliminar()
    return redirect(url_for('consultaClientes'))        
#Fin Crud Clientes

#Inicio Crud Cultivos
@app.route('/Cultivos')
def consultaCultivo():
    c = Cultivo()
    c = c.consultaGeneral()
    return render_template('/Cultivos/AdministrarCultivo.html',Cultivos=c)

@app.route('/AddCultivo',methods=['POST'])
def guardarCultivo():
    c = Cultivo()
    c.Nombre = request.form['Nombre']
    c.CostoAsesoria = request.form['Costo']
    c.Estatus       = request.form['Estatus']
    c.insertar()
    return redirect(url_for('consultaCultivos'))

@app.route('/EditCultivo/<int:id>')
def consultarCultivo(id):
    c = Cultivo()
    c.IdCultivo = id
    c = c.consultaIndividual()
    return render_template('Cultivos/EditCultivo.html', Cultivo=c)

@app.route('/Cultivo/modificar', methods=['POST'])
def actualizarCultivo():
    c = Cultivos()
    c.IdCultivo = request.form['IdCultivo']
    c.Nombre = request.form['Nombre']
    c.CostoAsesoria = request.form['Costo']
    c.Estatus       = request.form['Estatus']
    c.actualizar()
    return redirect(url_for('consultaCultivos'))

@app.route('/DeleteCultivo/<int:id>')
def eliminarCultivo(id):
    c = Cultivo()
    c.IdCultivo = id
    c.eliminar()
    return redirect(url_for('consultaCultivos'))        
#Fin Crud Cultivos


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)