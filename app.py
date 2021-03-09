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
        if c != None:
            login_user(c)
            return redirect(url_for('inicio'))
        else:
            return 'Datos Incorrectos'
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
        if current_user.is_authenticated and (current_user.Estatus=="A"):
            return render_template('index.html')
        else:
            if current_user.is_authenticated:
                logout_user()
            return render_template('Login.html')
    except:
        abort(500)

#Inicio Crud Asociaciones
@app.route('/Asociaciones')
@login_required
def consultaAsociaciones():
    a = Asociacion()
    a = a.consultaGeneral()
    return render_template('/Asociaciones/AdministrarAsociacion.html',Asociaciones=a)

@app.route('/AddAsociacion',methods=['POST'])
@login_required
def guardarAsociacion():
    try:
        a = Asociacion()
        a = a.consultaGeneral()
        for asociacion in a:
            if(str(asociacion.Nombre) == request.form['Nombre']):
                return 'Datos repetidos (Nombre)'
        aso = Asociacion()
        aso.Nombre = request.form['Nombre']
        aso.Estatus = request.form['Estatus']
        aso.insertar()
        return redirect(url_for('consultaAsociaciones'))
    except:
        return 'No se pudo realizar la inserción'

@app.route('/EditAsociacion/<int:id>')
@login_required
def consultarAsociacion(id):
    try:
        a = Asociacion()
        a.IdAsociacion = id
        a = a.consultaIndividual()
        return render_template('Asociaciones/EditAsociacion.html', Asociacion=a)
    except:
        return 'No se cargaron los datos correctamente'

@app.route('/Asociacion/modificar', methods=['POST'])
@login_required
def actualizarAsociacion():
    try:
        a = Asociacion()
        a.IdAsociacion = request.form['IdAsociacion']
        a.Nombre = request.form['Nombre']
        a.Estatus = request.form['Estatus']
        a.actualizar()
        return redirect(url_for('consultaAsociaciones'))
    except:
        return 'No se realizó la actualización, información incorrecta'

@app.route('/DeleteAsociacion/<int:id>')
@login_required
def eliminarAsociacion(id):
    a = Asociacion()
    a.IdAsociacion = id
    a.eliminar()
    return redirect(url_for('consultaAsociaciones'))        
#Fin Crud Asociaciones


#Inicio Crud Miembros
@app.route('/Miembros')
@login_required
def consultaMiembros():
    m = Miembro()
    m = m.consultaGeneral()

    c = Cliente()
    c = c.consultaGeneral()

    a = Asociacion()
    a = a.consultaGeneral()
    return render_template('/Miembros/AdministrarMiembro.html',Miembros=m,Asociaciones=a,Clientes=c)

@app.route('/AddMiembro',methods=['POST'])
@login_required
def guardarMiembro():
    try:
        m = Miembro()
        m.IdAsociacion = request.form['Asociacion']
        m.IdCliente = request.form['Cliente']
        m.FechaIncorporacion = request.form['Fecha']
        m.Estatus = request.form['Estatus']
        m.insertar()
        return redirect(url_for('consultaMiembros'))
    except:
        return'Campos Vacíos o Repetidos'

@app.route('/EditMiembro/<int:idcli>/<int:idaso>')
@login_required
def consultarMiembro(idcli,idaso):
    m = Miembro()
    m = m.consultaIndividual(idcli,idaso)

    a=Asociacion()
    a=a.consultaGeneral()
    
    c=Cliente()
    c=c.consultaGeneral()
    return render_template('Miembros/EditMiembro.html', Miembro=m, Asociacion=a,Cliente=c)

