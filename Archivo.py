import os
import os .path as path

# Clase para manejar archivos
class ARCH:

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Lee archivos (para este caso, solo la segunda linea "[2]" para leer las claves y el mensaje)
    def leerArchivo(self):

        archivo = open(self.nombre, 'r')

        contenido = archivo.readlines()[2]

        archivo.close()

        return contenido

    # Escribe en el archivo (sobreescribe todo lo que se encuentra en el)
    def escribirArchivo(self, escritura):
        archivo = open(self.nombre, 'w')

        archivo.write(escritura)
        archivo.write(" ")
        archivo.close()

    # Escribe en el archivo sin modificar lo que contiene ya escrito
    def añadirArchivo(self, escritura, tipo):
        # Si ya existe un archivo, se borra. Así genera solo un archivo cada vez que se requiera
        if path.exists(self.nombre):
            self.eliminarArchivo()

        archivo = open(self.nombre, 'a')
        # Escritura
        archivo.write('-----INICIO RSA ' + tipo +'-----')
        archivo.write('\n')
        archivo.write('\n'+escritura)
        archivo.write(" ")
        archivo.write('\n')
        archivo.write('\n'+'-----FINAL RSA ' + tipo + '-----')
        archivo.close()

    # Convierte el contenido del archivo (str por defecto) a enteros y lo devuelve en una lista
    def convertirArchivo(self, convertir):
        salida = []
        n = 0

        for m in range(0, len(convertir)):
            if convertir[m] == ' ':
                sal = int(convertir[n:m])
                salida.append(sal)
                n = m + 1

        return salida

    # Elimina el archivo por nobmre y ubicacion
    def eliminarArchivo(self):
        os.remove(os.getcwd() + "/" + self.nombre)

        print("\nEliminado archivo desde la ruta: \n\n\t{0}/{1}".format(os.getcwd(), self.nombre))

