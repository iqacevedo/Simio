def aaa():
    with open("hola.txt", "r") as file:
        a = file.readlines()
        c = []
        for i in a:
            for j in range(30):
                with open("chao.txt", "a") as file2:
                    file2.write(i)

def bbb():
    with open("pasion.txt", "r") as file:
        dicc = dict()
        for linea in file:
            datos = linea[:-1].split(";")
            if datos[0] in dicc:
                if datos[1] in dicc[datos[0]]:
                    dicc[datos[0]][datos[1]] += float(datos[3].replace(",", "."))
                else:
                    dicc[datos[0]][datos[1]] = float(
                        datos[3].replace(",", "."))
            else:
                dicc[datos[0]] = dict()
                dicc[datos[0]][datos[1]] = float(datos[3].replace(",", "."))
    for j in dicc:
        a = "Input@KoalaPesajeEntrada"
        b = "Input@PaperPesajeEntrad"
        c = "Input@BrightPesajeEntrada"
        with open("salida.txt", "a") as file2:
            e = str(int(dicc[j][c])).replace(".", ",")
            f = str(int(dicc[j][a])).replace(".", ",")
            g = str(int(dicc[j][b])).replace(".", ",")
            file2.write("{};{};{};{}\n".format(j, e,f,g))

bbb()




