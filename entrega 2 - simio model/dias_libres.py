from random import choice, random

#Se agrega varias veces la tupla (Domingo,1), ya que es el día que más se escoge para descansar
dias = [("Domingo", 1),("Domingo", 1),("Domingo", 1),("Domingo", 1),("Lunes", 2),("Martes", 3),("Miércoles", 4),("Jueves", 5), ("Viernes", 6), ("Sábado", 7)]
texto_dias = open("dias_aserradero_texto.txt", "w")
numeros_dias = open("dias_aserradero_numero.txt", "w")
for i in range(1,101):
    dia = choice(dias)
    if random() < 0.5:
        texto_dias.write(str(i)+"-."+dia[0] + "\n")
        numeros_dias.write(str(dia[1])+"-"+str(dia[1])+"\n")
    else:
        dia2 = choice(dias)
        while dia == dia2:
            dia2 = choice(dias)
        texto_dias.write(str(i) + "-." + dia[0]+"-"+ dia2[0] + "\n")
        numeros_dias.write(str(dia[1]) + "-" + str(dia2[1])+"\n")
texto_dias.close()
numeros_dias.close()

