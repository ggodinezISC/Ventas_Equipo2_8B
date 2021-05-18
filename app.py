from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from model.models import db, Venta,Sucursal,Empleado, VentasDetalle, Cobro, Envio, DetalleEnvio,  Cliente, Cultivo,Asociacion,Miembro,Estado,Ciudad,DireccionesClientes,History,Parcela,ContactosClientes,UnidadesTransportes,Mantenimiento
import re,js2py
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
            cult = History()
            c = History()
            cult=cult.consultaGeneral()
            for a in cult:
                if(str(a.Email)==current_user.Email):
                    return redirect('/')           
            
            c.Nombre= current_user.Nombre
            c.Email=current_user.Email
            c.insertar()
            return redirect('/')
        else:
            return render_template('Errores/error500.html',mensaje='Datos incorrectos de inicio')
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

@app.route('/Historial/<string:id>')
@login_required
def hosto(id):
    if current_user.is_authenticated:
        logout_user()
        return render_template('login.html',correo=id)
    else:
        abort(404)


@app.route('/')
def inicio():
    try:
        if current_user.is_authenticated and (current_user.Estatus=="A"):
            cult = History()
            cult=cult.consultaGeneral()
            
            return render_template('index.html',Historial=cult)
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
                return  render_template('Errores/error500.html',mensaje='Datos repetidos (Nombre)')
        aso = Asociacion()
        aso.Nombre = request.form['Nombre']
        aso.Estatus = request.form['Estatus']
        aso.insertar()
        return redirect(url_for('consultaAsociaciones'))
    except:
        return render_template('Errores/error500.html',mensaje='No se pudo realizar la inserción')

@app.route('/EditAsociacion/<int:id>')
@login_required
def consultarAsociacion(id):
    try:
        a = Asociacion()
        a.IdAsociacion = id
        a = a.consultaIndividual()
        return render_template('Asociaciones/EditAsociacion.html', Asociacion=a)
    except:
        return render_template('Errores/error400.html',mensaje='No se cargaron los datos correctamente')

@app.route('/Asociacion/modificar', methods=['POST'])
@login_required
def actualizarAsociacion():
    try:
        A = Asociacion()
        A = A.consultaGeneral()
        for asociacion in A:
            if(str(asociacion.Nombre) == request.form['Nombre']):
                return  render_template('Errores/error500.html',mensaje='Datos repetidos (Nombre)')
            else:
                aso = Asociacion()
                a.IdAsociacion = request.form['IdAsociacion']
                a.Nombre = request.form['Nombre']
                a.Estatus = request.form['Estatus']
                a.actualizar()
                return redirect(url_for('consultaAsociaciones'))
    except:
        return render_template('Errores/error500.html',mensaje='No se cargó la página')

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
        return  render_template('Errores/error500.html',mensaje='Campos Vacíos o Repetidos')

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
        return  render_template('Errores/error500.html',mensaje='No se actualizó')

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
                return  render_template('Errores/error500.html',mensaje='Datos repetidos (RFC, Teléfono, Email)')
        C = Cliente()
        C.Nombre = request.form['Nombre']
        C.Password = request.form['Password']
        C.RazonSocial = request.form['Razon']
        C.LimiteCredito = request.form['Limite']
        C.Rfc = request.form['Rfc']
        C.Telefono = request.form['Telefono']
        C.Email = request.form['Email']
        C.Tipo = request.form['Tipo']
        C.Estatus = request.form['Estatus']
        if(int(C.LimiteCredito) <= 0):
            return  render_template('Errores/error500.html',mensaje='Limite de credito no valido')
        regex = "^(\d{10}$)"    
        if(re.match(regex,str(C.Telefono))==None):
            return  render_template('Errores/error500.html',mensaje='Teléfono no válido')
        
        regex = "^(\D{4}\d{6}\D{3}$)"   
        if(re.match(regex,str(C.Rfc))==None):
            return  render_template('Errores/error500.html',mensaje='Rfc no válido LLLDDDDDDLLL')
        
        #Minimo 8 caracteres
        #Maximo 15
        #Al menos una letra mayúscula
        #Al menos una letra minucula
        #Al menos un dígito
        #No espacios en blanco
        #Al menos 1 caracter especial de estos 3: $ % &
        regex = "^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$)"   
        if(re.match(regex,str(C.Password))==None):
            return  render_template('Errores/error500.html',mensaje='Password debil')

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
                    return  render_template('Errores/error500.html',mensaje='Datos repetidos (Email, Telefono, RFC)')
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
            return  render_template('Errores/error500.html',mensaje='Limite de credito no valido')

        regex = "^(\d{10}$)"   
        if(re.match(regex,str(C.Telefono))==None):
            return  render_template('Errores/error500.html',mensaje='Teléfono no válido')
        
        regex = "^(\D{4}\d{6}\D{3}$)"   
        if(re.match(regex,str(C.Rfc))==None):
            return  render_template('Errores/error500.html',mensaje='Rfc no válido')

        #Minimo 8 caracteres
        #Maximo 15
        #Al menos una letra mayúscula
        #Al menos una letra minucula
        #Al menos un dígito
        #No espacios en blanco
        #Al menos 1 caracter especial de estos 3: $ % &
        regex = "^((?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$)"   
        if(re.match(regex,str(C.Password))==None):
            return  render_template('Errores/error500.html',mensaje='Password debil')
            
        C.actualizar()
        return redirect(url_for('consultaClientes'))
    except:
        return  render_template('Errores/error500.html',mensaje='No se actualizó la información')

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
        C=Cultivo()
        C=C.consultaGeneral()
        for direccion in C:
            if(str(direccion.Nombre) == c.Nombre):
                return  render_template('Errores/error500.html',mensaje='Datos repetidos (Nombre)')
        c.insertar()
        return redirect(url_for('consultaCultivo'))
    except:
        return  render_template('Errores/error500.html',mensaje='No se guardó la información')

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
        return  render_template('Errores/error500.html',mensaje='No se actualizó la información')