@app.route('/Miembro/modificar', methods=['POST'])
@login_required
def actualizarMiembro():
    try:
        m = Miembro()
        m.IdAsociacion = request.form['Asociacion']
        m.IdCliente = request.form['Cliente']
        m.FechaIncorporacion = request.form['Fecha']
        m.Estatus = request.form['Estatus']
        m.actualizar()
        return redirect(url_for('consultaMiembros'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteMiembro/<int:idcli>/<int:idaso>')
@login_required
def eliminarMiembro(idcli,idaso):
    m = Miembro()
    m = m.eliminar(idcli,idaso)
    return redirect(url_for('consultaMiembros'))        
#Fin Crud Miembros


#Inicio Crud Clientes
@app.route('/Clientes')
@login_required
def consultaClientes():
    c = Cliente()
    c = c.consultaGeneral()
    return render_template('/Clientes/AdministrarCliente.html',Cliente=c)

@app.route('/AddCliente',methods=['POST'])
@login_required
def guardarCliente():
    try:
        c = Cliente()
        c = c.consultaGeneral()
        for cliente in c:
            if(str(cliente.Rfc) == request.form['Rfc'] or str(cliente.Telefono) == request.form['Telefono'] or str(cliente.Email)== request.form['Email']):
                return 'Datos repetidos (RFC, Teléfono, Email)'
        C = Cliente()
        C.Nombre = request.form['Nombre']
        C.Password = request.form['Password']
        C.RazonSocial = request.form['Razon']
        C.LimiteCredito = request.form['Limite']
        C.Rfc = request.form['Rfc']
        C.Telefono = request.form['Telefono']
        C.Email = request.form['Email']
        C.Tipo = request.form['Password']
        C.Tipo = request.form['Tipo']
        C.Estatus = request.form['Estatus']
        if(int(C.LimiteCredito) <= 0):
            return 'Limite de credito no valido'
        regex = "^(\d{10}$)"    
        if(re.match(regex,str(C.Telefono))==None):
            return 'Teléfono no válido'
        
        regex = "^(\D{4}\d{6}\D{3}$)"   
        if(re.match(regex,str(C.Rfc))==None):
            return 'Rfc no válido LLLDDDDDDLLL'
        
        #Minimo 8 caracteres
        #Maximo 15
        #Al menos una letra mayúscula
        #Al menos una letra minucula
        #Al menos un dígito
        #No espacios en blanco
        #Al menos 1 caracter especial de estos 3: $ % &
        regex = "^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$)"   
        if(re.match(regex,str(C.Password))==None):
            return 'Password debil'

        C.insertar()
        return redirect(url_for('consultaClientes'))
    except:
        return 'No se guardó la información'

@app.route('/EditCliente/<int:id>')
@login_required
def consultarCliente(id):
    c = Cliente()
    c.IdCliente = id
    c = c.consultaIndividual()
    return render_template('Clientes/EditCliente.html', Cliente=c)

@app.route('/Clientes/modificar', methods=['POST'])
@login_required
def actualizarCliente():
    try:
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
        C.Password = request.form['Password']
        C.Tipo = request.form['Tipo']
        C.Estatus = request.form['Estatus']
        if(float(C.LimiteCredito) <= 0):
            return 'Limite de credito no valido'

        regex = "^(\d{10}$)"   
        if(re.match(regex,str(C.Telefono))==None):
            return 'Teléfono no válido'
        
        regex = "^(\D{4}\d{6}\D{3}$)"   
        if(re.match(regex,str(C.Rfc))==None):
            return 'Rfc no válido'

        #Minimo 8 caracteres
        #Maximo 15
        #Al menos una letra mayúscula
        #Al menos una letra minucula
        #Al menos un dígito
        #No espacios en blanco
        #Al menos 1 caracter especial de estos 3: $ % &
        regex = "^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$)"   
        if(re.match(regex,str(C.Password))==None):
            return 'Password debil'
            
        C.actualizar()
        return redirect(url_for('consultaClientes'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteCliente/<int:id>')
@login_required
def eliminarCliente(id):
    c = Cliente()
    c.IdCliente = id
    c.eliminar()
    return redirect(url_for('consultaClientes'))        
#Fin Crud Clientes

#Inicio Crud Cultivos
@app.route('/Cultivos')
@login_required
def consultaCultivo():
    c = Cultivo()
    c = c.consultaGeneral()
    return render_template('/Cultivos/AdministrarCultivo.html',Cultivos=c)

@app.route('/AddCultivo',methods=['POST'])
def guardarCultivo():
    try:
        c = Cultivo()
        c.Nombre = request.form['Nombre']
        c.CostoAsesoria = request.form['Costo']
        c.Estatus       = request.form['Estatus']
        c.insertar()
        return redirect(url_for('consultaCultivo'))
    except:
        return 'No se guardó la información'

@app.route('/EditCultivo/<int:id>')
@login_required
def consultarCultivo(id):
    c = Cultivo()
    c.IdCultivo = id
    c = c.consultaIndividual()
    return render_template('Cultivos/EditCultivo.html', Cultivo=c)

@app.route('/Cultivo/modificar', methods=['POST'])
@login_required
def actualizarCultivo():
    try:
        c = Cultivo()
        c.IdCultivo = request.form['IdCultivo']
        c.Nombre = request.form['Nombre']
        c.CostoAsesoria = request.form['Costo']
        c.Estatus       = request.form['Estatus']
        c.actualizar()
        return redirect(url_for('consultaCultivo'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteCultivo/<int:id>')
@login_required
def eliminarCultivo(id):
    c = Cultivo()
    c.IdCultivo = id
    c.eliminar()
    return redirect(url_for('consultaCultivo'))        
#Fin Crud Cultivos


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)