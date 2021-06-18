from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from flask_login import UserMixin
from sqlalchemy.orm import relationship, selectin_polymorphic

db = SQLAlchemy()

class Empleado(UserMixin,db.Model):
    __tablename__ = 'Empleados'
    idEmpleado = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    apellidoPaterno = Column(String, nullable=False)
    apellidoMaterno = Column(String, nullable=False)
    sexo = Column(String, nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    curp = Column(String, nullable=False)
    estadoCivil = Column(String, nullable=False)
    fechaContratacion = Column(Date, nullable=False)
    salarioDiario = Column(Float, nullable=False)
    nss = Column(String, nullable=False)
    diasVacaciones = Column(Integer, nullable=False)
    diasPermiso = Column(Integer, nullable=False)
    fotografia = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    colonia = Column(String, nullable=False)
    codigoPostal= Column(String, nullable=False)
    escolaridad = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    email = Column(String, nullable=False)
    passwor = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    estatus = Column(String, nullable=False)
    idDepartamento = Column(Integer, nullable=False)
    idPuesto = Column(Integer, nullable=False)
    idCiudad = Column(Integer, nullable=False)
    idSucursal = Column(Integer, nullable=False)
    idTurno = Column(Integer, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        cli = self.query.all()
        return cli
    
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    
    def eliminar(self):
        cli = self.consultaIndividual()
        cli.estatus="I"
        db.session.merge(cli)
        db.session.commit()
    
    def consultaIndividual(self):
        cli = self.query.get(self.idEmpleado)
        return cli

    def validarPassword(self, Password):
        pwd = self.query.filter_by(passwor=Password).first()
        return pwd
    
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.idEmpleado
    def validar(self, Email, Password):
        cli = Empleado.query.filter_by(email=Email).first()
        if cli != None:
            if cli.validarPassword(Password):
                return cli
        else:
            return None

class Cliente(UserMixin, db.Model):
    __tablename__ = 'Clientes'
    IdCliente = Column(Integer, primary_key=True)
    Nombre = Column(String, nullable=False)
    RazonSocial = Column(String, nullable=False)
    LimiteCredito = Column(Float, nullable=False)
    Rfc = Column(String, nullable=False)
    Telefono = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Password = Column(String, nullable=False)
    Tipo = Column(String, nullable=False)
    Estatus = Column(String, nullable=False)
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        cli = self.query.all()
        return cli
    
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    
    def eliminar(self):
        cli = self.consultaIndividual()
        cli.Estatus="I"
        db.session.merge(cli)
        db.session.commit()
    
    def consultaIndividual(self):
        cli = self.query.get(self.IdCliente)
        return cli
    
    def validarPassword(self, Password):
        pwd = self.query.filter_by(Password=Password).first()
        return pwd
    
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.IdCliente
    def validar(self, Email, Password):
        cli = Cliente.query.filter_by(Email=Email).first()
        if cli != None:
            if cli.validarPassword(Password):
                return cli
        else:
            return None

class Asociacion(db.Model):
    __tablename__ = 'Asociaciones'
    IdAsociacion = Column(Integer, primary_key=True)
    Nombre = Column(Integer, nullable=False)
    Estatus = Column(String, nullable=False)


    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        aso = self.query.all()
        return aso

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        aso = self.consultaIndividual()
        aso.Estatus="I"
        db.session.merge(aso)
        db.session.commit()

    def consultaIndividual(self):
        aso = self.query.get(self.IdAsociacion)
        return aso

class Cultivo(db.Model):
    __tablename__ = 'Cultivos'
    IdCultivo =  Column(Integer, primary_key=True)
    Nombre =        Column(String, nullable=False)
    CostoAsesoria = Column(Float, nullable=False)
    Estatus       = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        cult = self.query.all()
        return cult

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        cult = self.consultaIndividual()
        cult.Estatus="I"
        db.session.merge(cult)
        db.session.commit()

    def consultaIndividual(self):
        cult = self.query.get(self.IdCultivo)
        return cult

class Miembro(db.Model):
    __tablename__ = 'Miembros'
    IdCliente     = Column(Integer, ForeignKey('Clientes.IdCliente') , primary_key=True)
    IdAsociacion  = Column(Integer, ForeignKey('Asociaciones.IdAsociacion') , primary_key=True,)
    FechaIncorporacion = Column(Date, nullable=False)
    Estatus       = Column(String, nullable=False)
    Cliente=relationship('Cliente', foreign_keys=[IdCliente])
    Asociacion=relationship('Asociacion', foreign_keys=[IdAsociacion])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        cult = self.query.all()
        return cult

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,Cliente,Asociacion):
        cult = self.query.all()
        for cu in cult:
            if(cu.IdCliente==Cliente and cu.IdAsociacion==Asociacion):
                cu.Estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,Cliente,Asociacion):
        cult = self.query.all()
        for cu in cult:
            if(cu.IdCliente==Cliente and cu.IdAsociacion==Asociacion):
                return cu
        else:
            return None

