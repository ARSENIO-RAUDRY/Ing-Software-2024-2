from sqlalchemy import Column, Integer, String, LargeBinary

from alchemyClasses import db

class Usuarios(db.Model):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key = True)
    nombre = Column(String(200))
    apellido_pat = Column(String(200))
    apellido_mat = Column(String(200))
    password = Column(String(64))
    email = Column(String(500))
    profile_picture = Column(LargeBinary())
    superuser= Column(Int(1))
    
def __str__(self):
    return f'Id Usuario{self.id_usuario}\n Nombre:{self.nombre}\n Apellido Paterno:{self.apellido}'