@app.route('/DeleteCultivo/<int:id>')
@login_required
def eliminarCultivo(id):
    c = Cultivo()
    c.IdCultivo = id
    c.eliminar()
    return redirect(url_for('consultaCultivo'))        
#Fin Crud Cultivos


#Inicio Crud Estados
@app.route('/Estados/<int:id>')
@login_required
def consultaEstados(id):
    E = Estado()
    E = E.consultaGeneral()
    cantA=0;cantB=0;
    for direc in E:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)

    return render_template('/Estados/AdministrarEstado.html',Estado=E,PaginasA=cantA,PosicionA=id)

@app.route('/AddEstado',methods=['POST'])
@login_required
def guardarEstado():
    try:
        E = Estado()
        E.nombre = request.form['Nombre']
        E.siglas = request.form['Siglas']
        E.estatus = request.form['Estatus']
        d = Estado()
        d=d.consultaGeneral()
        for direccion in d:
            if(str(direccion.nombre) == E.nombre):
                return  render_template('Errores/error500.html',mensaje='Datos repetidos (Nombre)')
        E.insertar()
        return redirect('/Estados/1')
    except:
        return 'No se guardó la información'

@app.route('/EditEstado/<int:id>')
@login_required
def consultarEstado(id):
    E = Estado()
    E.idEstado = id
    E = E.consultaIndividual()
    return render_template('Estados/EditEstado.html', Estado=E)

@app.route('/Estados/modificar', methods=['POST'])
@login_required
def actualizarEstado():
    try:
        E = Estado()
        E.idEstado = request.form['IdEstado']
        E.nombre = request.form['Nombre']
        E.siglas = request.form['Siglas']
        E.estatus = request.form['Estatus']
        
        E.actualizar()
        return redirect('/Estados/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteEstado/<int:id>')
@login_required
def eliminarEstado(id):
    E = Estado()
    E.idEstado = id
    E.eliminar()
    return redirect('/Estados/1')        
#Fin Crud Estados


#Inicio Crud Ciudades
@app.route('/Ciudades/<int:id>')
@login_required
def consultaCiudades(id):
    C = Ciudad()
    C = C.consultaGeneral()
    E = Estado()
    E = E.consultaGeneral()
    cantA=0;cantB=0;
    for direc in C:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    return render_template('/Ciudades/AdministrarCiudad.html',Ciudades=C,Estados=E, PaginasA=cantA,PosicionA=id)

@app.route('/AddCiudad',methods=['POST'])
@login_required
def guardarCiudad():
    try:
        C = Ciudad()
        C.idEstado = request.form['IdEstado']
        C.nombre = request.form['Nombre']
        C.estatus = request.form['Estatus']
        
        d = Ciudad()
        d=d.consultaGeneral()
        for direccion in d:
            if(str(direccion.nombre) == C.nombre):
                return  render_template('Errores/error500.html',mensaje='Datos repetidos (Nombre)')
        C.insertar()
        return redirect('/Ciudades/1')
    except:
        return 'No se guardó la información'