class Estado(db.Model):
    __tablename__ = 'Estados'
    idEstado   = Column(Integer, primary_key=True)
    nombre         = Column(String, nullable=False)
    siglas        = Column(String, nullable=False)
    estatus       = Column(String, nullable=False)
    
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        Edo = self.query.all()
        return Edo

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idEstado)
        return cli
        
class Ciudad(db.Model):
    __tablename__ = 'Ciudades'
    idCiudad   = Column(Integer, primary_key=True)
    idEstado   = Column(Integer, ForeignKey('Estados.idEstado') )
    nombre     = Column(String, nullable=False)
    estatus    = Column(String, nullable=False)
    Estado=relationship('Estado', foreign_keys=[idEstado])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        CIU = self.query.all()
        return CIU

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idCiudad)
        return cli
            
class DireccionesClientes(db.Model):
    __tablename__ = 'DireccionesCliente'
    idDireccion   = Column(Integer, primary_key=True)
    idCliente     = Column(Integer, ForeignKey('Clientes.IdCliente') ,nullable=False)
    idCiudad      = Column(Integer, ForeignKey('Ciudades.idCiudad') , nullable=False)
    calle         = Column(String, nullable=False)
    numero        = Column(String, nullable=False)
    colonia       = Column(String, nullable=False)
    codigoPostal  = Column(String, nullable=False)
    tipo          = Column(String, nullable=False)
    estatus       = Column(String, nullable=False)
    Cliente=relationship('Cliente', foreign_keys=[idCliente])
    Ciudad=relationship('Ciudad', foreign_keys=[idCiudad])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        DC = self.query.all()
        return DC

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idDireccion)
        return cli

class Parcela(db.Model):
    __tablename__ = 'Parcelas'
    idParcela        = Column(Integer, primary_key=True)
    idCliente        = Column(Integer, ForeignKey('Clientes.IdCliente') ,nullable=False)
    idCultivo        = Column(Integer, ForeignKey('Cultivos.IdCultivo') , nullable=False)
    idDireccion      = Column(Integer, ForeignKey('DireccionesCliente.idDireccion') , nullable=False)
    extension        = Column(String, nullable=False)
    estatus          = Column(String, nullable=False)
    Cliente=relationship('Cliente', foreign_keys=[idCliente])
    Cultivo=relationship('Cultivo', foreign_keys=[idCultivo])
    Direccion=relationship('DireccionesClientes', foreign_keys=[idDireccion])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        parc = self.query.all()
        return parc

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idParcela)
        return cli

class ContactosClientes(db.Model):
    __tablename__ = 'ContactosCliente'
    idContacto   = Column(Integer, primary_key=True)
    idCliente     = Column(Integer, ForeignKey('Clientes.IdCliente') ,nullable=False)
    nombre         = Column(String, nullable=False)
    telefono        = Column(String, nullable=False)
    email       = Column(String, nullable=False)
    estatus       = Column(String, nullable=False)
    Cliente=relationship('Cliente', foreign_keys=[idCliente])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        CC = self.query.all()
        return CC

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idContacto)
        return cli

class UnidadesTransportes(db.Model):
    __tablename__ = 'UnidadesTransporte'
    idUnidadTransporte     = Column(Integer, primary_key=True)    
    placas = Column(String, nullable=False)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)
    capacidad = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    estatus = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        UT = self.query.all()
        return UT

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idUnidadTransporte)
        return cli

