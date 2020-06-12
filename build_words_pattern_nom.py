import pattern
from pattern.es import parse

# lista_atril es una lista con el atril de la computadora
lista_atril = ["u", "j", "a", "g", "r", "i", "a"]


#def build_words(lista_atril):
#    atril = list_to_dict(lista_atril)


def list_to_dict(lista_atril):
    hand_as_dict = {}
    for letra in lista_atril:
        hand_as_dict[letra] = hand_as_dict.get(letra, 0) + 1
    return hand_as_dict


def analizarPalabra(palabra):
    # pattern analiza la palabra (devuelve lista de lista de lista)
    pal = parse(palabra).split()
    if pal[0][0][1] == 'VB' or pal[0][0][1] == 'JJ':
        # si la palabra es verbo o adjetivo entra al if
        devuelve =  1
    else:
        #La palabra no es válida
        devuelve = 0
    return devuelve


def build_words(lista_atril):
    atril = list_to_dict(lista_atril)
    todas_las_palabras = [""]
    i = 0
    ew = ""
    while len(ew) < len(lista_atril):
        ew = todas_las_palabras[i]
        tempEW = []
        for w in range(len(ew)):
            tempEW.append(ew[w])
        temp_hand_dict = dict(atril)
        j = 0
        while j < len(lista_atril):
            if lista_atril[j] not in tempEW:
                nueva_palabra = ew + (lista_atril[j])
                todas_las_palabras.append(nueva_palabra)
                j += temp_hand_dict[lista_atril[j]]
            else:
                tempEW.remove(lista_atril[j])
                num = temp_hand_dict[lista_atril[j]] - 1
                temp_hand_dict[lista_atril[j]] = num
                j += 1
        i += 1
    return todas_las_palabras

def reviso_con_pattern(todas_las_palabras):
    #control
    #print(todas_las_palabras)
    #print(len(todas_las_palabras))
    #si no encuentra palabra va a devolver nada
    nada = "no encontró"
    # checkea con pattern
    a = 0
    #b es para control
    #b=1
    pos = len(todas_las_palabras)-1
    while a == 0 and pos>0:
        palabra_al_azar = todas_las_palabras[pos]
        a = analizarPalabra(palabra_al_azar)
        pos = pos-1
        #control
        #print(b)
        #b= b+1
    if pos!=0 :
        return palabra_al_azar
    else:
        return nada

#print(lista_atril)

# imprime una palabra válida o, si no encuentra ninguna, "no encontro"
print(reviso_con_pattern(build_words(lista_atril)))
