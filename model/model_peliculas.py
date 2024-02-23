from alchemyClasses.Peliculas import Peliculas
from alchemyClasses import db

def get_peliculas:
    for pelicula in Peliculas.query.all():
        print(f'{pelicula}\n')

def get_pelicula(id_pelicula):
    return Peliculas.query.filter(Peliculas.id_pelicula == id_pelicula).first()

def cambia_nombre(id_pelicula, nuevo_nombre):
    pelicula = get_pelicula(id_pelicula)
    if pelicula != None:
        pelicula.nombre = nuevo_nombre
        db.session.commit()
        return True
    else:
        return False

def elimina_pelicula(id_pelicula):
    pelicula = get_pelicula(id_pelicula)
    if pelicula != None:
        db.session.delete(pelicula)
        db.session.commit()
        return True
    else:
        return False

def elimina_todos_las_peliculas():
    peliculas = Peliculas.query.all()
    for pelicula in peliculas:
        db.session.delete(pelicula)

    db.session.commit()
