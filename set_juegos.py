
# ESTA ES LA VERSIÓN SIN PySimpleGUI

#Importo de cada juego solo la función jugar, que es la que necesito para ejecutar los juegos
from ahorcado import jugar_ahorcado
from reverse import jugar_reverse
from tateti import jugar_tateti

import json

#Diccionario jugador para juardar los datos: nombre y juegos que jugo
# juegos es un arreglo que guarda cada juego que juega
# cada partida se guarda como una tupla que contiene el nombre del juego y el resultado de la partida
jugador = { "nombre": input("Agrege su nombre:  "),
            "juegos": []
            }
# el jugador puede jugar varias veces
jugar = True
archivo = open("datos_jugadores.txt","a+")

#Jugador pone su nombre y elige un juego
def inicio():
    juego = input("Elija un juego \n 1: ahorcado\n 2: reverse\n 3: tateti\n ")
    if juego == "1":
        print("\n AHORCADO \n")
        partida = ("ahorcado",jugar_ahorcado())
        jugador["juegos"].append(partida)
    elif juego == "2":
        print("\n REVERSE \n")
        partida = ("reverse", jugar_reverse())
        jugador["juegos"].append(partida)
    elif juego == "3":
        print("\n TATETI \n")
        partida = ("tateti", jugar_tateti())
        jugador["juegos"].append(partida)
    else:
        print("Número no es válido, elija otra vez")
        inicio()


while jugar:
    inicio()
    again = input(" \n ¿Quiere jugar otra vez? (si o no) ")
    if again == "no":
        jugar = False
        print(" \n Gracias por jugar! \n Estos son sus datos: ")
        print(jugador)
        json.dump(jugador,archivo)
        archivo.close()