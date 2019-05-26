##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
a = list([(z[4]) for z in x[0:]])
k = str(a)
g = list([(z[0]) for z in x[0:]])
import re 
cadena = re.sub("\D", "", k)
b = list(cadena)
e = [int(z[0]) for z in b[0:]]
h = [z.split(',') for z in a]
lena = len(a)
cont=0
for i in range(0,lena):
    if i == 0:
        sum=0
        u = (len(h[i]))
        for j in range(cont,u):
            sum = sum + e[j]
            cont=u
    elif i == 1:
        sum=0
        u = (len(h[i]))
        s = cont + 1
        r = s + u
        for j in range(s,r):
            sum = sum + e[j]
    elif i > 1:
        sum=0
        s = s + u
        u = (len(h[i]))
        r = s + u
        for j in range(s,r):
            sum = sum + e[j-1]
    print(g[i], end="")
    print(',', end="")
    print(sum)
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
