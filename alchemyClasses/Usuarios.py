from sqlalchemy import Column, Integer, String, LargeBinary

from alchemyClasses import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key = True)
    nombre = Column(String(200))
    apellido_pat = Column(String(200))
    apellido_mat = Column(String(200))
    password = Column(String(64))
    email = Column(String(500))
    profile_picture = Column(LargeBinary)
    superuser= Column(Integer)
    
    def __init__(self, nombre, apellido_pat, apellido_mat, password, email, profile_picture=None, superuser):
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.password = password
        self.email = email
        self.profile_picture = profile_picture
        self.superuser = superuser
    
    def __str__(self):
        return f'Id Usuario: {self.id_usuario}\nNombre:{self.nombre}\nApellido Paterno:{self.apellido_pat}\nApellido Materno:{self.apellido_mat}\nCorreo:{self.email}'
