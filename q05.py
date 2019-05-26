## Imprima el valor maximo y minimo por cada letra de la columa 1.
x = open('data.csv','r').readlines() #Se lee el archivo
x = [z.replace('\n', '') for z in x]
x = [z.split('\t') for z in x]
b = [(z[0]) for z in x[0:]]
e=[int(z[1]) for z in x[0:]]
c = set(b)
d = list(c)
d.sort()
lenb = len(b)
lend = len(d)
for i in range(0,lend):
    max=e[i]
    min=e[i]
    for j in range(0,lenb):
        if b[j] == d[i]:
            if e[j] > max:
                max= e[j]
    for j in range(0,lenb):
        if b[j] == d[i]:
            if e[j] < min:
                min= e[j]
    print(d[i], end="")
    print(',', end="")
    print(max, end="")
    print(',', end="")
    print(min)
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
