import pattern
from pattern.es import parse

#lista de las letras que va ubicando en el tablero, en orden
#letras_pal = []
#letra = ""

#esta parte (while) solo esta porque todavía no sé como controlar como ingresan las letras!
#while letra != ".":
	#letra = input("Letra: ")
	#letras_pal.append(letra) 

#cuando la palabra ya ingresó y el jugador clickea porque terminó de poner la palabra
#el join junta las letras en orden y forma un string con la palabra
#palabra=""
#palabra = palabra.join(letras_pal)
#control
#print("La palabra es: ", palabra)

def analizarPalabra(palabra): 
	#pattern analiza la palabra (devuelve lista de lista de lista)
	pal = parse(palabra).split()
	#control
	#print('ESTO TENGOOOOOOOOO ' ,pal)
	if pal[0][0][1] == 'VB' or pal[0][0][1] == 'NN' or pal[0][0][1] == 'NNS' or pal[0][0][1] == 'JJ':
		#si la palabra es sustantivo, verbo o adjetivo entra al if
		print("La palabra ", pal[0][0][0], " es válida")
	else:
		print("La palabra no es válida")

