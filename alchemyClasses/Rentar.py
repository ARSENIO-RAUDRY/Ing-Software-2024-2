from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

from alchemyClasses import db
from alchemyClasses import Usuarios
from alchemyClasses import Peliculas


class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer,primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    idPelicula = Column(Integer, ForeignKey('pelicula.id_pelicula'))
    fecha_renta = Column(DateTime, nullable=True)
    dias_de_renta = Column(Integer)
    estatus = Column(Integer)
    
    def __init__(self, id_usuario,id_pelicula,fecha_renta,dias_de_renta=5,estatus=0):
        self.idUsuario = id_usuario
        self.idPelicula = id_pelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

        
    def __str__(self):
        return f'Id Rentar: {self.id_rentar}\nId Usuario: {self.id_usuario}\nId Pelicula: {self.id_pelicula}\nFecha de Renta:{self.fecha_renta}\n Dias de renta:{self.dias_de_renta}\nEstatus:{self.estatus}'
