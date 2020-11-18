# Diccionario para la conversion de caracteres
dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, ' ': 10, 'A': 11, 'B': 12,
       'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24,
       'Ñ': 25, 'O': 26, 'P': 27, 'Q': 28, 'R':29, 'S': 30, 'T': 31, 'U': 32, 'V': 33, 'W': 34, 'X': 35, 'Y': 36,
       'Z': 37, 'a': 38, 'b': 39, 'c': 40, 'd': 41, 'e': 42, 'f': 43, 'g': 44, 'h': 45, 'i': 46, 'j': 47, 'k': 48,
       'l': 49, 'm': 50, 'n': 51, 'ñ': 52, 'o': 53, 'p': 54, 'q': 55, 'r': 56, 's': 57, 't': 58, 'u': 59, 'v': 60,
       'w': 61, 'x': 62, 'y': 63, 'z': 64}


lista_numeros = []
lista_cadena = []

# Convierte un mensaje a una lista de enteros
def convInt(mensaje):
    for letra in mensaje:
        lista_numeros.append(dic.get(letra))

    return lista_numeros


# Convierte la lista de enteros a una cadena
def convStr(numeros):
    for i in numeros:
        lista_cadena.append(list(dic.keys())[list(dic.values()).index(i)])

    cadena = "".join(lista_cadena)
    return cadena
