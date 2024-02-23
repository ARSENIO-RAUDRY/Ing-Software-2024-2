from alchemyClasses.Rentar import Rentar
from alchemyClasses import db

def get_rentar:
    for renta in Rentar.query.all():
        print(f'{renta}\n')

def get_renta(id_renta):
    return Rentar.query.filter(Rentar.id_renta == id_renta).first()

def genera_nueva_fecha():
    anio

def cambia_fecha(id_renta, nueva_fecha):
    renta = get_renta(id_renta)
    if renta != None:
        renta.fecha_renta = nueva_fecha
        db.session.commit()
        return True
    else:
        return False

def elimina_renta(id_renta):
    renta = get_renta(id_renta)
    if renta != None:
        db.session.delete(renta)
        db.session.commit()
        return True
    else:
        return False

def elimina_todos_las_rentas():
    rentar = Rentar.query.all()
    for renta in rentar:
        db.session.delete(renta)

    db.session.commit()
