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

turnos = 12

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

        # this print the correct palabra
        print("la palabra es: ", palabra)
        break

    intento = input("dame letra:")

    intentos += intento

    if intento not in palabra:

        turnos -= 1

        print("error")

        print("aun te quedan", + turnos, 'intentos')


        if turnos == 0:
            print("fin de la partida, has perdido")