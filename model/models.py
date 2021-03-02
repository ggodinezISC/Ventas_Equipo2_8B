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
        db.session.delete(cli)
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
        db.session.delete(aso)
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
        db.session.delete(cult)
        db.session.commit()

    def consultaIndividual(self):
        cult = self.query.get(self.IdCultivo)
        return cult

class Miembro(db.Model):
    __tablename__ = 'Miembros'
    IdCultivo     = Column(Integer, ForeignKey('Cultivos.IdCultivo') , primary_key=True)
    IdAsociacion  = Column(Integer, ForeignKey('Asociaciones.IdAsociacion') , primary_key=True,)
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
        db.session.delete(cult)
        db.session.commit()

    def consultaIndividual(self):
        cult = self.query.get(self.IdCultivo)
        return cult