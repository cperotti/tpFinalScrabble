import PySimpleGUI as sg
import json
import lexicon_pattern as ppattern
import random
import pickle
#import build_words_pattern_nom as juegaCompu
  
def muestroL(window,atril): 
    for indice in range(len(atril)):
        letra = atril[indice] 
        window.FindElement("Letra" + str(indice)).Update(letra)

def muestroLC(window,atril): 
    for indice in range(len(atril)):
        letra = atril[indice] 
        window.FindElement("LetraC" + str(indice)).Update("*")
   
def accionAtril (window,atrilJ,pos,textBoton):
	letraElegida = atrilJ[pos]  
	window.FindElement(textBoton).Update("")
	atrilJ[pos] = 0
	return letraElegida
	
def accionTablero(window,event,listaCoordenadas,letraElegida,matriz):
	posicionCasilleroTablero = event  #me da que boton del tablero toque
	listaCoordenadas.append(posicionCasilleroTablero)
	
	x=posicionCasilleroTablero[0]
	y=posicionCasilleroTablero[1]
	
	window[posicionCasilleroTablero].update(letraElegida)
	matriz[x][y] = letraElegida
	return listaCoordenadas
	
def armarPalabra(listaCoordenadas,matriz):
	unionLetras = []
	listaCoordenadas.sort()
	for lcoord in listaCoordenadas:
		x= lcoord[0]
		y= lcoord[1]
		unionLetras.append(matriz[x][y])
	     
	return ''.join(unionLetras)
	
def rellenarAtril(window,atrilJ,letras):
	for indice in range(len(atrilJ)):
		if atrilJ[indice] == 0:
			letra=random.choice(letras)
			atrilJ[indice] = letra
			window.FindElement("Letra" + str(indice)).Update(letra)
			letras.remove(letra)
		#print(atrilJ)
	return atrilJ
	
def devolverLetrasAtril(window,listaCoordenadas,matriz,atrilJ):
	guardoLetrasTemporal = []
	for lcoord in listaCoordenadas:
		x=lcoord[0]
		y=lcoord[1]
		
		letra = matriz[x][y]
		guardoLetrasTemporal.append(letra)
		window.FindElement(lcoord).Update("")
	for indice in range(len(atrilJ)):
		if atrilJ[indice]== 0:
			valor = random.choice(guardoLetrasTemporal)
			atrilJ[indice]= valor
			guardoLetrasTemporal.remove(valor)
			window.FindElement("Letra" + str(indice)).Update(valor)
	listaCoordenadas = []
	unionLetras = []
	print(listaCoordenadas)
	return atrilJ	

