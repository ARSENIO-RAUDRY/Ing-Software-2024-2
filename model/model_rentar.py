from alchemyClasses.Rentar import Rentar
from alchemyClasses import db
import datetime

def get_rentas():
    for renta in Rentar.query.all():
        print(f'{renta}\n')

def get_rentar(id_renta):
    return Rentar.query.filter(Rentar.idRentar == id_renta).first()

def genera_nueva_fecha():
    anio = 0

    while(True):
        try:
            anio = int(input("Ingresa el nuevo año:"))
            if anio <1969 or anio >2024:
                raise ValueError
            else: break

        except ValueError:
            print("Ingresa una fecha valida")

    mes=0
    while(True):
        try:
            mes = int(input("Ingresa el nuevo mes:"))
            if mes <1 or mes>12:
                raise ValueError
            else: break

        except ValueError:
            print("Ingresa una fecha valida")

    dia = 0
    while(True):
        try:
            dia = int(input("Ingresa el nuevo dia:"))
            if dia < 1 or (dia > 28 and mes == 2) or (dia > 31 and mes != 2):
                raise ValueError
            else: break

        except ValueError:
            print("Ingresa una fecha valida")

    return datetime.date(year=anio, month=mes, day=dia)

def cambia_fecha(id_renta, nueva_fecha):
    renta = get_rentar(id_renta)
    if renta != None:
        renta.fecha_renta = nueva_fecha
        db.session.commit()
        return True
    else:
        return False

def elimina_renta(id_renta):
    renta = get_rentar(id_renta)
    if renta != None:
        db.session.delete(renta)
        db.session.commit()
        return True
    else:
        return False

def elimina_todas_las_rentas():
    rentar = Rentar.query.all()
    for renta in rentar:
        db.session.delete(renta)

    db.session.commit()
