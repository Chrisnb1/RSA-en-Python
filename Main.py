from Diccionario import convInt, convStr
from Algoritmo import RSA
from Archivo import ARCH

# Menu
def menu():
    # solicita una accion
    while True:
        print('(1) RSA por consola.')
        print('(2) RSA por archivos.')
        print('(3) Salir.')

        accion = input('Elija una accion a realizar: ')

        if accion == '1':
            consolaRSA()
            break
        elif accion == '2':
            archivosRSA()
            break
        elif accion == '3':
            exit(0)
        else:
            print('Entrada no válida. Intentelo nuevamente.')
            break

# ejecuta el algoritmo solo por consola
def consolaRSA():

    # solicita un mensaje
    mensaje = input("Introduzca un mensaje a encriptar: ")
    # convierte el mensaje a una lista de enteros
    mensaje = convInt(mensaje)
    # instancia el objeto del algoritmo
    obj = RSA(mensaje)
    # generacion de claves
    clavePublica = obj.genClavePublica()
    clavePrivada = obj.genClavePrivada()
    # encriptar y descencriptar utilizando las claves
    encrip = obj.encriptar(clavePublica[0], clavePublica[1])
    desencrip = obj.desencriptar(encrip, clavePrivada[0], clavePrivada[1])
    # Convierte a str para su lectura
    msjCifrado = " ".join(map(str, encrip))
    msjDescifrado = " ".join(map(str, desencrip))
    # muestra las variables del algortimo
    obj.verInfo()
    # impresion por consola
    print("Clave Publica: ", clavePublica)
    print("Clave Privada: ", clavePrivada)

    print("MSJ CIFRADO: ", msjCifrado)
    print("MSJ DESCIFRADO: ", msjDescifrado)

    print("MSJ ORIGINAL: ", convStr(desencrip))

# ejecuta el algoritmo atraves de archivos
def archivosRSA():
    # solicita una accion
    while True:
        print('(1) Crear Claves y Cifrar Mensaje.')
        print('(2) Descifrar Mensaje.')
        print('(3) Salir.')

        accion = input('Elija una accion a realizar: ')

        if accion == '1':
            cifrar()
            break
        elif accion == '2':
            descifrar()
            break
        elif accion == '3':
            exit(0)
        else:
            print('Entrada no válida. Intentelo nuevamente.')
            break

# crea las claves y el mensaje cifrado en diferentes archivos
def cifrar():
    # solicita un mensaje
    mensaje = input("Introduzca un mensaje a encriptar: ")
    # convierte el mensaje a una lista de enteros
    mensaje = convInt(mensaje)

    # instancia el objeto del algoritmo
    obj = RSA(mensaje)
    # generacion de claves
    clavePublica = obj.genClavePublica()
    clavePrivada = obj.genClavePrivada()
    # cifra el mensaje
    encrip = obj.encriptar(clavePublica[0], clavePublica[1])

    '''Claves'''
    # guarda la clave publica en un arch txt
    clavePublica = " ".join(map(str, clavePublica))
    arcPublic = ARCH('Clave Publica.txt')
    arcPublic.añadirArchivo(str(clavePublica), 'CLAVE PUBLICA')

    # guarda la clave privada en un arch txt
    clavePrivada = " ".join(map(str, clavePrivada))
    arcPriv = ARCH('Clave Privada.txt')
    arcPriv.añadirArchivo(str(clavePrivada), 'CLAVE PRIVADA')

    '''Encriptar'''
    # guarda el mensaje cifrado en un arch txt
    msjCifrado = " ".join(map(str, encrip))
    arcMsj = ARCH('Mensaje Cifrado.txt')
    arcMsj.añadirArchivo(str(msjCifrado), 'MENSAJE CIFRADO')

    print('\nSe han creado los archivos correctamente.')

# descifra el mensaje
def descifrar():
    # solicita el mensaje y la clave privada
    arcMsj = ARCH('Mensaje Cifrado.txt')
    arcPriv = ARCH('Clave Privada.txt')

    #  procede al descifrado
    if arcMsj and arcPriv:
        # instancia de un objeto del algoritmo
        obj = RSA(0)
        # lee los archivos
        msjC = arcMsj.leerArchivo()
        msjCP = arcPriv.leerArchivo()
        # realiza la conversion
        salida = arcMsj.convertirArchivo(msjC)
        salidaP = arcPriv.convertirArchivo(msjCP)
        # descifra el mensaje
        desencrip = obj.desencriptar(salida, salidaP[0], salidaP[1])
        # lo muestra por pantalla
        print("\nMSJ ORIGINAL: ", convStr(desencrip))

    else:
        print('Los archivos no estan creados.')

# ejecuta el programa
menu()