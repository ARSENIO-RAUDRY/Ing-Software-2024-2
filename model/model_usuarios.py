from alchemyClasses.Usuarios import Usuarios
from alchemyClasses import db

def get_usuarios():
    for usuario in Usuarios.query.all():
        print(f'{usuario}\n')

def get_usuario(id_usuario):
    return Usuarios.query.filter(Usuarios.id_usuario == id_usuario).first()

def cambia_nombre_usuario(id_usuario, nuevo_nombre):
    usuario = get_usuario(id_usuario)
    if usuario != None:
        usuario.nombre = nuevo_nombre
        db.session.commit()
        return True
    else:
        return False

def elimina_usuario(id_usuario):
    usuario = get_usuario(id_usuario)
    if usuario != None:
        db.session.delete(usuario)
        db.session.commit()
        return True
    else:
        return False

def elimina_todos_los_usuarios():
    usuarios = Usuarios.query.all()
    for usuario in usuarios:
        db.session.delete(usuario)

    db.session.commit()
