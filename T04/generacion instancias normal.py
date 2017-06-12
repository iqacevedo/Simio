from random import uniform, sample
from numpy import sqrt, log, cos, sin, pi, exp, linspace

def generar_normal(mu, sigma):
    #Se generan 50 instancias de una Normal(0,1) con el método de seno y coseno visto en clases
    normales01 = []
    for j in range(5):
        u1 = uniform(0, 1)
        u2 = uniform(0, 1)
        x1 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
        x2 = sqrt(-2 * log(u1)) * sin(2 * pi * u2)
        normales01 += [x1, x2]

    #Se generan las instancias de una Normal(mu, sigma) usando el proceso inverso a la estandarización
    normalesMuSigma = []
    for z in normales01:
        n = mu + z * sigma
        normalesMuSigma.append(round(n, 6))

    return normalesMuSigma

seleccion = list(map(lambda x: round(x,2),sample(generar_normal(10,2), 5)))
print(seleccion)
