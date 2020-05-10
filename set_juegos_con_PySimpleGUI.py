import PySimpleGUI as sg
sg.theme(' Dark Blue 2')

#Importo de cada juego solo la función jugar, que es la que necesito para ejecutar los juegos
from ahorcado import jugar_ahorcado
from reverse import jugar_reverse
from tateti import jugar_tateti

import json
#se guarda en un archivo txt los datos de los jugadores, por lo que usamos json
archivo = open("datos_jugadores.txt","a+")

#Diccionario jugador para juardar los datos: nombre y juegos que jugo
# juegos es un arreglo que guarda cada juego que juega
# cada partida se guarda como una tupla que contiene el nombre del juego y el resultado de la partida
jugador = { "nombre": " ",
            "juegos": []
            }

#un jugador puede jugar varias veces
continuar = True

def menu():
    col1 = [[sg.Text("Tu nombre: ")],
            [sg.Text("Elija un juego:      ")]]
    col2 = [[sg.InputText(size = (30,1))],
            [sg.Listbox(values=('Ahorcado', 'Reverse', 'Tateti'), size=(30, 3), no_scrollbar=True)]]
    layout = [[sg.Text("¡Bienvenido al Set de Juegos!")],
              [sg.Column(col1),sg.Column(col2)],
              [sg.Button("Jugar"),sg.Button("No quiero seguir jugando")]
            ]
    window = sg.Window('Set de Juegos', layout)
    events, datos = window.read()
    window.close()
    if events == "Jugar":
        return datos, events
    else:
        global continuar
        continuar = False
        return 0, events

def seguir_jugando():
    #Popup que pregunta si se quiere seguir jugando
    layout = [[sg.Text("¿Seguir Jugando?")],
              [sg.Button("si"),sg.Button("no")]]
    window = sg.Window('Set de Juegos', layout)
    events, datos = window.read()
    window.close()
    if events == "si": return True
    else: return False

def juego(cual):
    jugador["nombre"] = cual[0]
    juego_elegido = cual[1][0]
    if juego_elegido == "Ahorcado":
        print("\n AHORCADO \n")
        partida = ("ahorcado", jugar_ahorcado())
        jugador["juegos"].append(partida)
    elif juego_elegido == "Reverse":
        print("\n REVERSE \n")
        partida = ("reverse", jugar_reverse())
        jugador["juegos"].append(partida)
    elif juego_elegido == "Tateti":
        print("\n TATETI \n")
        partida = ("tateti", jugar_tateti())
        jugador["juegos"].append(partida)

# J U E G O
while continuar:
    datos, va = menu()
    if(va == "Jugar"):
        juego(datos)
    if continuar == True:
        continuar = seguir_jugando()

print(" \n Gracias por jugar! \n ")
print("Estos son tus datos:")
print(jugador)
json.dump(jugador,archivo)
archivo.close()