@app.route('/EditCiudad/<int:id>')
@login_required
def consultarCiudad(id):
    C = Ciudad()
    C.idCiudad = id
    C = C.consultaIndividual()
    return render_template('Ciudades/EditCiudad.html', Ciudad=C)

@app.route('/Ciudades/modificar', methods=['POST'])
@login_required
def actualizarCiudad():
    try:
        C = Ciudad()
        C.idCiudad = request.form['IdCiudad']
        C.idEstado = request.form['IdEstado']
        C.nombre = request.form['Nombre']
        C.estatus = request.form['Estatus']
        C.actualizar()
        return redirect('/Ciudades/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteCiudad/<int:id>')
@login_required
def eliminarCiudad(id):
    C = Ciudad()
    C.idCiudad = id
    C.eliminar()
    return redirect('/Ciudades/1')        
#Fin Crud Ciudades

#Inicio Crud DireccionesClientes
@app.route('/DireccionesClientes/<int:id>')
@login_required
def consultaDirecciones(id):
    cantA=0;cantB=0;
    D = DireccionesClientes()
    D = D.consultaGeneral()
    E = Cliente()
    E = E.consultaGeneral()
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    
    
    F = Ciudad()
    F = F.consultaGeneral()
    return render_template('/DireccionesClientes/AdministrarDireccion.html',Direccion=D,Clientes=E,Ciudad=F,PaginasA=cantA,PosicionA=id)

@app.route('/AddDireccion',methods=['POST'])
@login_required
def guardarDireccion():
    try:
        D = DireccionesClientes()
        D.idCliente = request.form['IdCliente']
        D.idCiudad = request.form['IdCiudad']
        D.calle = request.form['Calle']
        D.numero = request.form['Numero']
        D.colonia = request.form['Colonia']
        D.codigoPostal = request.form['CP']
        D.tipo = request.form['Tipo']
        D.estatus = request.form['Estatus']
        regex = "^(\d{5}$)"    
        if(re.match(regex,str(D.codigoPostal))==None):
            return  render_template('Errores/error500.html',mensaje='CP no válido')  
        if(int(D.numero)<=0):
            return  render_template('Errores/error500.html',mensaje='Número no válido')
        D.insertar()
        return redirect('/DireccionesClientes/1')
    except:
        return 'No hay respuesta a tu peticion'

@app.route('/EditDireccion/<int:id>')
@login_required
def consultarDireccion(id):
    D = DireccionesClientes()
    D.idDireccion = id
    D = D.consultaIndividual()
    E = Cliente()
    E = E.consultaGeneral()
    F = Ciudad()
    F = F.consultaGeneral()
    return render_template('DireccionesClientes/EditDireccion.html', Direccion=D,Clientes=E,Ciudad=F)

@app.route('/Direcciones/modificar', methods=['POST'])
@login_required
def actualizarDireccion():
    try:
        D = DireccionesClientes()
        D.idDireccion = request.form['IdDireccion']
        D.idCliente = request.form['IdCliente']
        D.idCiudad = request.form['IdCiudad']
        D.calle = request.form['Calle']
        D.numero = request.form['Numero']
        D.colonia = request.form['Colonia']
        D.codigoPostal = request.form['CP']
        D.tipo = request.form['Tipo']
        D.estatus = request.form['Estatus']

        regex = "^(\d{5}$)"    
        if(re.match(regex,str(D.codigoPostal))==None):
            return  render_template('Errores/error500.html',mensaje='CP no válido')  
        if(int(D.numero)<=0):
            return  render_template('Errores/error500.html',mensaje='Número no válido')
        D.actualizar()
        return redirect('/DireccionesClientes/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteDireccion/<int:id>')
@login_required
def eliminarDireccion(id):
    D= DireccionesClientes()
    D.idDireccion = id
    D.eliminar()
    return redirect('/DireccionesClientes/1')        
#Fin Crud DireccionesClientes