class Mantenimiento(db.Model):
    __tablename__ = 'Mantenimientos'
    idMantenimiento     = Column(Integer, primary_key=True)
    idUnidadTransporte  = Column(Integer, ForeignKey('UnidadesTransporte.idUnidadTransporte') ,nullable=False)
    fechaInicio         = Column(Date, nullable=False)
    fechaFin            = Column(Date, nullable=False)
    taller              = Column(String, nullable=False)
    costo               = Column(Integer, nullable=False)
    comentarios         = Column(String, nullable=False)
    tipo                = Column(String, nullable=False)
    estatus             = Column(String, nullable=False)
    Transporte=relationship('UnidadesTransportes', foreign_keys=[idUnidadTransporte])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idMantenimiento)
        return cli

class History(db.Model):
    __tablename__ = 'Historial'
    IdHistorial     = Column(Integer, primary_key=True)
    Nombre          = Column(String ,nullable=False)
    Email           = Column(Date, nullable=False)
   

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()    

    def consultaIndividual(self):
        cli = self.query.get(self.IdHistorial)
        return cli

class Venta(db.Model):
    __tablename__ = 'Ventas'
    idVenta  = Column(Integer, primary_key=True)
    idCliente = Column(Integer, ForeignKey('Clientes.IdCliente'),nullable=False)
    idSucursal = Column(Integer,ForeignKey('Sucursales.idSucursal'), nullable=False)
    idEmpleado = Column(Integer,ForeignKey('Empleados.idEmpleado'), nullable=False)
    fecha    = Column(Date, nullable=False)
    subtotal = Column(Float, nullable=False)
    iva = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    cantPagada = Column(Float, nullable=False)
    comentarios = Column(String, nullable=False)
    estatus = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    Cliente=relationship('Cliente', foreign_keys=[idCliente])
    Sucursal=relationship('Sucursal', foreign_keys=[idSucursal])
    Empleado=relationship('Empleado', foreign_keys=[idEmpleado])
    

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idVenta)
        return cli

class VentasDetalle(db.Model):
    __tablename__ = 'VentaDetalle'
    idVentaDetalle = Column(Integer, primary_key=True)
    idVenta = Column(Integer, ForeignKey('Ventas.idVenta'), nullable=False)
    idPresentacion = Column(Integer, ForeignKey('PresentacionesProducto.idPresentacion'), nullable=False)
    precioVenta = Column(Float, nullable=False)
    cantidad = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    estatus = Column(String, nullable=False)
    Venta=relationship('Venta', foreign_keys=[idVenta])
    Presentacion=relationship('PresentacionProducto', foreign_keys=[idPresentacion])


    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idVentaDetalle)
        return cli

class Cobro(db.Model):
    __tablename__ = 'Cobros'
    idCobro = Column(Integer, primary_key=True)
    fecha   = Column(Date, nullable=False)
    importe = Column(Float, nullable=False)
    idVenta = Column(Integer,  ForeignKey('Ventas.idVenta') ,nullable=False)
    estatus = Column(String, nullable=False)
    Venta=relationship('Venta', foreign_keys=[idVenta])


    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idCobro)
        return cli

class Envio(db.Model):
    __tablename__ = 'Envios'
    idEnvio = Column(Integer, primary_key=True)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=False)
    idUnidadTransporte = Column(Integer, ForeignKey('UnidadesTransporte.idUnidadTransporte') ,nullable=False)
    pesoTotal = Column(Float, nullable=False)
    estatus = Column(String, nullable=False)
    Unidad=relationship('UnidadesTransportes', foreign_keys=[idUnidadTransporte])
    

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idEnvio)
        return cli

