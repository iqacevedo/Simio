from random import choice

molinos = ["PaperTech", "KoalaPaper", "Bright"]

asignaciones =[(i, choice(molinos)) for i in range(1, 101)]

LO_de_PaperTech = [e[0] for e in asignaciones if e[1] == "PaperTech"]
LO_de_KoalaPaper = [e[0] for e in asignaciones if e[1] == "KoalaPaper"]
LO_de_Bright = [e[0] for e in asignaciones if e[1] == "Bright"]

print("Total de L.O. de PaperTech: ", len(LO_de_PaperTech))
print("Total de L.O. de KoalaPaper: ", len(LO_de_KoalaPaper))
print("Total de L.O. de Bright: ", len(LO_de_Bright))

print("L.O. de PaperTech: ", LO_de_PaperTech)
print("L.O. de KoalaPaper: ", LO_de_KoalaPaper)
print("L.O. de Bright: ", LO_de_Bright)