def main(args):  
	jugada=args
	puntos=jugada.get_puntos()
	letras = jugada.get_letras()
  
	sg.theme("GreenTan")

	max_col = max_rows = 15
  
	letrasEnTablero = [] 
	columna_1 = [
		[sg.Text("Jugador")],[sg.Input(size=(15,1),key="nombre")],
		[sg.Button("Comenzar", key="comenzar"), sg.Button("Posponer",key="posponer"),sg.Button("Reanudar",key="reanudar")],
		[sg.Button("Comprobar", key="comprobar")],
		[sg.Button("Finalizar", button_color=("white","red"),key="finalizo")],
		[sg.Text("Puntos Jugador")],[sg.Input(size=(15,1),key="puntosJug")],
		[sg.Text("Puntos Compu")],[sg.Input(size=(15,1),key="puntosPc")],
		[sg.Text("Tiempo",justification="center")], [sg.Text(size=(5, 2), font=('Helvetica', 20), justification='center', key='tiempo')],
		[sg.Text("Computadora")],
		[sg.Text(" ", size=(1,1)),sg.Button("", size=(2,1), key="LetraC0"), sg.Button("", size=(2,1), key="LetraC1"), sg.Button("", size=(2,1), key="LetraC2"), sg.Button("", size=(2,1), key="LetraC3"), sg.Button("", size=(2,1), key="LetraC4"), sg.Button("", size=(2,1), key="LetraC5"), sg.Button("", size=(2,1), key="LetraC6")],
		[sg.Text(" ", size=(1,1))],
		[sg.Text("Jugador")],
		[sg.Text(" ", size=(1,1)),sg.Button("", size=(2,1), key="Letra0"), sg.Button("", size=(2,1), key="Letra1"), sg.Button("", size=(2,1), key="Letra2"), sg.Button("", size=(2,1), key="Letra3"), sg.Button("", size=(2,1), key="Letra4"), sg.Button("", size=(2,1), key="Letra5"), sg.Button("", size=(2,1), key="Letra6")],
		[sg.Text(" ", size=(4, 1)), sg.Button("Cambio letras", size=(12,2),key="cambio")]
		]
 
	columna_tablero = [[sg.Button("", size=(2, 1), key=(i,j), pad=(0,0), button_color=("white", "tan")) for j in range(max_col)] for i in range(max_rows)]

	layout = [
		[sg.Column(columna_tablero), sg.Column(columna_1)],
		[sg.Button('Insertar Palabra',size=(9,2), key="insertar"), sg.Button('Pasar',size=(9,2), key="pasar")]
		]
	
	window = sg.Window("::::::::: SCRABBLE AR :::::::::", layout)
	window.Finalize()

	tiempoCorriendo = False
	contador = 0
	jugadorJ=jugada.get_jugadorJ()
	jugadorC=jugada.get_jugadorC()
	listaCoordenadas = []
	matriz=[]
	esValida = False
	
	#unionLetras = []
	atrilJ = jugadorJ._atril
  
	for i in range (15):
		matriz.append([0]*15)
  
	while True:
		event, values = window.Read(timeout=10)
  
		if event == 'Letra0':
			letraElegida = accionAtril(window,atrilJ,0,event)
  
		if event == 'Letra1':
			letraElegida = accionAtril(window,atrilJ,1,event)
  
		if event == 'Letra2':
			letraElegida = accionAtril(window,atrilJ,2,event)
	  
		if event == 'Letra3':
			letraElegida = accionAtril(window,atrilJ,3,event)
	  
		if event == 'Letra4':
			letraElegida = accionAtril(window,atrilJ,4,event)
	  
		if event == 'Letra5':
			letraElegida = accionAtril(window,atrilJ,5,event)
	  
		if event == 'Letra6':
			letraElegida = accionAtril(window,atrilJ,6,event)
	  
		if type(event) is tuple:
			print('tamaño lista coordenadas ', len(listaCoordenadas))
			if len(listaCoordenadas) == 0:
				listaCoordenadas = accionTablero(window,event,listaCoordenadas,letraElegida,matriz)
			else:
				coordx=listaCoordenadas[0][0]
				coordy=listaCoordenadas[0][1]
				listaCoordenadas = accionTablero(window,event,listaCoordenadas,letraElegida,matriz)
				for i in listaCoordenadas:
					if i[1] == coordy+1:
						print('va por horizontal', listaCoordenadas)
					elif i[0] == coordx+1:
						print('va por vertcal',listaCoordenadas)	
		  
		if event == 'insertar':
			palabra = armarPalabra(listaCoordenadas,matriz)
			print('palabra ',palabra)
			print('voy a analizar la palabra')
			esValida = ppattern.analizarPalabra(palabra, esValida)
			print('volvi de analizar la palabra')
			print('palabra analizada es: ', esValida)
			
			if esValida:
				rellenarAtril(window,atrilJ,letras)
				nuevo_puntaje = jugadorJ.get_puntaje()
				for letra in palabra:
					nuevo_puntaje= nuevo_puntaje+puntos[letra]
					jugadorJ.set_puntaje(nuevo_puntaje)
				window["puntosJug"].update(nuevo_puntaje)
				listaCoordenadas = []
				print(listaCoordenadas)
			else:
				devolverLetrasAtril(window,listaCoordenadas,matriz,atrilJ)
											
		if event == "finalizo":
			tiempoCorriendo = False
			break
	  
		if event == "comenzar":
			window["nombre"].update(jugadorJ.get_nombre())
			window["puntosJug"].update(jugadorJ.get_puntaje())
		  
			muestroL(window,jugadorJ.get_atril())
			muestroLC(window,jugadorC.get_atril())
			jugadorJ.set_turno = True
			tiempoCorriendo = True
	  
		if event == "comprobar":
			ptos=jugadorJ.get_puntaje()
			for j in letrasEnTablero:
				ptos=ptos+puntos.get(j)
				window["puntosJug"].update(ptos)
	  
		if event ==  "posponer":
			tiempoCorriendo = False
			with open('scrabble.pkl', 'wb') as output:
				pickle.dump(jugada, output, pickle.HIGHEST_PROTOCOL)
			
			#registro={} 
			#jugada.set_tiempo(window["tiempo"])
			#datos={"jugada":jugada,"tablero":[[(i,j) for j in range(max_col)] for i in range(max_rows)]}
			#registro.setdefault(window["nombre"],datos)
			#with open("jugadas.json",'a') as file:
			#	json.dump(registro,file)
			#file.close() 

			break 
		if event == "reanudar":
			tiempoCorriendo = True
			with open('scrabble.pkl', 'rb') as input:
				jugada = pickle.load(input)
			jugadorJ=jugada.get_jugadorJ()
			jugadorC=jugada.get_jugadorC()
			window["nombre"].update(jugadorJ.get_nombre())
			window["puntosJug"].update(jugadorJ.get_puntaje())
		  
			muestroL(window,jugadorJ.get_atril())
			muestroLC(window,jugadorC.get_atril())
              
		if tiempoCorriendo: 
			window["tiempo"].update("{:02d}:{:02d}".format((contador // 100) // 60, (contador // 100) % 60))
			contador += 1
	  
		if event == "cambio":
			if jugada.get_cantCambios()<3:
				jugadorJ.cambioL(letras,jugadorJ.get_atril(),window)
				print(jugadorJ.get_atril())
				jugada.sumarCambio()	
	window.close() 	 
 
