from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from model.models import db, Cliente, Cultivo,Asociacion,Miembro,Estado,Ciudad,DireccionesClientes,Parcela,ContactosClientes,UnidadesTransportes,Mantenimiento
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
@app.route('/Estados')
@login_required
def consultaEstados():
    E = Estado()
    E = E.consultaGeneral()
    return render_template('/Estados/AdministrarEstado.html',Estado=E)

@app.route('/AddEstado',methods=['POST'])
@login_required
def guardarEstado():
    try:
        E = Estado()
        E.nombre = request.form['Nombre']
        E.siglas = request.form['Siglas']
        E.estatus = request.form['Estatus']
        E.insertar()
        return redirect(url_for('consultaEstados'))
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
        return redirect(url_for('consultaEstados'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteEstado/<int:id>')
@login_required
def eliminarEstado(id):
    E = Estado()
    E.idEstado = id
    E.eliminar()
    return redirect(url_for('consultaEstados'))        
#Fin Crud Estados


#Inicio Crud Ciudades
@app.route('/Ciudades')
@login_required
def consultaCiudades():
    C = Ciudad()
    C = C.consultaGeneral()
    E = Estado()
    E = E.consultaGeneral()
    return render_template('/Ciudades/AdministrarCiudad.html',Ciudades=C,Estados=E)

@app.route('/AddCiudad',methods=['POST'])
@login_required
def guardarCiudad():
    try:
        C = Ciudad()
        C.idEstado = request.form['IdEstado']
        C.nombre = request.form['Nombre']
        C.estatus = request.form['Estatus']
        C.insertar()
        return redirect(url_for('consultaCiudades'))
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
        return redirect(url_for('consultaCiudades'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteCiudad/<int:id>')
@login_required
def eliminarCiudad(id):
    C = Ciudad()
    C.idCiudad = id
    C.eliminar()
    return redirect(url_for('consultaCiudades'))        
#Fin Crud Ciudades

#Inicio Crud DireccionesClientes
@app.route('/DireccionesClientes/<int:id>/<int:id2>')
@login_required
def consultaDirecciones(id,id2):
    cantA=0;cantB=0;
    D = DireccionesClientes()
    D = D.consultaGeneral()
    E = Cliente()
    E = E.consultaGeneral()
    for direc in D:
        if(direc.estatus=="A"):
            cantA+=1
        else:
            cantB+=1
    if(cantA%5!=0):
        cantA= int(cantA/5)
        cantA+=1 
    else:
        cantA= int(cantA/5)
    
    if(cantB%5!=0):
        cantB= int(cantB/5)
        cantB+=1 
    else:
        cantB= int(cantB/5)
    
    
    F = Ciudad()
    F = F.consultaGeneral()
    return render_template('/DireccionesClientes/AdministrarDireccion.html',Direccion=D,Clientes=E,Ciudad=F,PaginasA=cantA,PaginasB=cantB,PosicionA=id,PosicionB=id2)

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
        if(D.numero<=0):
            return  render_template('Errores/error500.html',mensaje='Número no válido')
        D.insertar()
        return redirect('/DireccionesClientes/1/1')
    except:
        return 'No se guardó la información'

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
        if(D.numero<=0):
            return  render_template('Errores/error500.html',mensaje='Número no válido')
        D.actualizar()
        return redirect('/DireccionesClientes/1/')
    except:
        return 'No se actualizó la información'

@app.route('/DeleteDireccion/<int:id>')
@login_required
def eliminarDireccion(id):
    D= DireccionesClientes()
    D.idDireccion = id
    D.eliminar()
    return redirect('/DireccionesClientes/1/1')        
#Fin Crud DireccionesClientes

#Inicio Crud Parcelas
@app.route('/Parcelas')
@login_required
def consultaParcelas():
    D = Parcela()
    D = D.consultaGeneral()
    E = Cliente()
    E = E.consultaGeneral()
    F = Cultivo()
    F = F.consultaGeneral()
    G = DireccionesClientes()
    G = G.consultaGeneral()
    return render_template('/Parcelas/AdministrarParcela.html',Parcela=D,Clientes=E,Cultivo=F,Direccion=G)

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
        if(D.extension<=0):
            return  render_template('Errores/error500.html',mensaje='extensión no válida') 
        D.insertar()
        return redirect(url_for('consultaParcelas'))
    except:
        return 'No se guardó la información'

@app.route('/EditParcela/<int:id>')
@login_required
def consultarParcela(id):
    D = Parcela()
    D.idParcela = id
    E = Cliente()
    E = E.consultaGeneral()
    F = Cultivo()
    F = F.consultaGeneral()
    G = DireccionesClientes()
    G = G.consultaGeneral()
    D = D.consultaIndividual()
    return render_template('Parcelas/EditParcela.html', Parcela=D, Clientes=E,Cultivo=F,Direccion=G)

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
        if(D.extension<=0):
            return  render_template('Errores/error500.html',mensaje='extensión no válida') 
        D.actualizar()
        return redirect(url_for('consultaParcelas'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteParcela/<int:id>')
@login_required
def eliminarParcela(id):
    D= Parcela()
    D.idParcela = id
    D.eliminar()
    return redirect(url_for('consultaParcelas'))        
#Fin Crud Parcelas


#Inicio Crud ContactosCliente
@app.route('/ContactosClientes')
@login_required
def consultaContactos():
    D = ContactosClientes()
    D = D.consultaGeneral()
    C = Cliente()
    C = C.consultaGeneral()
    return render_template('/ContactosClientes/AdministrarContacto.html',Contacto=D,Cliente=C)

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

        regex = "^(\d{10}$)"    
        if(re.match(regex,str(D.telefono))==None):
            return  render_template('Errores/error500.html',mensaje='teléfono no válido')  
        D.insertar()
        return redirect(url_for('consultaContactos'))
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
        return redirect(url_for('consultaContactos'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteContacto/<int:id>')
@login_required
def eliminarContacto(id):
    D= ContactosClientes()
    D.idContacto = id
    D.eliminar()
    return redirect(url_for('consultaContactos'))        
#Fin Crud ContactosCliente


#Inicio Crud UnidadesTransporte
@app.route('/UnidadesTransporte')
@login_required
def consultaUnidades():
    D = UnidadesTransportes()
    D = D.consultaGeneral()
    return render_template('/UnidadesTransporte/AdministrarUnidad.html',Unidades=D)

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

        regex = "^(\d{4}$)"   
        if(re.match(regex,str(D.anio))==None):
            return  render_template('Errores/error500.html',mensaje='año no válido DDDD')
          
        
        if(int (D.capacidad)<=0):
            return  render_template('Errores/error500.html',mensaje='capacidad no válida')

        D.insertar()
        return redirect(url_for('consultaUnidades'))
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
        return redirect(url_for('consultaUnidades'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteUnidad/<int:id>')
@login_required
def eliminarUnidad(id):
    D= UnidadesTransportes()
    D.idUnidadTransporte = id
    D.eliminar()
    return redirect(url_for('consultaUnidades'))        
#Fin Crud UnidadesTransporte


#Inicio Crud Mantenimiento
@app.route('/Mantenimientos')
@login_required
def consultaMantenimientos():
    D = Mantenimiento()
    D = D.consultaGeneral()
    F = UnidadesTransportes()
    F = F.consultaGeneral()
    return render_template('/Mantenimientos/AdministrarMantenimiento.html',Mantenimientos=D,Unidades=F)

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
        
        if(D.fechaFin>=D.fechaInicio):
            return  render_template('Errores/error500.html',mensaje='capacidad no válida')  
        if(int (D.costo)>0):
            return  render_template('Errores/error500.html',mensaje='capacidad no válida')

        D.insertar()
        return redirect(url_for('consultaMantenimientos'))
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
        if(D.fechaFin>=D.fechaInicio):
            return  render_template('Errores/error500.html',mensaje='capacidad no válida')  
        if(int(D.costo)>=0):
            return  render_template('Errores/error500.html',mensaje='capacidad no válida')
        D.actualizar()
        return redirect(url_for('consultaMantenimientos'))
    except:
        return 'No se actualizó la información'

@app.route('/DeleteMantenimiento/<int:id>')
@login_required
def eliminarMantenimiento(id):
    D= Mantenimiento()
    D.idMantenimiento = id
    D.eliminar()
    return redirect(url_for('consultaMantenimientos'))        
#Fin Crud Mantenimiento


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