#Inicio Crud Parcelas
@app.route('/Parcelas/<int:id>')
@login_required
def consultaParcelas(id):
    D = Parcela()
    D = D.consultaGeneral()
    E = Cliente()
    E = E.consultaGeneral()
    F = Cultivo()
    F = F.consultaGeneral()
    G = DireccionesClientes()
    G = G.consultaGeneral()
    cantA=0;cantB=0;
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)

    return render_template('/Parcelas/AdministrarParcela.html',Parcela=D,Clientes=E,Cultivo=F,Direccion=G,PaginasA=cantA,PosicionA=id)

@app.route('/AddParcela',methods=['POST'])
@login_required
def guardarParcela():
    try:
        D = Parcela()
        D.idCliente = request.form['IdCliente']
        D.idCultivo = request.form['IdCultivo']
        D.idDireccion = request.form['IdDireccion']
        D.extension = request.form['Extension']
        D.estatus = request.form['Estatus']   
        if(float(D.extension)<=0):
            return  render_template('Errores/error500.html',mensaje='extensión no válida') 
        D.insertar()
        return redirect('/Parcelas/1')
    except:
        return 'No se guardó la información'

@app.route('/EditParcela/<int:id>')
@login_required
def consultarParcela(id):
    D = Parcela()    
    D.idParcela = id
    D = D.consultaIndividual()

    F = DireccionesClientes()
    F=F.consultaGeneral()
    
    G = Cliente()
    G=G.consultaGeneral()
    
    H = Cultivo()
    H=H.consultaGeneral()
    return render_template('Parcelas/EditParcela.html', Parcela=D,Direcciones=F,Clientes=G,Cultivos=H)

@app.route('/Parcelas/modificar', methods=['POST'])
@login_required
def actualizarParcela():
    try:
        D = Parcela()
        D.idParcela = request.form['IdParcela']
        D.idCliente = request.form['IdCliente']
        D.idCultivo = request.form['IdCultivo']
        D.idDireccion = request.form['IdDireccion']
        D.extension = request.form['Extension']
        D.estatus = request.form['Estatus']
        if(float(D.extension)<=0):
            return  render_template('Errores/error500.html',mensaje='extensión no válida') 
        D.actualizar()
        return redirect('/Parcelas/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteParcela/<int:id>')
@login_required
def eliminarParcela(id):
    D= Parcela()
    D.idParcela = id
    D.eliminar()
    return redirect('/Parcelas/1')        
#Fin Crud Parcelas


#Inicio Crud ContactosCliente
@app.route('/ContactosClientes/<int:id>')
@login_required
def consultaContactos(id):
    D = ContactosClientes()
    D = D.consultaGeneral()
    C = Cliente()
    C = C.consultaGeneral()
    cantA=0;
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    return render_template('/ContactosClientes/AdministrarContacto.html',Contacto=D,Cliente=C,PaginasA=cantA,PosicionA=id)

@app.route('/AddContacto',methods=['POST'])
@login_required
def guardarContacto():
    try:
        D = ContactosClientes()
        D.idCliente = request.form['IdCliente']
        D.nombre = request.form['Nombre']
        D.telefono = request.form['Telefono']
        D.email = request.form['Email']
        D.estatus = request.form['Estatus']

        d = ContactosClientes()
        d = d.consultaGeneral()
        for cliente in d:
            if(str(cliente.email) == str(D.email) or str(cliente.telefono) == str(D.telefono) ):
                return  render_template('Errores/error500.html',mensaje='Datos repetidos (Email o Teléfono)')
        regex = "^(\d{10}$)"    
        if(re.match(regex,str(D.telefono))==None):
            return  render_template('Errores/error500.html',mensaje='teléfono no válido')  
        D.insertar()
        return redirect('/ContactosClientes/1')
    except:
        return 'No se guardó la información'

@app.route('/EditContacto/<int:id>')
@login_required
def consultarContacto(id):
    D = ContactosClientes()
    D.idContacto = id
    D = D.consultaIndividual()
    C = Cliente()
    C = C.consultaGeneral()
    return render_template('ContactosClientes/EditContacto.html', Contacto=D, Cliente=C)

@app.route('/Contacto/modificar', methods=['POST'])
@login_required
def actualizarContacto():
    try:
        D = ContactosClientes()
        D.idContacto = request.form['IdContacto']
        D.idCliente = request.form['IdCliente']
        D.nombre = request.form['Nombre']
        D.telefono = request.form['Telefono']
        D.email = request.form['Email']
        D.estatus = request.form['Estatus']
        regex = "^(\d{10}$)"    
        if(re.match(regex,str(D.telefono))==None):
            return  render_template('Errores/error500.html',mensaje='teléfono no válido')  
        D.actualizar()
        return redirect('/ContactosClientes/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteContacto/<int:id>')