class DetalleEnvio(db.Model):
    __tablename__ = 'DetallesEnvio'
    idEnvio              = Column(Integer, ForeignKey('Envios.idEnvio'), primary_key=True)
    idVenta              = Column(Integer, ForeignKey('Ventas.idVenta'), primary_key=True)
    idDireccion          = Column(Integer,ForeignKey('DireccionesCliente.idDireccion'), nullable=False)
    fechaEntregaPlaneada = Column(Date, nullable=False)
    peso                 = Column(Float, nullable=False)
    estatus              = Column(String, nullable=False)
    idContacto           = Column(Integer, ForeignKey('ContactosCliente.idContacto') ,nullable=False)
    Venta=relationship('Venta', foreign_keys=[idVenta])
    Direccion=relationship('DireccionesClientes', foreign_keys=[idDireccion])
    Contacto=relationship('ContactosClientes', foreign_keys=[idContacto])

    
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,idEnvio,idVenta):
        cult = self.query.all()
        for cu in cult:
            if(cu.idEnvio==idEnvio and cu.idVenta==idVenta):
                cu.estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None
        

    def consultaIndividual(self,idVenta,idEnvio):
         cult = self.query.all()
         for cu in cult:
            if(cu.idVenta==idVenta and cu.idEnvio==idEnvio):
                return cu

class Laboratorio(db.Model):
    __tablename__ = 'Laboratorios'
    idLaboratorio = Column(Integer, primary_key=True)
    nombre = Column(String, primary_key=True)
    origen = Column(String, primary_key=True)
    estatus = Column(String, primary_key=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idLaboratorio)
        return cli 

class Categoria(db.Model):
    __tablename__ = 'Categorias'
    idCategoria = Column(Integer, primary_key=True)
    nombre  = Column(String, nullable=False)
    estatus = Column(String, nullable=False)


    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idCategoria)
        return cli 

class Sucursal(db.Model):
    __tablename__ = 'Sucursales'
    idSucursal = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    colonia = Column(String, nullable=False)
    codigoPostal = Column(String, nullable=False)
    presupuesto = Column(Float, nullable=False)
    estatus = Column(String, nullable=False)
    idCiudad = Column(Integer,  ForeignKey('Ciudades.idCiudad'), nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idSucursal)
        return cli 

class Producto(db.Model):
    __tablename__ = 'Productos'
    idProducto = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion  = Column(String, nullable=False)
    ingredienteActivo = Column(String, nullable=False)
    bandaToxicologica = Column(String, nullable=False)
    aplicacion = Column(String, nullable=False)
    uso = Column(String, nullable=False)
    estatus  = Column(String, nullable=False)
    idLaboratorio  = Column(Integer, ForeignKey('Laboratorios.idLaboratorio'), nullable=False)
    idCategoria  = Column(Integer, ForeignKey('Categorias.idCategoria'), nullable=False)
    
    Categoria = relationship('Categoria', foreign_keys=[idCategoria])
    Laboratorio = relationship('Laboratorio', foreign_keys=[idLaboratorio])


    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idProducto)
        return cli 

class UnidadMedida(db.Model):
    __tablename__ = 'UnidadesMedida'
    idUnidad = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    siglas  = Column(String, nullable=False)
    estatus = Column(String, nullable=False)


    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idUnidad)
        return cli 

class Empaque(db.Model):
    __tablename__ = 'Empaques'
    idEmpaque = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    capacidad = Column(Float, nullable=False)
    estatus = Column(String, nullable=False)
    idUnidad = Column(Integer, ForeignKey('UnidadesMedida.idUnidad'), nullable=False)
    Unidad=relationship('UnidadMedida', foreign_keys=[idUnidad])
    


    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idEmpaque)
        return cli 

class PresentacionProducto(db.Model):
    __tablename__ = 'PresentacionesProducto'
    idPresentacion = Column(Integer, primary_key=True)
    precioCompra = Column(Float, nullable=False)
    precioVenta = Column(Float, nullable=False)
    puntoReorden = Column(Float, nullable=False)
    idProducto = Column(Integer, ForeignKey('Productos.idProducto'), nullable=False)
    idEmpaque  = Column(Integer, ForeignKey('Empaques.idEmpaque'), nullable=False)
    Producto=relationship('Producto', foreign_keys=[idProducto])
    Empaque=relationship('Empaque', foreign_keys=[idEmpaque])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idPresentacion)
        return cli 

