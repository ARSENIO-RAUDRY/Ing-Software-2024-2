from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar

from model.model_usuarios import *
from model.model_peliculas import *
from model.model_rentar import *
from hashlib import sha256


#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        print(" __  __            _    _ \n|  \\/  |          | |  | |\n| \\  / | ___ _ __ | |  | |\n| |\\/| |/ _ \\ '_ \| |  | |\n| |  | |  __/ | | | |__| |\n|_|  |_|\___|_| |_|\\____/ ")
        print("Operaciones disponibles:")
        print("(1) Consultar los registros de una tabla")
        print("(2) Filtrar los registros de una tabla por Id")
        print("(3) Actualizar el nombre de un registro o modificar la fecha de una renta")
        print("(4) Eliminar un registro por Id o todos los registros")

        operacion = 0

        while(True):
            try:
                operacion = int(input("Elija la operacion a realizar: "))
                if operacion not in [1,2,3,4]:
                    raise ValueError
                else: break
            except ValueError:
                print("Ingrese una opcion valida:")


        if operacion == 1:
            print("Tablas existentes en la base:")
            print("(1) Tabla de Usuarios")
            print("(2) Tabla de Peliculas")
            print("(3) Tabla de Rentas")

            tabla =0

            while(True):
                try:
                    tabla = int(input("Elija la tabla a consultar:"))
                    if tabla not in [1,2,3]:
                        raise ValueError
                    else: break
                except ValueError:
                    print("Ingrese una tabla valida")

            if tabla == 1:
                 print("Tabla de usuarios")
                 get_usuarios()

            elif tabla == 2:
                 print("Tabla de peliculas")
                 get_peliculas()

            elif tabla == 3:
                 print("Tabla de rentas")
                 get_rentas()

                 

        elif operacion == 2:
            print("Tablas existentes en la base:")
            print("(1) Tabla de Usuarios")
            print("(2) Tabla de Peliculas")
            print("(3) Tabla de Rentas")

            tabla =0

            while(True):
                try:
                    tabla = int(input("Elija la tabla del registro a consultar:"))
                    if tabla not in [1,2,3]:
                        raise ValueError
                    else: break
                except ValueError:
                    print("Ingrese una tabla valida")

            if tabla == 1:
                 id_usuario = int(input("Inserte el ID del usuario"))
                 print(f'{get_usuario(id_usuario)}\n')

            elif tabla == 2:
                 id_pelicula = int(input("Inserte el ID de la pelicula"))
                 print(f'{get_pelicula(id_pelicula)}\n')

            elif tabla == 3:
                 id_renta = int(input("Inserte el ID de la renta"))
                 print(f'{get_rentar(id_renta)}\n')

            
        elif operacion == 3:
            print("Tablas existentes en la base:")
            print("(1) Tabla de Usuarios")
            print("(2) Tabla de Peliculas")
            print("(3) Tabla de Rentas")

            tabla =0

            while(True):
                try:
                    tabla = int(input("Elija la tabla del registro que se quiera cambiar el nombre (fecha en caso de Rentas):"))
                    if tabla not in [1,2,3]:
                        raise ValueError
                    else: break
                except ValueError:
                    print("Ingrese una tabla valida")

            if tabla == 1:
                 id_usuario = int(input("Inserte el ID del usuario"))
                 nombre = input("Ingresa el nuevo nombre del Usuario:")
                 if cambia_nombre_usuario(id_usuario, nombre) == False:
                     print("Entrada no valida, nombre sin cambiar")

                 else:
                     print("Nombre cambiado")

            elif tabla == 2:
                 id_pelicula = int(input("Inserte el ID de la pelicula"))
                 nombre = input("Ingresa el nuevo nombre de la Pelicula:")
                 if cambia_nombre_pelicula(id_pelicula, nombre) == False:
                     print("Entrada no valida, nombre sin cambiar")

                 else:
                     print("Nombre cambiado")

            elif tabla == 3:
                 id_renta = int(input("Inserte el ID de la renta"))
                 nueva_fecha = genera_nueva_fecha()
                 if cambia_fecha(id_renta, nueva_fecha) == False:
                     print("Entrada no valida, Fecha sin cambiar")

                 else:
                     print("Fecha cambiado")

            
        elif operacion == 4:
            print("Que desea eliminar?")
            print("(1) Un registro")
            print("(2) Todos los registros de una tabla")

            eliminar = 0

            while(True):
                try:
                    eliminar = int(input("Inserte la opcion"))
                    if eliminar not in [1,2]:
                        raise ValueError
                    else: break
                except ValueError:
                    print("Elija una opción valida")

            if eliminar == 1:
                print("Tablas existentes en la base:")
                print("(1) Tabla de Usuarios")
                print("(2) Tabla de Peliculas")
                print("(3) Tabla de Rentas")

                tabla =0                
                while(True):
                    try:
                        tabla = int(input("Elija la tabla del registro que se quiera cambiar el nombre (fecha en caso de Rentas):"))
                        if tabla not in [1,2,3]:
                            raise ValueError
                        else: break
                    except ValueError:
                        print("Ingrese una tabla valida")

                if tabla == 1:
                     id_usuario = int(input("Id del usuario:"))
                     elimina_usuario(id_usuario)

                elif tabla == 2:
                     id_pelicula = int(input("Id de la pelicula"))
                     elimina_pelicula(id_pelicula)

                elif tabla == 3:
                     id_renta = int(input("Id de la renta"))
                     elimina_renta(id_renta)
                
                
            elif eliminar == 2:
                print("Tablas existentes en la base:")
                print("(1) Tabla de Usuarios")
                print("(2) Tabla de Peliculas")
                print("(3) Tabla de Rentas")

                tabla =0                
                while(True):
                    try:
                        tabla = int(input("Elija la tabla del registro que se quiera cambiar el nombre (fecha en caso de Rentas):"))
                        if tabla not in [1,2,3]:
                            raise ValueError
                        else: break
                    except ValueError:
                        print("Ingrese una tabla valida")

                if tabla == 1:
                     id_usuario = int(input("Id del usuario:"))
                     elimina_todos_los_usuario()

                elif tabla == 2:
                     id_pelicula = int(input("Id de la pelicula"))
                     elimina_todas_las_peliculas()

                elif tabla == 3:
                     id_renta = int(input("Id de la renta"))
                     elimina_todas_las_rentas()                