@login_required
def eliminarContacto(id):
    D= ContactosClientes()
    D.idContacto = id
    D.eliminar()
    return redirect('/ContactosClientes/1')        
#Fin Crud ContactosCliente


#Inicio Crud UnidadesTransporte
@app.route('/UnidadesTransporte/<int:id>')
@login_required
def consultaUnidades(id):
    D = UnidadesTransportes()
    D = D.consultaGeneral()
    cantA=0;
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    return render_template('/UnidadesTransporte/AdministrarUnidad.html',Unidades=D,PaginasA=cantA,PosicionA=id)

@app.route('/AddUnidad',methods=['POST'])
@login_required
def guardarUnidad():
    try:
        D = UnidadesTransportes()
        D.placas = request.form['Placas']
        D.marca = request.form['Marca']
        D.modelo = request.form['Modelo']
        D.anio = request.form['Anio']
        D.capacidad = request.form['Capacidad']
        D.tipo = request.form['Tipo']
        D.estatus = request.form['Estatus']
        
        d= UnidadesTransportes()
        d=d.consultaGeneral()
        for cliente in d:
            if(str(cliente.placas) == request.form['Placas'] ):
                return  render_template('Errores/error500.html',mensaje='Datos repetidos (Placas)')

        regex = "^(\d{3}-\D{4}$)"   
        if(re.match(regex,str(D.placas))==None):
            return  render_template('Errores/error500.html',mensaje='Placas no válidas LLL-DDDD')

        regex = "^(\d{4}$)"   
        if(re.match(regex,str(D.anio))==None):
            return  render_template('Errores/error500.html',mensaje='año no válido DDDD')
          
        
        if(int (D.capacidad)<=0):
            return  render_template('Errores/error500.html',mensaje='capacidad no válida')

        D.insertar()
        return redirect('/UnidadesTransporte/1')
    except:
        return 'No se guardó la información'

@app.route('/EditUnidad/<int:id>')
@login_required
def consultarUnidad(id):
    D = UnidadesTransportes()
    D.idUnidadTransporte = id
    D = D.consultaIndividual()
    return render_template('UnidadesTransporte/EditUnidad.html', Unidad=D)

@app.route('/Unidad/modificar', methods=['POST'])
@login_required
def actualizarUnidad():
    try:
        D = UnidadesTransportes()
        D.idUnidadTransporte = request.form['IdUnidad']
        D.placas = request.form['Placas']
        D.marca = request.form['Marca']
        D.modelo = request.form['Modelo']
        D.anio = request.form['Anio']
        D.capacidad = request.form['Capacidad']
        D.tipo = request.form['Tipo']
        D.estatus = request.form['Estatus']
        

        regex = "^(\d{4}$)"   
        if(re.match(regex,str(D.anio))==None):
            return  render_template('Errores/error500.html',mensaje='año no válido DDDD')
          
        
        if(int (D.capacidad)<=0):
            return  render_template('Errores/error500.html',mensaje='capacidad no válida')  
        

        D.actualizar()
        return redirect('/UnidadesTransporte/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteUnidad/<int:id>')
@login_required
def eliminarUnidad(id):
    D= UnidadesTransportes()
    D.idUnidadTransporte = id
    D.eliminar()
    return redirect('/UnidadesTransporte/1')        
#Fin Crud UnidadesTransporte


#Inicio Crud Mantenimiento
@app.route('/Mantenimientos/<int:id>')
@login_required
def consultaMantenimientos(id):
    D = Mantenimiento()
    D = D.consultaGeneral()
    F = UnidadesTransportes()
    F = F.consultaGeneral()
    cantA=0;
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    return render_template('/Mantenimientos/AdministrarMantenimiento.html',Mantenimientos=D,Unidades=F,PaginasA=cantA,PosicionA=id)

@app.route('/AddMantenimiento',methods=['POST'])
@login_required
def guardarMantenimiento():
    try:
        D = Mantenimiento()
        D.idUnidadTransporte = request.form['IdUnidad']
        D.fechaInicio = request.form['FechaI']
        D.fechaFin = request.form['FechaF']
        D.taller = request.form['Taller']
        D.costo = request.form['Costo']
        D.comentarios = request.form['Comentarios']
        D.tipo = request.form['Tipo']
        D.estatus = request.form['Estatus']
        
        
        if(int (D.costo)<1):
            return  render_template('Errores/error500.html',mensaje='Costo no válido')

        D.insertar()
        return redirect('/Mantenimientos/1')
    except:
        return 'No se guardó la información'

