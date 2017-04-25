import numpy.random as nr
import matplotlib.pyplot as plt
import math
from random import normalvariate, triangular, randint, uniform

def calcular_multas(invB, invK, invP, multasB, multasK, multasP):
    if invB < 20000: multasB += 1
    if invK < 20000: multasK += 1
    if invP < 20000: multasP += 1
    return (multasB, multasK, multasP)

def prom(lista, d=0):
    if d==0:
        return round(sum(lista)/len(lista))
    else:
        return round(sum(lista) / len(lista), d)


def imprimir_inv(mes, invB, invK, invP):
    string = "Fin "+mes+": " + " "*(10-len(mes))
    string += str(round(invB)) + " "  + str(round(invK)) + " " + str(round(invP))
    print(string)

def SIMULAR_AÑO(imprimir):
    inventarios_historicos = [[], [], []]
    inv_B = 60000
    inv_K = 60000
    inv_P = 55000

    multas_B = 0
    multas_K = 0
    multas_P = 0

    if imprimir:
        print("                Bright Koala Paper")
        print("1 de Enero:", round(inv_B), round(inv_K), round(inv_P))

    ###############################################################################################3
    #Enero
    for i in range(30):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        inv_B -= dema_b
        inv_K -= dema_k
        inv_P -= dema_p
        inv_B += (28.43 * 3.3 * 30)
        inv_K += (29.4 * 3.2 * 30)
        inv_P += (36.9 * 3.6 * 30)
        multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[0].append(round(inv_B))
        inventarios_historicos[1].append(round(inv_K))
        inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Enero", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Febrero
    for i in range(30):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        inv_B -= dema_b
        inv_K -= dema_k
        inv_P -= dema_p
        inv_B += (28.43 * 4.65 * 30)
        inv_K += (29.4 * 4.5 * 30)
        inv_P += (36.9 * 4.5 * 30)
        multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[0].append(round(inv_B))
        inventarios_historicos[1].append(round(inv_K))
        inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Febrero", inv_B, inv_K, inv_P)

    ###############################################################################################3
    #Marzo

    #PARA BRIGHT
    for i in range(11):
        dema_b = normalvariate(4000, 100)
        inv_B -= dema_b
        inv_B += (28.43 * 4.7 * 30)
        multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[0].append(round(inv_B))
    for i in range(19):
        dema_b = normalvariate(4000, 100)
        inv_B -= dema_b
        inv_B += (28.43 * 7 * 30) #Maxima Capacidad, que en esta temporada es en promedio 7
        multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[0].append(round(inv_B))

    #PARA KOALA
    for i in range(16):
        dema_k = normalvariate(4000, 200)
        inv_K -= dema_k
        inv_K += (29.4 * 4.5 * 30)
        multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[1].append(round(inv_K))
    for i in range(14):
        dema_k = normalvariate(4000, 200)
        inv_K -= dema_k
        inv_K += (29.4 * 7 * 30)   #Máxima Capacidad, que en esta temporada es en promedio 7
        multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[1].append(round(inv_K))

    #PARA PAPER
    for i in range(18):
        dema_p = triangular(4500, 5000, 5500)
        inv_P -= dema_p
        inv_P += (36.9 * 4.5 * 30)
        multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[2].append(round(inv_P))
    for i in range(12):
        dema_p = triangular(4500, 5000, 5500)
        inv_P -= dema_p
        inv_P += (36.9 * 7 * 30)   #Máxima Capacidad, que en esta temporada es en promedio 7
        multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Marzo", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Abril
    for i in range(30):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        inv_B -= dema_b
        inv_K -= dema_k
        inv_P -= dema_p
        inv_B += (28.43 * 4 * 30) #Máxima Capacidad, que en esta temporada es en promedio 4
        inv_K += (29.4 * 4 * 30)  #Máxima Capacidad
        inv_P += (36.9 * 4 * 30)  #Máxima Capacidad
        multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[0].append(round(inv_B))
        inventarios_historicos[1].append(round(inv_K))
        inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Abril", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Mayo
    for i in range(30):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        inv_B -= dema_b
        inv_K -= dema_k
        inv_P -= dema_p
        inv_B += (28.43 * 4 * 30)  #Máxima Capacidad, que en esta temporada es en promedio 4
        inv_K += (29.4 * 4 * 30)   #Máxima Capacidad
        inv_P += (36.9 * 4 * 30)   #Máxima Capacidad
        multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[0].append(round(inv_B))
        inventarios_historicos[1].append(round(inv_K))
        inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Mayo", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Meses de Junio a Diciembre
    for i in range(210):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        inv_B -= dema_b
        inv_K -= dema_k
        inv_P -= dema_p
        inv_B += (28.43 * 4.7 * 30)
        inv_K += (29.4 * 4.55 * 30)
        inv_P += (36.9 * 4.5 * 30)
        multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
        inventarios_historicos[0].append(round(inv_B))
        inventarios_historicos[1].append(round(inv_K))
        inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Diciembre", inv_B, inv_K, inv_P)

    if imprimir:
        print("\nMultas durante el año")
        print("Bright:", multas_B)
        print("Koala:", multas_K)
        print("Paper:", multas_P, "\n")

    return (round(inv_B), round(inv_K), round(inv_P), multas_B, multas_K, multas_P, inventarios_historicos)


n=1
replicas = [SIMULAR_AÑO(imprimir=0) for i in range(n)]
resultados = list(zip(*replicas))


bright = resultados[0]
koala = resultados[1]
paper = resultados[2]
MB = resultados[3]
MK = resultados[4]
MP = resultados[5]
inventarios_historicos = resultados[6]
allMultas = MB + MK + MP

print("Inventarios al final del 1er año, luego de {} réplicas.".format(n))
print("        min   prom  max    Tmultas")
print("Bright:", end=" "); print(min(bright), end=" "); print(prom(bright), end=" "); print(max(bright), end="   "); print(sum(MB), end="\n")
print("Koala:", end="  "); print(min(koala), end=" "); print(prom(koala), end=" "); print(max(koala), end="   "); print(sum(MK), end="\n")
print("Paper:", end="  "); print(min(paper), end=" "); print(prom(paper), end=" "); print(max(paper), end="   "); print(sum(MP), end="\n")

replica1 = inventarios_historicos[0]
bright_r1 = replica1[0]
print(min(bright_r1))
plt.plot(range(1,361), bright_r1)
plt.plot(range(1, 361), [26884 for i in range(360)])
plt.show()