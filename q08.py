##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
a = list([(z[4]) for z in x[0:]])
h = ",".join(a)
j = h.split(',')
k = [(z[1]) for z in x[0:]]
e = list([(z[0]) for z in x[0:]])
f = set(k)
d = list(f)
d.sort()
lenb = len(e)
lend = len(d)
import numpy as np
for i in range(0,lend):
    y=[]
    for j in range(0,lenb):
        if k[j] == d[i]:
            y.append(e[j])
            y.sort()
    u = d[i],y
    print(u)
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
