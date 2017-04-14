from random import randint
with open("maximo_camiones.txt", "w") as file:
    for i in range(100):
        file.write(str(randint(4,6)) + "\n")