##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
a = list([(z[4]) for z in x[0:]])
k = list([(z[3]) for z in x[0:]])
e = [z.split(',') for z in k]
d = list([(z[0]) for z in x[0:]])
m = list([(z[4]) for z in x[0:]])
h = [z.split(',') for z in m]
lend = len(d)
import math
for i in range(0,lend):
    v = len(e[i])
    u = math.floor(len(h[i]))
    print(d[i], end="")
    print(',', end="")
    print(v, end="")
    print(',', end="")
    print(u)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
