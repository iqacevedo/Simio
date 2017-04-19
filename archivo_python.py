import math
import random

Mills = ["B"]*30 + ["K"]*30 + ["P"]*40

class Aserradero:
    MyId = 1
    def __init__(self, distancia):
        self.distancia = distancia
        self.MyId = Aserradero.MyId
        self.camiones = random.randint(4, 6)
        Aserradero.MyId += 1
        self.mill = random.choice(Mills)
        Mills.remove(self.mill)
        self.camionadas = 0
        self.madera_diaria = 0
        self.madera_total = 0
        self.dias_libres = [random.randint(0,6)]
        if random.random()>0.5:
            nuevo_dia = random.randint(0, 6)
            while nuevo_dia == self.dias_libres[0]:
                nuevo_dia = random.randint(0, 6)

aserraderos = []
for i in range(5, 100, 10):
    for j in range(5, 100, 10):
        aserraderos.append(Aserradero(math.sqrt(((i - 50)**2) + ((j- 50)**2))))

fehca_1 = 13
fecha_2 = 9
fecha_3 = 52- fecha_2 - fehca_1

costo_transporte = 0
ton_madera = 0
costo_inventario = 0
cargas_diarias = [[0] * 730]*3
demanda = [[random.normalvariate(4000, 200)] * 730, [random.normalvariate(4000, 200)] * 730, [random.triangular(4500, 5500, 5000)] * 730]
inventario = [60000, 60000, 55000]
stock_out = [0,0,0]

for i in range(730):
    if i in list(range(fehca_1)):
        for j in aserraderos:
            if j.mill == "B":
                dema = (demanda[0][i] / 30) /30
            elif j.mill == "K":
                dema = (demanda[1][i] / 30) / 30
            else:
                dema = (demanda[2][i] / 30) / 30
            j.camionadas = int(min(random.choice([6,7,8]), dema))
            if i % 7 in j.dias_libres:
                j.madera_diaria = 0
            else:
                for k in range(j.camionadas):
                    madera = random.uniform(25,35)
                    j.madera_diaria += madera
                    costo_transporte += (j.distancia*0.12* madera )
                    j.madera_total += madera
                    ton_madera += madera

    elif i in list(range(fehca_1, fehca_1 + fecha_2)):
        if random.random() > 0.95:
            for j in aserraderos:
                j.camionadas = 0
                j.madera_diaria = 0
        else:
            for j in aserraderos:
                if j.mill == "B":
                    dema = (demanda[0][i] / 30) / 30
                elif j.mill == "K":
                    dema = (demanda[1][i] / 30) / 30
                else:
                    dema = (demanda[2][i] / 30) / 30
                j.camionadas = int(min(random.choice([3,4,5]), dema))
                if i % 7 in j.dias_libres:
                    j.madera_diaria = 0
                else:
                    for k in range(j.camionadas):
                        madera = random.uniform(25, 35)
                        j.madera_diaria += madera
                        costo_transporte += (j.distancia * 0.12 * madera)
                        j.madera_total += madera
                        ton_madera += madera
    else:
        for j in aserraderos:
            if j.mill == "B":
                dema = (demanda[0][i] / 30) / 40
            elif j.mill == "K":
                dema = (demanda[1][i] / 30) / 40
            else:
                dema = (demanda[2][i] / 30) / 40
            j.camionadas = int(min(random.choice([5,6,7]), dema))
            if i % 7 in j.dias_libres:
                j.madera_diaria = 0
            else:
                for k in range(j.camionadas):
                    madera = random.uniform(25, 35)
                    j.madera_diaria += madera
                    costo_transporte += (j.distancia * 0.12 * madera)
                    j.madera_total += madera
                    ton_madera += madera
    for aserradero in aserraderos:
        if aserradero.mill == "B":
            indice = 0
        elif aserradero.mill == "K":
            indice = 1
        else:
            indice = 2
        inventario[indice] += aserradero.madera_diaria
    inventario[0] -= demanda[0][i]
    inventario[1] -= demanda[1][i]
    inventario[2] -= demanda[2][i]
    for l in range(3):
        if inventario[l] < 0:
            inventario[l] = 0
            stock_out[l] += 1

    costo_inventario += (inventario[0] + inventario[1] + inventario[2])*50*0.06

print(costo_transporte, "costo_transporte")
print(costo_inventario, "costo_inventario")
print(sum([o.madera_total for o in aserraderos]), "total_madera")
print(stock_out, "stock_out")

