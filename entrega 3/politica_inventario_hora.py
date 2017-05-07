import numpy.random as n
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
    #Enero 2017
    for i in range(31):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 3.3 * 30) / 24
            inv_K += (29.4 * 3.2 * 30) / 24
            inv_P += (36.9 * 3.6 * 30) / 24
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Enero", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Febrero 2017
    for i in range(28):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4.65 * 30)/24
            inv_K += (29.4 * 4.5 * 30)/24
            inv_P += (36.9 * 4.5 * 30)/24
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Febrero", inv_B, inv_K, inv_P)

    ###############################################################################################3
    #Marzo 2017

    #PARA BRIGHT
    for i in range(13):
        dema_b = normalvariate(4000, 100)
        for j in range(24):
            inv_B += (28.43 * 4.7 * 30) / 24
            inv_B -= dema_b/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))

    for i in range(18):
        dema_b = normalvariate(4000, 100)
        for j in range(24):
            inv_B += (28.43 * 7 * 30) / 24  #Maxima Capacidad, que en esta temporada es en promedio 7
            inv_B -= dema_b/24
            multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))

    #PARA KOALA
    for i in range(17):
        dema_k = normalvariate(4000, 200)
        for j in range(24):
            inv_K += (29.4 * 4.5 * 30) / 24
            inv_K -= dema_k/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[1].append(round(inv_K))

    for i in range(14):
        dema_k = normalvariate(4000, 200)
        for j in range(24):
            inv_K += (29.4 * 7 * 30) / 24  # Máxima Capacidad, que en esta temporada es en promedio 7
            inv_K -= dema_k/24
            multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[1].append(round(inv_K))

    #PARA PAPER
    for i in range(19):
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_P += (36.9 * 4.5 * 30) / 24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[2].append(round(inv_P))

    for i in range(12):
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_P += (36.9 * 7 * 30) / 24  # Máxima Capacidad, que en esta temporada es en promedio 7
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Marzo", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Abril 2017
    for i in range(30):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4 * 30) / 24  # Máxima Capacidad, que en esta temporada es en promedio 4
            inv_K += (29.4 * 4 * 30) / 24  # Máxima Capacidad
            inv_P += (36.9 * 4 * 30) / 24  # Máxima Capacidad
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Abril", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Mayo 2017
    for i in range(31):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4 * 30)/24  #Máxima Capacidad, que en esta temporada es en promedio 4
            inv_K += (29.4 * 4 * 30)/24   #Máxima Capacidad
            inv_P += (36.9 * 4 * 30)/24   #Máxima Capacidad
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Mayo", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Meses de Junio a Diciembre 2017
    for i in range(214):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4.7 * 30)/24
            inv_K += (29.4 * 4.55 * 30)/24
            inv_P += (36.9 * 4.5 * 30)/24
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Diciembre", inv_B, inv_K, inv_P)

    if imprimir:
        print("                Bright Koala Paper")
        print("1 de Enero:", round(inv_B), round(inv_K), round(inv_P))

    ###############################################################################################3
    #Enero 2018
    for i in range(31):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4.7 * 30) / 24
            inv_K += (29.4 * 4.55 * 30) / 24
            inv_P += (36.9 * 4.5 * 30) / 24
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Enero", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Febrero 2018
    for i in range(28):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4.7 * 30)/24
            inv_K += (29.4 * 4.55 * 30)/24
            inv_P += (36.9 * 4.5 * 30)/24
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Febrero", inv_B, inv_K, inv_P)

    ###############################################################################################3
    #Marzo 2018

    #PARA BRIGHT
    for i in range(12):
        dema_b = normalvariate(4000, 100)
        for j in range(24):
            inv_B += (28.43 * 4.7 * 30) / 24
            inv_B -= dema_b/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))

    for i in range(19):
        dema_b = normalvariate(4000, 100)
        for j in range(24):
            inv_B += (28.43 * 7 * 30) / 24  #Maxima Capacidad, que en esta temporada es en promedio 7
            inv_B -= dema_b/24
            multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))

    #PARA KOALA
    for i in range(17):
        dema_k = normalvariate(4000, 200)
        for j in range(24):
            inv_K += (29.4 * 4.5 * 30) / 24
            inv_K -= dema_k/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[1].append(round(inv_K))

    for i in range(14):
        dema_k = normalvariate(4000, 200)
        for j in range(24):
            inv_K += (29.4 * 7 * 30) / 24  # Máxima Capacidad, que en esta temporada es en promedio 7
            inv_K -= dema_k/24
            multas_B,multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[1].append(round(inv_K))

    #PARA PAPER
    for i in range(19):
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_P += (36.9 * 4.5 * 30) / 24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[2].append(round(inv_P))

    for i in range(12):
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_P += (36.9 * 7 * 30) / 24  # Máxima Capacidad, que en esta temporada es en promedio 7
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Marzo", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Abril 2018
    for i in range(30):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4 * 30) / 24  # Máxima Capacidad, que en esta temporada es en promedio 4
            inv_K += (29.4 * 4 * 30) / 24  # Máxima Capacidad
            inv_P += (36.9 * 4 * 30) / 24  # Máxima Capacidad
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Abril", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Mayo 2018
    for i in range(31):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4 * 30)/24  #Máxima Capacidad, que en esta temporada es en promedio 4
            inv_K += (29.4 * 4 * 30)/24   #Máxima Capacidad
            inv_P += (36.9 * 4 * 30)/24   #Máxima Capacidad
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
            multas_B, multas_K, multas_P = calcular_multas(inv_B, inv_K, inv_P, multas_B, multas_K, multas_P)
            inventarios_historicos[0].append(round(inv_B))
            inventarios_historicos[1].append(round(inv_K))
            inventarios_historicos[2].append(round(inv_P))

    if imprimir:
        imprimir_inv("Mayo", inv_B, inv_K, inv_P)

    ###############################################################################################3

    #Meses de Junio a Diciembre 2018
    for i in range(214):
        dema_b = normalvariate(4000, 100)
        dema_k = normalvariate(4000, 200)
        dema_p = triangular(4500, 5000, 5500)
        for j in range(24):
            inv_B += (28.43 * 4.7 * 30)/24
            inv_K += (29.4 * 4.55 * 30)/24
            inv_P += (36.9 * 4.5 * 30)/24
            inv_B -= dema_b/24
            inv_K -= dema_k/24
            inv_P -= dema_p/24
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

