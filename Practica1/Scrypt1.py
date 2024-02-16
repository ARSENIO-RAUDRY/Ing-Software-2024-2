class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0
        self.juegos = 0
        self.sets = 0
        self.saque = False
        self.ventaja = False

    def mostrar_nombre(self):
        return self.nombre

    def mostrar_puntaje(self):
        return self.puntaje

    def mostrar_juegos(self):
        return str(self.juegos)

    def mostrar_sets(self):
        return str(self.sets)

    def reiniciar_puntaje(self):
        self.puntaje=0
        return

    def sumar_puntaje(self):
        if self.puntaje == 0:
            self.puntaje = 15
            return

        if self.puntaje == 15:
            self.puntaje = 30
            return

        if self.puntaje == 30:
            self.puntaje = 40
            return

    
def anotar(nombre, jugador1,jugador2):
    if nombre == jugador1.nombre:
        return jugador1, jugador2
    if nombre == jugador2.nombre:
        return jugador2,jugador1
    
if __name__ == '__main__':
    nombre1 = input("Ingrese el nombre del Primer jugador")
    nombre2 = input("Ingrese el nombre del Segundo Jugador")

    jugador1 = Jugador(nombre1)
    jugador2 = Jugador(nombre2)
    ganador = None

    sets = int (input("Ingrese el numero de sets"))
    while(True):
        print("Sets:" + jugador1.mostrar_nombre() + jugador2.mostrar_sets()+jugador2.mostrar_nombre()+jugador2.mostrar_sets())
        print("Juegos:" + jugador1.mostrar_nombre() + jugador2.mostrar_juegos()+jugador2.mostrar_nombre()+jugador2.mostrar_juegos())
        print("Comienza el juego")
        ganador_juego = None

        """Se juegan las rondas entre ambos jugadores"""
        while(ganador_juego == None):

            anotador_nombre = input("Ingrese el nombre de quien anoto el punto")
            anotador, noanotador = anotar(anotador_nombre,jugador1,jugador2)

            if anotador.ventaja == True or (anotador.puntaje==40 and noanotador.puntaje<40):
                ganador_juego = anotador
                jugador1.reiniciar_puntaje()
                jugador2.reiniciar_puntaje()

            elif (anotador.puntaje == 40 and noanotador.puntaje ==40) or noanotador.ventaja == True:
                anotador.ventaja = True
                noanotador.ventaja = False

                print(anotador.mostrar_nombre() + "Adv. - " + str(noanotador.mostrar_puntaje()) + noanotador.mostrar_nombre())

            else:
                anotador.sumar_puntaje()
                print(anotador.mostrar_nombre() + str(anotador.mostrar_puntaje()) + "-" + str(noanotador.mostrar_puntaje()) + noanotador.mostrar_nombre())

        ganador_juego.juegos +=1

        if jugador1.juegos > jugador2.juegos:
            if jugador1.juegos >= 6 and abs(jugador2.juegos - jugador1.juegos) >=2:
                jugador1.sets += 1
        if jugador2.juegos > jugador1.juegos:
            if jugador2.juegos >= 6 and abs(jugador2.juegos - jugador1.juegos) >=2:
                jugador2.sets += 1

        if jugador1.sets> int(sets/2):
            ganador=jugador1
            break
        if jugador2.sets> int(sets/2):
            ganador=jugador2
            break
    print("El ganador es: "+ ganador.mostrar_nombre())
   
