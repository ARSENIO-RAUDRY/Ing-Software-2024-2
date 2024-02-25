from sqlalchemy import Column, Integer, String, LargeBinary

from alchemyClasses import db

class Peliculas(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key = True)
    nombre = Column(String(200))
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer)

    def __init__(self, nombre, genero=None, duracion=None, inventario=5):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario
    
    def __str__(self):
        return f'Id Pelicula: {self.idPelicula}\nNombre:{self.nombre}\nGenero:{self.genero}\nDuracion:{self.duracion}\nInventario:{self.inventario}'
