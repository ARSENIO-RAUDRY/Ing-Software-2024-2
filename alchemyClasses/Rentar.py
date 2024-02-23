from alchemyClasses import db
from flask import Column, Integer, ForeignKey, DateTime
from datetime import date

class Rentar(db.Model):
    __tablename__ = 'rentar'
    id_rentar = Column(Integer,primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_pelicula = Column(Integer, ForeignKey('pelicula.id_pelicula'))
    fecha_renta = Column(DateTime, nullable=True)
    dias_de_renta = Column(Integer)
    estatus = Column(Integer)

    def __str__(self):
        return f'Id Rentar: {self.id_rentar}\nId Usuario: {self.id_usuario}\nId Pelicula: {self.id_pelicula}\nFecha de Renta:{self.fecha_renta}\n Dias de renta:{self.dias_de_renta}\nEstatus:{self.estatus}'
    
    def __init__(self, id_usuario,id_pelicula,fecha_renta=date.today(),dias_de_renta,estatus):
        self.id_usuario = id_usuario
        self.id_pelicula = id_pelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

        
