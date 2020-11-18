from Math import *

# Clase del algortimo
class RSA:
    # Constructor
    def __init__(self, msg, e = 65537, p = genPrimo(), q = genPrimo()):

        self.e = e
        self.p = p
        self.q = q
        self.msg = msg

        # Verifica que (e,p) y (e,q) sean coprimos y que q sea distinto de p
        while not coprimo(e,p) and not coprimo(e,q) and q != p:
            self.p = genPrimo()
            self.q = genPrimo()

        # Calculos para generar las claves
        self.n = p * q
        self.phi = (q-1)*(p-1)
        self.d = mod_inverso(self.e, self.phi)

    # Genera la clave publica (n,e)
    def genClavePublica(self):
        publica = (self.n, self.e)
        return publica

    # Genera la clave privada (n, d)
    def genClavePrivada(self):
        privada = (self.n, self.d)
        return privada

    # Cifra un mensaje con la clave publica
    def encriptar(self, n, e):
        if type(self.msg) == list: # Para un conjunto de enteros
            listaAux = []
            for i in self.msg:
                resul = (pow(i, e) % n)
                listaAux.append(resul)

            return listaAux
        else: # Para un solo entero
            return pow(self.msg, e) % n

    # Descifra un mensaje con la clave privada
    def desencriptar(self, msg, n, d):
        if type(msg) == list: # Para un conjunto de enteros
            listaAux = []
            for i in msg:
                listaAux.append(pow(i, d) % n)

            return listaAux
        else: # Para un solo entero
            return pow(msg, d) % n

    # Muestra la informacion de las variables del algoritmo
    def verInfo(self):
        print("Q = ", self.q)
        print("P = ", self.p)
        print("N = ", self.n)
        print("PHI = ", self.phi)
        print("E = ", self.e)
        print("D = ", self.d)




