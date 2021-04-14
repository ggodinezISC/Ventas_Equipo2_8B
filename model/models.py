from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Cliente(UserMixin,db.Model):
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

    def eliminar(self,Estado):
        Edo = self.query.all()
        for est in Edo:
            if(est.idEstado==Estado):
                est.estatus="I"
                db.session.merge(est)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,Estado):
        EDO = self.query.all()
        for est in EDO:
            if(est.idEstado==Estado):
                return est
        else:
            return None
        
class Ciudad(db.Model):
    __tablename__ = 'Ciudades'
    idCiudad   = Column(Integer, primary_key=True)
    idEstado   = Column(Integer, ForeignKey('Estados.idEstado') )
    nombre     = Column(String, nullable=False)
    estatus    = Column(String, nullable=False)
    
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        CIU = self.query.all()
        return CIU

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,Ciudad):
        CUI = self.query.all()
        for est in CIU:
            if(est.idCiudad==Ciudad):
                est.estatus="I"
                db.session.merge(est)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,Ciudad):
        CIU = self.query.all()
        for est in CIU:
            if(est.idCiudad==Ciudad):
                return est
        else:
            return None
            
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

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        DC = self.query.all()
        return DC

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,idDireccion):
        dc = self.query.all()
        for cu in dc:
            if(cu.idDireccion==idDireccion ):
                cu.estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,Direccion):
        DC = self.query.all()
        for cu in DC:
            if(cu.idDireccion==Direccion):
                return cu
        else:
            return None

class Parcela(db.Model):
    __tablename__ = 'Parcelas'
    idParcela        = Column(Integer, primary_key=True)
    idCliente        = Column(Integer, ForeignKey('Clientes.IdCliente') ,nullable=False)
    idCultivo        = Column(Integer, ForeignKey('Cultivos.IdCultivo') , nullable=False)
    idDireccion      = Column(Integer, ForeignKey('DireccionesCliente.idDireccion') , nullable=False)
    extension        = Column(String, nullable=False)
    estatus          = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        parc = self.query.all()
        return parc

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,idParcela):
        parc = self.query.all()
        for cu in parc:
            if(cu.idParcela==idParcela ):
                cu.estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,idParcela):
        parc = self.query.all()
        for cu in parc:
            if(cu.idParcela==idParcela):
                return cu
        else:
            return None

class ContactosClientes(db.Model):
    __tablename__ = 'ContactosCliente'
    idContacto   = Column(Integer, primary_key=True)
    idCliente     = Column(Integer, ForeignKey('Clientes.IdCliente') ,nullable=False)
    nombre         = Column(String, nullable=False)
    telefono        = Column(String, nullable=False)
    email       = Column(String, nullable=False)
    estatus       = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        CC = self.query.all()
        return CC

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,idContacto):
        CC = self.query.all()
        for cu in CC:
            if(cu.idContacto==idContacto ):
                cu.estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,idContacto):
        CC = self.query.all()
        for cu in CC:
            if(cu.idContacto==idContacto):
                return cu
        else:
            return None

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

    def eliminar(self,idUnidadTransporte):
        UT = self.query.all()
        for cu in UT:
            if(cu.idUnidadTransporte==idUnidadTransporte ):
                cu.estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,idUnidadTransporte):
        UT = self.query.all()
        for cu in UT:
            if(cu.idUnidadTransporte==idUnidadTransporte):
                return cu
        else:
            return None

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

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        MAN = self.query.all()
        return MAN

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,idMantenimiento):
        MAN = self.query.all()
        for cu in MAN:
            if(cu.idMantenimiento==idMantenimiento ):
                cu.estatus="I"
                db.session.merge(cu)
                db.session.commit()
        else:
            return None

    def consultaIndividual(self,idMantenimiento):
        MAN = self.query.all()
        for cu in MAN:
            if(cu.idMantenimiento==idMantenimiento):
                return cu
        else:
            return None



