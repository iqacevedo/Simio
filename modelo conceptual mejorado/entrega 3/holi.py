import numpy.random as n
import matplotlib.pyplot as plt
import math
from random import normalvariate, triangular, randint, uniform
inventario_b = 60000
inventario_k = 60000
inventario_p = 55000

for i in range(60):
    dema_b = normalvariate(4000, 100)
    dema_k = normalvariate(4000, 200)
    dema_p = triangular(4500, 5000, 5500)
    inventario_b -= dema_b
    inventario_k -= dema_k
    inventario_p -= dema_p
    inventario_b += (28.43 * 4 * 30)
    inventario_k += (29.4 * 4 * 30)
    inventario_p += (36.9 * 4.1* 30)
for i in range(25):
    dema_b = normalvariate(4000, 100)
    dema_k = normalvariate(4000, 200)
    dema_p = triangular(4500, 5000, 5500)
    inventario_b -= dema_b
    inventario_k -= dema_k
    inventario_p -= dema_p
    inventario_b += (28.43 * 5 * 30)
    inventario_k += (29.4 * 5 * 30)
    inventario_p += (36.9 * 5* 30)
print(inventario_b, inventario_k, inventario_p)
for i in range(5):

    dema_b = normalvariate(4000, 100)
    dema_k = normalvariate(4000, 200)
    dema_p = triangular(4500, 5000, 5500)
    inventario_b -= dema_b
    inventario_k -= dema_k
    inventario_p -= dema_p
    inventario_b += (28.43 * uniform(5, 7) * 30)
    inventario_k += (29.4 * uniform(5, 7) * 30)
    inventario_p += (36.9 * uniform(5, 7) * 30)
print(inventario_b, inventario_k, inventario_p)
for i in range(210):
    dema_b = normalvariate(4000, 100)
    dema_k = normalvariate(4000, 200)
    dema_p = triangular(4500, 5000, 5500)
    inventario_b -= dema_b
    inventario_k -= dema_k
    inventario_p -= dema_p
    inventario_b += (28.43 * 4.6 * 30)
    inventario_k += (29.4 * 4.4 * 30)
    inventario_p += (36.9 * 4.38 * 30)
print(inventario_b, inventario_k, inventario_p)
