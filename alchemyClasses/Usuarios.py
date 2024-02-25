from sqlalchemy import Column, Integer, String, LargeBinary

from alchemyClasses import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key = True)
    nombre = Column(String(200))
    apPat = Column(String(200))
    apMat = Column(String(200))
    password = Column(String(64))
    email = Column(String(500))
    profilePicture = Column(LargeBinary)
    superUser= Column(Integer)
    
    def __init__(self, nombre, apellido_pat, apellido_mat, password, email=None, profile_picture=None, superuser=None):
        self.nombre = nombre
        self.apPat = apellido_pat
        self.apMat = apellido_mat
        self.password = password
        self.email = email
        self.profilePicture = profile_picture
        self.superUser = superuser
    
    def __str__(self):
        return f'Id Usuario: {self.idUsuario}\nNombre:{self.nombre}\nApellido Paterno:{self.apPat}\nApellido Materno:{self.apMat}\nCorreo:{self.email}'
