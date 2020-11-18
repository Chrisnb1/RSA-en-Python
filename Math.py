from Crypto.Util import number
from math import gcd as bltin_gcd

# Genera un numero primo de longitud nbits
def genPrimo(leng=10):
    return number.getPrime(leng)

# Calcula el inverso multiplicativo modular con el Algoritmo Euclidiano Extendido
def mod_inverso(x,y):

    def eea(a,b):
        if b==0:return (1,0)
        (q,r) = (a//b,a%b)
        (s,t) = eea(b,r)
        return (t, s-(q*t))

    inv = eea(x,y)[0]
    if inv < 1: inv += y
    return inv

# Verifica que dos numeros sean coprimos
def coprimo(a, b):
    return bltin_gcd(a, b) == 1