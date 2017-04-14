from random import choice, randint

molinos = ["KoalaPaper"]*30 + ["Bright"]*30 + ["PaperTech"]*40
archivo = open("datos_aserradero.txt", "w")

for i in range(1,101):
    ubicacion_molino = randint(0, len(molinos) - 1)
    fila = molinos.pop(ubicacion_molino)
    archivo.write("{}-.{}\n".format(i, fila))
archivo.close()