from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from model.models import db, Cliente, Cultivo,Asociacion,Miembro
import re
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

@app.route('/login',methods=['POST'])
def login():
    try:
        c = Cliente()
        c = c.validar(request.form['inputEmail'], request.form['inputPassword'])
        if u != None:
            login_user(u)
            return redirect(url_for('inicio'))
        else:
            return 'Datos No Válidos'
    except:
        abort(500)

@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for("inicio"))
    else:
        abort(404)

@app.route('/')
def inicio():
    try:
        if current_user.is_authenticated and current_user.Tipo=="C":
            return render_template('index.html')
        else:
            return render_template('Login.html')
    except:
        abort(500)


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
    c = c.consultaGeneral()
    for cliente in c:
        if(str(cliente.Rfc) == request.form['Rfc'] or str(cliente.Telefono) == request.form['Telefono'] or str(cliente.Email)== request.form['Email']):
            return 'Datos repetidos (RFC, Teléfono, Email)'
    C = Cliente()
    C.Nombre = request.form['Nombre']
    C.RazonSocial = request.form['Razon']
    C.LimiteCredito = request.form['Limite']
    C.Rfc = request.form['Rfc']
    C.Telefono = request.form['Telefono']
    C.Email = request.form['Email']
    C.Tipo = request.form['Password']
    C.Tipo = request.form['Tipo']
    if(int(C.LimiteCredito) <= 0):
        return 'Limite de credito no valido'
    regex = "^(\d{10}$)"    
    if(re.match(regex,str(C.Telefono))==None):
        return 'Teléfono no válido'
    
    regex = "^(\D{4}\d{6}\D{3}$)"   
    if(re.match(regex,str(C.Rfc))==None):
        return 'Rfc no válido'

    C.insertar()
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
    c = c.consultaGeneral()
    
    for cliente in c:
        if(int(cliente.IdCliente) != int(request.form['IdCliente'])):
            if(str(cliente.Rfc) == request.form['Rfc'] or str(cliente.Telefono) == request.form['Telefono'] or str(cliente.Email)== request.form['Email']):
                return 'Datos repetidos (Email, Telefono, RFC)'
    C = Cliente()
    C.IdCliente = request.form['IdCliente']
    C.Nombre = request.form['Nombre']
    C.RazonSocial = request.form['Razon']
    C.LimiteCredito = request.form['Limite']
    C.Rfc = request.form['Rfc']
    C.Telefono = request.form['Telefono']
    C.Email = request.form['Email']
    C.Tipo = request.form['Password']
    C.Tipo = request.form['Tipo']
    if(float(C.LimiteCredito) <= 0):
        return 'Limite de credito no valido'

    regex = "^(\d{10}$)"   
    if(re.match(regex,str(C.Telefono))==None):
        return 'Teléfono no válido'
    
    regex = "^(\D{4}\d{6}\D{3}$)"   
    if(re.match(regex,str(C.Rfc))==None):
        return 'Rfc no válido'

    C.actualizar()
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