#from pattern.es import lexicon, spelling, tag

#palabra = input('ingresa una palabra\n ')

#def clasificar(palabra):
	#print(tag(palabra, tokenize=True, encoding='utf-8', tagset = 'UNIVERSAL'))
	#print(tag(palabra, tokenize=True, encoding='utf-8'))


#palabra = 'árbol'

#if not palabra in spelling:
	#if not palabra in lexicon:
		#print('No se encuentra en pattern.es')
	#else:
		#print('La encontró en lexicon')
		#clasificar(palabra)
#else:
	#print('La encontró en spelling')
	#clasificar(palabra)

##################################################################
##################################################################



from pattern.es import verbs, tag, spelling, lexicon
import string

#palabra = input('ingresa una palabra\n ')

def clasificar(palabra):
	print( tag(palabra, tokenize=True, encoding='utf-8',tagset = 'UNIVERSAL'))
	print( tag(palabra, tokenize=True, encoding='utf-8'))
	print()


#palabra = 'Camino'
#print(palabra)
def analizarPalabra (palabra,esValida):
	if not palabra.lower() in verbs:
		#palabraAnalizada = False
		if not palabra.lower() in spelling:
			#palabraAnalizada = False
			if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
				print('No se encuentra en pattern.es')
				esValida = False
				print(esValida)
			else:
				print('La encontró en lexicon')
				esValida = True
				print(esValida)
				#clasificar(palabra)
		else:
			print('La encontró en spelling')
			esValida = True
			print(esValida)
			#clasificar(palabra)
	else:
		print('La encontró en verbs')
		esValida = True
		print(esValida)
		#clasificar(palabra)
	print()
	return esValida