@app.route('/EditMantenimiento/<int:id>')
@login_required
def consultarMantenimiento(id):
    D = Mantenimiento()
    D.idMantenimiento = id
    D = D.consultaIndividual()
    F = UnidadesTransportes()
    F = F.consultaGeneral()
    return render_template('Mantenimientos/EditMantenimiento.html', Mantenimiento=D,Unidades=F)

@app.route('/Mantenimiento/modificar', methods=['POST'])
@login_required
def actualizarMantenimiento():
    try:
        D = Mantenimiento()
        D.idMantenimiento = request.form['IdMantenimiento']
        D.idUnidadTransporte = request.form['IdUnidad']
        D.fechaInicio = request.form['FechaI']
        D.fechaFin = request.form['FechaF']
        D.taller = request.form['Taller']
        D.costo = request.form['Costo']
        D.comentarios = request.form['Comentarios']
        D.tipo = request.form['Tipo']
        D.estatus = request.form['Estatus']
         
        if(float(D.costo)<0):
            return  render_template('Errores/error500.html',mensaje='Costo no válido')
        D.actualizar()
        return redirect('/Mantenimientos/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteMantenimiento/<int:id>')
@login_required
def eliminarMantenimiento(id):
    D= Mantenimiento()
    D.idMantenimiento = id
    D.eliminar()
    return redirect('/Mantenimientos/1')        
#Fin Crud Mantenimiento

#Inicio Crud Ventas
@app.route('/Ventas/<int:id>')
@login_required
def consultaVentas(id):
    V = Venta()
    V = V.consultaGeneral()
    cantA=0;
    for direc in V:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    
    
    F = Cliente()
    F = F.consultaGeneral()
    S = Sucursal()
    S = S.consultaGeneral()
    E = Empleado()
    E = E.consultaGeneral()

    return render_template('/Ventas/AdministrarVenta.html',Ventas=V,Sucursales=S,Empleados=E,Clientes=F,PaginasA=cantA,PosicionA=id)

@app.route('/AddVenta',methods=['POST'])
@login_required
def guardarVenta():
     D = Venta()
     D.idCliente = request.form['idCliente']
     D.idSucursal = request.form['idSucursal']
     D.idEmpleado = request.form['idEmpleado']
     D.fecha = request.form['fecha']
     D.subtotal = request.form['subtotal']
     D.iva = request.form['iva']
     D.cantPagada = request.form['cantPagada']
     D.total = ( (float (D.iva)/100)*float(D.subtotal) )+ float(D.subtotal)
     D.comentarios = request.form['comentarios']
     D.estatus = request.form['estatus']
     D.tipo = request.form['tipo']
     D.insertar()
     return redirect('/Ventas/1')

@app.route('/EditVenta/<int:id>')
@login_required
def consultarVenta(id):
    D = Venta()
    D.idVenta = id
    D = D.consultaIndividual()
    F = Cliente()
    F = F.consultaGeneral()
    S = Sucursal()
    S = S.consultaGeneral()
    E = Empleado()
    E = E.consultaGeneral()
    return render_template('Ventas/EditVenta.html',Sucursales=S,Empleados=E,Clientes=F,Venta=D)

@app.route('/Venta/modificar', methods=['POST'])
@login_required
def actualizarVenta():
    try:
        D = Venta()
        D.idVenta = request.form['idVenta']
        D.fecha = request.form['fecha']
        D.subtotal = request.form['subtotal']
        D.iva = request.form['iva']
        D.total = request.form['total']
        D.cantPagada = request.form['cantPagada']
        D.comentarios = request.form['comentarios']
        D.estatus = request.form['estatus']
        D.tipo = request.form['tipo']
        D.idCliente = request.form['idCliente']
        D.idSucursal = request.form['idSucursal']
        D.idEmpleado = request.form['idEmpleado']

        
        D.actualizar()
        return redirect('/Ventas/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteVenta/<int:id>')
@login_required
def eliminarVenta(id):
    D= Venta()
    D.idVenta = id
    D.eliminar()
    return redirect('/Ventas/1')        
#Fin Crud Ventas


