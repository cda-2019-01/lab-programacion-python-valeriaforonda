##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
a = list([(z[4]) for z in x[0:]])
h = ",".join(a)
j = h.split(',')
k = list([(z[0:3]) for z in j[0:]])
f = set(k)
d = list(f)
d.sort()
lend = len(d)
lenb = len(k)
for i in range(0,lend):
    n=0
    for j in range(0,lenb):
        if k[j] == d[i]:
            n = n +1
    print(d[i], end="")
    print(',', end="")
    print(n)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
