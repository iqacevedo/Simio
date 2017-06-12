from random import uniform, sample
from numpy import log

def generar_exponencial(lmda):
    #Se generan 5 instancias de una exponencial(1/10) con el método la transformada inversa
    exponenciales = []
    for j in range(5):
        u = uniform(0, 1)
        x = -(1/lmda) * log(1 - u)
        exponenciales += [x]
    return exponenciales

seleccion = list(map(lambda x: round(x, 2), sample(generar_exponencial(1/10), 5)))
print(seleccion)