#Inicio Crud VentaDetalle
@app.route('/VentaDetalle/<int:id>')
@login_required
def consultaVentaDe(id):
    cantA=0;
    D = VentasDetalle()
    D = D.consultaGeneral()
    C = Venta()
    C = C.consultaGeneral()
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    
    return render_template('/VentasDetalle/AdministrarDetalle.html',Detalles=D,Ventas=C,PaginasA=cantA,PosicionA=id)

@app.route('/AddVentaDetalle',methods=['POST'])
@login_required
def guardarVentaDe():
    try:
        D = VentasDetalle()
        D.precioVenta = request.form['precioVenta']
        D.cantidad = request.form['cantidad']
        D.subtotal = request.form['subtotal']
        D.idVenta = request.form['idVenta']
        D.estatus = request.form['estatus']
        D.insertar()
        return redirect('/VentaDetalle/1')
    except:
        return 'No hay respuesta a tu peticion'

@app.route('/EditVentaDetalle/<int:id>')
@login_required
def consultarVentaDe(id):
    D = VentasDetalle()
    D.idVentaDetalle = id
    D = D.consultaIndividual()
    C = Venta()
    C = C.consultaGeneral()
    return render_template('VentasDetalle/EditDetalle.html', Ventas=C, Detalle=D)

@app.route('/VentaDetalle/modificar', methods=['POST'])
@login_required
def actualizarVentaDe():
    try:
        D = VentasDetalle()
        D.idVentaDetalle = request.form['idVentaDetalle']
        D.precioVenta = request.form['precioVenta']
        D.cantidad = request.form['cantidad']
        D.subtotal = request.form['subtotal']
        D.idVenta = request.form['idVenta']
        D.estatus = request.form['estatus']
        
        D.actualizar()
        return redirect('/VentaDetalle/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteVentaDetalle/<int:id>')
@login_required
def eliminarVentaDe(id):
    D= VentasDetalle()
    D.idVentaDetalle = id
    D.eliminar()
    return redirect('/VentaDetalle/1')        
#Fin Crud VentasDetalle

#Inicio Crud Cobro
@app.route('/Cobros/<int:id>')
@login_required
def consultaCobros(id):
    cantA=0;
    D = Cobro()
    D = D.consultaGeneral()

    V = Venta()
    V = V.consultaGeneral()
   
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    
    return render_template('/Cobros/AdministrarCobro.html',Cobro=D,Ventas=V,PaginasA=cantA,PosicionA=id)

@app.route('/AddCobro',methods=['POST'])
@login_required
def guardarCobro():
    D = Cobro()
    D.fecha = request.form['fecha']
    D.importe = request.form['importe']
    D.idVenta = request.form['idVenta']
    D.estatus = request.form['estatus']
    D.insertar()
    return redirect('/Cobros/1')

@app.route('/EditCobro/<int:id>')
@login_required
def consultarCobro(id):
    D = Cobro()
    D.idCobro = id
    D = D.consultaIndividual()
    return render_template('Cobros/EditCobro.html', Cobro=D)

@app.route('/Cobro/modificar', methods=['POST'])
@login_required
def actualizarCobro():
    try:
        D = Cobro()
        D.idCobro = request.form['idCobro']
        D.fecha = request.form['fecha']
        D.importe = request.form['importe']
        D.idVenta = request.form['idVenta']
        D.estatus = request.form['estatus']

        
        D.actualizar()
        return redirect('/Cobros/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteCobro/<int:id>')
@login_required
def eliminarCobro(id):
    D= Cobro()
    D.idCobro = id
    D.eliminar()
    return redirect('/Cobros/1')        
#Fin Crud Cobros

#Inicio Crud Envios
@app.route('/Envios/<int:id>')
@login_required
def consultaEnvios(id):
    cantA=0;
    D = Envio()
    D = D.consultaGeneral()
    U = UnidadesTransportes()
    U = U.consultaGeneral()
    
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    return render_template('/Envios/AdministrarEnvio.html',Direccion=D,Unidades=U, PaginasA=cantA,PosicionA=id)

@app.route('/AddEnvio',methods=['POST'])
@login_required
def guardarEnvio():
    try:
        D = Envio()
        D.fechaInicio = request.form['fechaInicio']
        D.fechaFin = request.form['fechaFin']
        D.idUnidadTransporte = request.form['idUnidadTransporte']
        D.pesoTotal = request.form['pesoTotal']
        D.estatus = request.form['estatus']
        
        D.insertar()
        return redirect('/Envios/1')
    except:
        return 'No hay respuesta a tu peticion'

