## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
a = list([(z[4]) for z in x[0:]])
h = ",".join(a)
j = h.split(',')
k = list([(z[0:3]) for z in j[0:]])
e = [int(z[4]) for z in j[0:]]
f = set(k)
d = list(f)
d.sort()
lenb = len(e)
lend = len(d)
for i in range(0,lend):
    max=e[i]
    min=e[i]
    for j in range(0,lenb):
        if k[j] == d[i]:
            if e[j] > max:
                max= e[j]
    for j in range(0,lenb):
        if k[j] == d[i]:
            if e[j] < min:
                min= e[j]
    print(d[i], end="")
    print(',', end="")
    print(min, end="")
    print(',', end="")
    print(max)
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
