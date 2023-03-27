from flask_sqlalchemy import SQLAlchemy
import datetime

db= SQLAlchemy()

class Usuario(db.Model):
    __tablename__='usuariolog'
    idUsuarioLog=db.Column(db.Integer,primary_key=True)
    idCliente = db.Column(db.Integer)
    idEmpleado = db.Column(db.Integer)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

class Cliente(db.Model):
    __tablename__='cliente'
    idCliente=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    ape_paterno = db.Column(db.String(50))
    ape_materno = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    estatus = db.Column(db.String(50))


class Empleado(db.Model):
    __tablename__='empleado'
    idEmpleado=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    ape_paterno = db.Column(db.String(50))
    ape_materno = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    estatus = db.Column(db.String(50))



