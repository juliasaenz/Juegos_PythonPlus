import random
#Preparo el juego
#Defino conjunto de palabras a trabajar por temas
palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
#Defino estructura del ahoracado
ahorcado = [' O ', '/|\\','/ \\']

#FUNCIÓN PALABRA: Devuelve una palabra
def palabra():
	tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
	#Selecciono la palabra a trabajar
	pal_ = palabras[tema][random.randrange(len(palabras[tema]))]
	#armo la estructura de la palabra
	return pal_

#FUNCIÓN SEPARAR: Devuluve lista con huecos
def separar(palabra):
	pal_separada_ = []
	for y in palabra:
		pal_separada_.append(['_ '])
	return pal_separada_

#FUNCIÓN JUEGO
def juego():
	#eligo palabra
	pal = palabra()
	#hago agujeros
	pal_separada = separar(pal)
	#incio variables
	cantidad_letras_adivinadas = 0
	cantidad_partes_cuerpo = 0
	#Muestro agujeros
	print ('- '*len(pal))
	#interacción
	sigue = True
	while sigue:
		#usuario elige letra
		letra = input('Ingresa una letra: ').lower()
		# Si hay al menos una aparición de la letra..
		if letra in pal:
			#Guardo las posiciones donde se encuentra
			for pos in range(len (pal)):
				if pal[pos] == letra:
					pal_separada[pos] = letra
					cantidad_letras_adivinadas = cantidad_letras_adivinadas + 1
		#armo la palabra a mostrar al jugador con su letra elegida
			pal_imprime = ''
			for y in pal_separada:
				pal_imprime = pal_imprime + y[0]
			print (pal_imprime)
			#averiguo si terminó o debe continuar
			if cantidad_letras_adivinadas == len(pal):
				print ('Ganaste')
				return 'Ganó'
				sigue = False
		else:
			#si se equivocó completo el cuerpo
			cantidad_partes_cuerpo=cantidad_partes_cuerpo + 1
			for x in range(cantidad_partes_cuerpo):
				print (ahorcado[x])
			if cantidad_partes_cuerpo == 3:
				print ('Perdiste!. La palabra era:', pal)
				return 'Perdió'
				sigue = False

def jugar_ahorcado():
	return juego()