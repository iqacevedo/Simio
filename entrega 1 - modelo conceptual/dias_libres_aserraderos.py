from random import choice, randint

archivo = open("datos_dias_libres.txt", "w")
dias = [0,0,0,1,2,3,4,5,6]
for i in range(1,101):
    aux = [0,0,0,0,0,0,0]
    cuantos_dias = choice([1,1,1,2])
    if cuantos_dias == 2:
        dia_1 = choice(dias)
        dia_2 = choice(dias)
        while dia_1 == dia_2:
            dia_2 = choice(dias)
        aux[dia_1] = 1
        aux[dia_2] = 1
    else:
        dia_1 = choice(dias)
        aux[dia_1] = 1

    aux = list(map(str, aux))
    archivo.write(",".join(aux) + "\n")
    
archivo.close()
