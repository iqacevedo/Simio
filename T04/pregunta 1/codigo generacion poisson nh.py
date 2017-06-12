from random import expovariate, random

max_lambda = 6
llegadas = []

for i in range(5):
    #Creamos los instantes de llegada según Poisson Hom. con la máxima tasa
    replica = []
    t = 0
    while t < 2:
        t += expovariate(max_lambda)
        replica.append(t)
        if t >= 2: break

    #Luego descartamos según la probabilidad
    for t in replica:
        prob = 1 - (3 * t / max_lambda)
        if random() < prob:
            replica.remove(t)

    #Finalmente guardamos la rélica        
    llegadas.append(replica)
        
        