@app.route('/EditEnvio/<int:id>')
@login_required
def consultarEnvio(id):
    D = Envio()
    D.idEnvio = id
    D = D.consultaIndividual()
    U = UnidadesTransportes()
    U = U.consultaGeneral()
    
    return render_template('Envios/EditEnvio.html', Direccion=D, Unidades=U)

@app.route('/Envio/modificar', methods=['POST'])
@login_required
def actualizarEnvio():
    try:
        D = Envio()
        D.idEnvio = request.form['idEnvio']
        D.fechaInicio = request.form['fechaInicio']
        D.fechaFin = request.form['fechaFin']
        D.idUnidadTransporte = request.form['idUnidadTransporte']
        D.pesoTotal = request.form['pesoTotal']
        D.estatus = request.form['estatus']
        D.actualizar()
        return redirect('/Envios/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteEnvio/<int:id>')
@login_required
def eliminarEnvio(id):
    D= Envio()
    D.idEnvio = id
    D.eliminar()
    return redirect('/Envios/1')        
#Fin Crud Envios

#Inicio Crud DetallesEnvio
@app.route('/DetallesEnvio/<int:id>')
@login_required
def consultaDetallesEn(id):
    cantA=0;
    D = DetalleEnvio()
    D = D.consultaGeneral()

    E = Envio()
    E = E.consultaGeneral()
    V = Venta()
    V = V.consultaGeneral()

    C = DireccionesClientes()
    C = C.consultaGeneral()

    H = ContactosClientes()
    H = H.consultaGeneral()
    
    for direc in D:
        cantA+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)

    return render_template('/DetallesEnvio/AdministrarDetalle.html',Contactos=H,Direccion=D,Direcciones=C,Envios=E,Ventas=V, PaginasA=cantA,PosicionA=id)

@app.route('/AddDetalleEnvio',methods=['POST'])
@login_required
def guardarDetalleEn():
    try:
        D = DetalleEnvio()
        D.idEnvio = request.form['idEnvio']
        D.idVenta = request.form['idVenta']
        D.idDireccion = request.form['idDireccion']
        D.idContacto = request.form['idContacto']
        D.fechaEntregaPlaneada = request.form['fecha']
        D.peso = request.form['peso']
        D.estatus = request.form['estatus']
        D.insertar()
        return redirect('/DetallesEnvio/1')
    except:
        return 'No hay respuesta a tu peticion'

@app.route('/EditDetalleEnvio/<int:idventa>/<int:idenvio>')
@login_required
def consultarDetalleEn(idventa,idenvio):
    D = DetalleEnvio()
    D = D.consultaIndividual(idventa,idenvio)
    
    C = DireccionesClientes()
    C = C.consultaGeneral()

    H = ContactosClientes()
    H = H.consultaGeneral()

    return render_template('DetallesEnvio/EditDetalle.html',Mantenimiento=D, Direcciones=C,Contactos=H)

@app.route('/DetalleEnvio/modificar', methods=['POST'])
@login_required
def actualizarDetalleEn():
    try:
        D = DetalleEnvio()
        D.idEnvio = request.form['idEnvio']
        D.idVenta = request.form['idVenta']
        D.idDireccion = request.form['idDireccion']
        D.fechaEntregaPlaneada = request.form['fecha']
        D.peso = request.form['peso']
        D.estatus = request.form['estatus']
        D.idContacto = request.form['idContacto']

        D.actualizar()
        return redirect('/DetallesEnvio/1')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteDetalleEnvio/<int:idventa>/<int:idenvio>')
@login_required
def eliminarDetalleEn(idventa,idenvio):
    D= DetalleEnvio()
    D.eliminar(idventa,idenvio)
    return redirect('/DetallesEnvio/1')        
#Fin Crud DetallesEnvio

@app.errorhandler(400)
def error_400(e):
    return render_template('Errores/error404.html',mensaje='La pagina que buscas No Existe en esta plataforma'),400

@app.errorhandler(404)
def error_404(e):
    return render_template('Errores/error404.html',mensaje='La pagina que buscas No Existe en esta plataforma'),404

@app.errorhandler(500)
def error_500(e):
    return render_template('Errores/error500.html',mensaje='Introdujiste información errónea en algunos campos'),500

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

