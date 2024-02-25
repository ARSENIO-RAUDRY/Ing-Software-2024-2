import pymysql.cursors
import random
import datetime

connection = pymysql.connect(host='localhost',
                            user='lab',
                            password='Developer123!',
                            db='lab_ing_software',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

nombres = ["Tony","Asahel","Emilio","Arturo","Alberto","Eduardo","Angel","David","Lluvia","Bill","Aaron","Jose","Italia","Renata","Dahlia","Tamai","Octavio","Eugenio","Joao","Fernando","Valentina","Fabian","Misael","Rafael","Omar","Diana","Ashley","Jaime","Daniel","Abraham","Aquiles"]
apellidos =["Ramirez","Lazo","Blancas","Coronado","Preciado","Meyer","Celano","Aprieto","Griffin","Benavides","Reyes","Parra","Lerma","Rocha","Arjona","Ortega","Pacheco","Binladen","Gonzalez","Main","Cerezo","Penaloza","Shamash","Rooney","Cosby","Cascajo","Davis","Wilson","Ortega","Garcia","Pelaez","Granados","Quiroz","Smith","Hernandez","Tiburcio","Evangelista","Castanon","Mora","Estrada","Hitler","Vacheron","Restrepo","Urbide","Urbina","Flores","Fong","Grahue","Ramirez","Revilla","Mendoza","Saavedra","Islas","Falcon","Brito","Vidal","Diaz","Marquez","Marley"]
nombres_peliculas = ["La mataviejitas","La toalla del mojado","Efrain Origins","Hardly Queef","Black to the future","Read Me No More","Man","Jonkler","Canek superestrella","Fer Fong contraataca","La decepcion de Arjona","La caida de Edgar","La pizza de la discordia","Kung Pow 2","Desmadre Callejero","Las metricas del soware","Ant Man in Chimalhuacan","Harry Potter y el Codigo Penal del Estado de Mexico","Rapido y Furi8","Jesus Cazavampiros","FC Hotel","Adam's Sandler Roots","Man Begins","The dark man rises","Suicide Squads kills Seguridad UNAM","Sharknado 666","El eterno resplandor de una linterna sin pilas","Min y Max"]

correos = ["@gmail.com","@ciencias.una.mx","@telehit.com","@yahoo.com","@proton.me","@family.guy.com","@ipn.gob","@televisa.mx","@azteca.mx","@netflix.com","@outlook.com","@hotmail.com"]

generos = ["Fantasia", "Terror Abuelita Miedo", "Cienciologia", "Shmunguss", "Puro ritmo", "Distrito Comedia", "Animacion Coreana", "Basado en Hechos Hiper-reales"]


# 1 Funcion que agrega un registro en cada tabla
def inserta(connection):
    with connection.cursor() as cursor:
        #Inserta Usuario
        nombre = random.choice(nombres)
        apellidopat = random.choice(apellidos)
        apellidomat = random.choice(apellidos)
        correo = nombre + apellidomat + str(random.randint(0,999)) + random.choice(correos)
        password = nombre + "es lo maximo"

        cursor.execute("INSERT INTO `usuarios` (`nombre`,`apPat`,`apMat`,`password`,`email`,`superuser`) VALUES (%s,%s,%s,%s,%s,%s)",(nombre, apellidopat, apellidomat, password, correo, 0))

        id_usuario = cursor.lastrowid

        #Insertar Pelicula
        nombre_pelicula = random.choice(nombres_peliculas)
        genero_pelicula = random.choice(generos)
        duracion = random.randint(40, 240)
        inventario = random.randint(1,15)

        cursor.execute("INSERT INTO `peliculas` (`nombre`,`genero`,`duracion`,`inventario`) VALUES (%s,%s,%s,%s)",(nombre_pelicula, genero_pelicula, duracion, inventario))

        id_pelicula  = cursor.lastrowid

        #Insertar Renta
        fecha_renta = datetime.date(random.randint(2022,2024), random.randint(1,12), random.randint(1,28))

        cursor.execute("INSERT INTO `rentar` (`idUsuario`,`idPelicula`,`fecha_renta`,`dias_de_renta`,`estatus`) VALUES (%s,%s,%s,%s,%s)",(id_usuario, id_pelicula, fecha_renta, random.randint(30,365), random.randint(0,1)))
    connection.commit()

# 2 Filtra de la tabla Usuarios a aquellos cuyo alguno de sus apellidos termine con cierta cadena    
def filtra(connection, cadena):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `usuarios` WHERE `apPat` LIKE %s OR `apMat` LIKE %s",(f"%{cadena}",f"%{cadena}"))
        resultados = cursor.fetchall()
        for usuario in resultados:
            print(usuario)

# 3 Cambia el genero de una pelicula por uno a eleccion del usuario            
def cambia_genero(connection, pelicula, genero):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE `peliculas` SET `genero` = %s WHERE `nombre` = %s", (genero, pelicula))
    connection.commit()

# 4  Elmina todas las rentas anteriores a la fecha actual
def elimina_rentas(connection):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM `rentar` WHERE `rentar` < %s", (datetime.date.today()-datetime.timedelta(days=3)))
    connection.commit()

if __name__ == "__main__":


    for numero in [1,2,3,4,5,6,7,8,9,10]:
        inserta(connection)

    cadena_apellido = input("Inserta la terminacion de un apellido para ver a sus usuarios correspondientes")
    filtra(connection,cadena_apellido)

    nombre = input("Entra el nombre de la pelicula a cambiar")
    nuevo_genero = input("Nuevo genero que tendra la pelicula")
    cambia_genero(connection, nombre, nuevo_genero)
