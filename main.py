import random
import colorama

from colorama import Fore, Back, Style
colorama.init()


print("bienvenido al juego del ahorcado")

print("buena suerte ",)

palabras = ['arcoiris', 'computadora', 'ciencia', 'programar',
         'python', 'matematicas', 'jugador', 'condicion',
         'reverso', 'agua', 'tablero', 'genios']

palabra = random.choice(palabras)

print("dame letra")

intentos = ''

turnos = 6

print (Fore.RED)
while turnos > 0:

    fallo = 0

    for caracter in palabra:

        if caracter in intentos:
            print(caracter)

        else:

            print("_")

            fallo += 1


    if fallo == 0:

        print("ganastes")

        print("la palabra es: ", palabra)
        break

    intento = input("dame letra:")

    intentos += intento

    if intento not in palabra:




        turnos -= 1

        print("error. intenta otra letra")


        print("aun te quedan", + turnos, 'intentos')

        if turnos == 5:
            print("""
          +---+
          |   |
          O   |
              |
              |
              |
        =========""")

        if turnos == 4:
            print("""
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========""")

        if turnos == 3:
            print("""
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========""")
        if turnos == 2:
            print("""
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========""")
        if turnos == 1:
            print("""
                    +---+
                    |   |
                    O   |
                   /|\  |
                   /    |
                        |
                  =========""")




        if turnos == 0:
            print("""
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========""")
            print("fin de la partida, has perdido")
            exit()