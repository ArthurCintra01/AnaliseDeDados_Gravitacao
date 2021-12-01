import matplotlib.pylab as plt
import math
import numpy as np

def readfile():
    file= open("reduzido.txt")
    alturas = []
    medias = []
    desvios = []
    linhas = file.readlines()
    #colocando cada coluna do grafico em uma lista
    for x in linhas:
        alturas.append(x.split(' ')[0])
        medias.append(x.split(' ')[1])
        desvios.append(x.split(' ')[2])
    file.close()
    tam = len(alturas)
    #transformando os vetores de string para float
    for i in range(0, tam):
        alturas[i] = float(alturas[i])
        medias[i] = float(medias[i])
        desvios[i] = float(desvios[i])
    return alturas,medias,desvios,tam

def funcaogravidade(h):
    return math.sqrt((2*h)/9.81)

def plotgrafico(alturas,medias,desvios,tam):
    #plot tempos medios em relacao a altura
    for i in range(0, tam):
        plt.plot(alturas[i], medias[i], "ro")
    #barra de erro
    for i in range(0, tam):
        plt.vlines(alturas[i], (medias[i] + (desvios[i]/math.sqrt(5))), (medias[i] - (desvios[i]/math.sqrt(5))), "r")
    #plot curva tempo com g=9.81
    h = np.linspace(0.8, 2.2, 50)
    t = np.zeros(len(h))
    for i in range(len(t)):
        t[i] = funcaogravidade(h[i])
    plt.plot(h, t)
    #mostrar grafico
    plt.xlabel("Altura(m)")
    plt.ylabel("Tempo(s)")
    plt.grid()
    plt.show()

alturas,medias,desvios,tam=readfile()
plotgrafico(alturas,medias,desvios,tam)