def graficar_inventarios_replica(j, inventarios_historicos):

    replicaJ = inventarios_historicos[j-1]
    bright_r1 = replicaJ[0]
    koala_r1 = replicaJ[1]
    paper_r1 = replicaJ[2]

    minimo_b_1 = min(bright_r1)
    minimo_k_1 = min(koala_r1)
    minimo_p_1 = min(paper_r1)
    #print(minimo_b_1, minimo_k_1, minimo_p_1)

    plt.plot(range(1,2*365*24+1), bright_r1, color="orange")
    plt.plot(range(1,2*365*24+1), koala_r1, color="blue")
    plt.plot(range(1,2*365*24+1), paper_r1, color="red")
    plt.plot([2160 for i in range(10)], [20000 + i * 4500 for i in range(10)], color = "black")
    plt.plot([3600 for i in range(10)], [20000 + i * 4500 for i in range(10)], color="black")
    plt.plot([8640 for i in range(10)], [20000 + i*4500 for i in range(10)], color = "black")
    plt.plot([10800 for i in range(10)], [20000 + i * 4500 for i in range(10)],color="black")
    plt.plot([12240 for i in range(10)], [20000 + i * 4500 for i in range(10)],color="black")
    plt.ylim(20000, 65000)
    plt.title("Inventory during 2 years of Simulation\n orange = Bright, blue = Koala, red = Paper")
    plt.xlabel("Hours")
    plt.ylabel("Inventory")
    #plt.plot(range(1, 361*24), [minimo_b_1 for i in range(360*24)])
    plt.show()

def SIMULACION_FINAL(n):
    n=1
    replicas = [SIMULAR_AÑO(0) for i in range(n)]
    resultados = list(zip(*replicas))

    bright_end_year = resultados[0]
    koala_end_year = resultados[1]
    paper_end_year = resultados[2]
    MB = resultados[3]
    MK = resultados[4]
    MP = resultados[5]
    inventarios_historicos = resultados[6]
    historic_bright = [inventarios_historicos[j][0] for j in range(n)]
    print(len(historic_bright))
    allMultas = MB + MK + MP

    """
    print("Estadistica al final del 1er año, luego de {} réplicas.".format(n))
    print("        min   prom  max    Tmultas")
    print("Bright:", end=" "); print(min(bright_end_year), end=" "); print(prom(bright_end_year), end=" "); print(max(bright_end_year), end="   "); print(sum(MB), end="\n")
    print("Koala:", end="  "); print(min(koala_end_year), end=" "); print(prom(koala_end_year), end=" "); print(max(koala_end_year), end="   "); print(sum(MK), end="\n")
    print("Paper:", end="  "); print(min(paper_end_year), end=" "); print(prom(paper_end_year), end=" "); print(max(paper_end_year), end="   "); print(sum(MP), end="\n")
    """

    graficar_inventarios_replica(1, inventarios_historicos)


SIMULACION_FINAL(10)
