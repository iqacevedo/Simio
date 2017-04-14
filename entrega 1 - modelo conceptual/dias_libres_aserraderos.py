from random import choice, randint

archivo = open("datos_dias_libres.txt", "w")
for i in range(1,101):
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"] + ["Domingo"]*3
    cuantos_dias = choice([1, 2])
    if cuantos_dias == 2:
        dia_1 = choice(dias)
        dia_2 = choice(dias)
        while dia_1 == dia_2:
            dia_2 = choice(dias)
        fila = "[{}-{}]".format(dia_1, dia_2)
    else:
        fila = "[{}]".format(choice(dias))
    archivo.write("{}-.{}\n".format(i, fila))
archivo.close()
