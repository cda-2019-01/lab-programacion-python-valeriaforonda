#coding=utf-8
## Imprima la cantidad de registros por cada mes.
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
b = [z[2].split('-')[1] for z in x[0:]]
a=list(set([z[2].split('-')[1] for z in x[0:]]))
a.sort()
lenb = len(b)
lena = len(a)
for i in range(0,lena):
    n=0
    for j in range(0,lenb):
        if b[j] == a[i]:
            n = n + 1
    print(a[i], end="")
    print(',', end="")
    print(n)
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
