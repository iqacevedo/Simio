from random import choice
with open("datos_aserradero.txt", "r") as file:
    lines = [i.split("-.") for i in file]
a = []
while len(a) <3:
    b = choice(lines)
    agregar = True
    for i in a:
        if b[1] == i[1]:
            agregar = False
    if agregar:
        a.append(b)
print(a)
