##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
a = list([(z[3]) for z in x[0:]])
h = [int(z[1]) for z in x[0:]]
e = list(h)
b = [z.split(',') for z in a]
c = list([(z[0]) for z in b[0:]])
d = list(set(c))
d.sort()
lenb = len(b)
lend = len(d)
for m in range (0,lend):
    sum = 0
    for i in range(0,lenb):
        v = len(b[i])
        u = b[i]
        for j in range (0, v):
            if u[j] == d[m]:
                sum = sum + e[i]
    print(d[m], end="")
    print(',', end="")
    print(sum)
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
