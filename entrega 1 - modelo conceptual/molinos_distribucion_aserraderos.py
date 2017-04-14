from random import choice, randint

molinos = ["KoalaPaper"]*33 + ["Bright"]*33 + ["PaperTech"]*33 + [choice(["KoalaPaper", "Bright", "PaperTech"])]

archivo = open("datos_aserradero.txt", "w")

for i in range(1,101):
    ubicacion_molino = randint(0, len(molinos) - 1)
    mol = molinos.pop(ubicacion_molino)
    archivo.write("{}-.{}\n".format(i, mol))
    
archivo.close()
