import math
def readfile(string):
    #retorna os numeros do arquivo dado transformados em float
    file = open(string, "r")
    numbers = []
    for i in file:
        numbers.append(float(i))
    tam = len(numbers)
    file.close()
    return numbers,tam

def valormedio(x,len):
    #cacula e retorna a media dos tempos
    soma=sum(x)
    avg=soma/len
    return avg

def desviopadrao(media,numeros,len):
    #retorna desvio padrao
    x=0
    for i in range (0,len):
        x=x+pow(numeros[i]-media,2)
    desvio=math.sqrt(x/len)
    return desvio

#main
num=[0,0,0,0,0]
length=[0,0,0,0,0]
media=[0,0,0,0,0]
desvio=[0,0,0,0,0]
alturas=["altura1.txt","altura2.txt","altura3.txt","altura4.txt","altura5.txt"]

for i in range(0,5):
    num[i],length[i]=readfile(alturas[i])

for i in range(0,5):
    media[i]=valormedio(num[i],length[i])

for i in range(0,5):
    desvio[i]=desviopadrao(media[i],num[i],length[i])

#saida de dados
for i in range(0,5):
    print("media{}:".format(i+1),media[i],"\n","desvio{}:".format(i+1),desvio[i],"\n")