class Oferta(db.Model):
    __tablename__ = 'Ofertas'
    idOferta = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion  = Column(String, nullable=False)
    porDescuento  = Column(Float, nullable=False)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=False)
    canMinProductos = Column(Integer, nullable=False)
    estatus = Column(String, nullable=False)
    idPresentacion = Column(Integer, ForeignKey('PresentacionesProducto.idPresentacion'), nullable=False)

    
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idOferta)
        return cli 

class ExistenciaSucursal(db.Model):
    __tablename__ = 'ExistenciasSucursal'
    idPresentacion = Column(Integer, ForeignKey('PresentacionesProducto.idPresentacion'), primary_key=True)
    idSucursal = Column(Integer, ForeignKey('Sucursales.idSucursal'), primary_key=True)
    cantidad = Column(Integer, nullable=False)
    Presentacion = relationship('PresentacionProducto', foreign_keys=[idPresentacion])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,presentacion,sucursal):
        cult = self.query.all()
        for cu in cult:
            if(cu.idPresentacion==presentacion and cu.idSucursal==sucursal):
                cu.cantidad=0
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,presentacion,sucursal):
        cult = self.query.all()
        for cu in cult:
            if(cu.idPresentacion==presentacion and cu.idSucursal==sucursal):
                return cu
        else:
            return None

class Tripulantes(db.Model):
    __tablename__ = 'Tripulacion'
    idEmpleado = Column(Integer, ForeignKey('Empleados.idEmpleado'), primary_key=True)
    idEnvio = Column(Integer, ForeignKey('Envios.idEnvio'), primary_key=True)
    rol = Column(String, nullable=False)
    estatus = Column(String, nullable=False)
    Empleado = relationship('Empleado', foreign_keys=[idEmpleado])
    Envio = relationship('Envio', foreign_keys=[idEnvio])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,Empleado,Envio):
        cult = self.query.all()
        for cu in cult:
            if(cu.idEmpleado==Empleado and cu.idEnvio==Envio):
                cu.estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,Empleado,Envio):
        cult = self.query.all()
        for cu in cult:
            if(cu.idEmpleado==Empleado and cu.idEnvio==Envio):
                return cu
        else:
            return None

class OfertaAsociacion(db.Model):
    __tablename__ = 'OfertasAsociacion'
    idAsosiacion = Column(Integer, ForeignKey('Asociaciones.IdAsociacion'), primary_key=True)
    idOferta = Column(Integer, ForeignKey('Ofertas.idOferta'), primary_key=True)
    estatus = Column(String, nullable=False)
    Asociacion = relationship('Asociacion', foreign_keys=[idAsosiacion])
    Oferta = relationship('Oferta', foreign_keys=[idOferta])

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, Asociacion, Oferta):
        cult = self.query.all()
        for cu in cult:
            if(cu.idAsosiacion==Asociacion and cu.idOferta==Oferta):
                cu.estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,Asociacion, Oferta):
        cult = self.query.all()
        for cu in cult:
            if(cu.idAsosiacion==Asociacion and cu.idOferta==Oferta):
                return cu
        else:
            return None

class Asesoria(db.Model):
    __tablename__ = 'Asesorias'
    idAsesoria = Column(Integer, primary_key=True)
    idParcela = Column(Integer, ForeignKey('Parcelas.idParcela'), nullable=False)
    idEmpleado = Column(Integer,ForeignKey('Empleados.idEmpleado'), nullable=False)
    idUnidadTransporte = Column(Integer, ForeignKey('UnidadesTransporte.idUnidadTransporte') ,nullable=False)
    fecha = Column(Date, nullable=False)
    comentarios  = Column(String, nullable=False)
    estatus  = Column(String, nullable=False)
    costo = Column(Float, nullable=False)
    Parcela=relationship('Parcela', foreign_keys=[idParcela])
    Empleado=relationship('Empleado', foreign_keys=[idEmpleado])
    Unidad=relationship('UnidadesTransportes', foreign_keys=[idUnidadTransporte])

    
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        est = self.consultaIndividual()
        est.estatus="I"
        db.session.merge(est)
        db.session.commit()

    def consultaIndividual(self):
        cli = self.query.get(self.idAsesoria)
        return cli 
