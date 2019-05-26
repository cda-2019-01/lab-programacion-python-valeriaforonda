#coding=utf-8
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
b = [(z[0]) for z in x[0:]] #Se extrae la primera columna del archivo
e=[int(z[1]) for z in x[0:]] #Se extrae la columna 2 (posición 1) como entero para poder hacer la suma
c = set(b) #Valores únicos de las letras
d = list(c) #Lista de valores únicos
d.sort() #Lista ordenada
lenb = len(b) #Total de registros
lend = len(d) #Total de valores únicos
for i in range(0,lend): #De 0 a todos los valores únicos
    n=0 #Se inicializa el conteo
    for j in range(0,lenb): #De 0 a todos los registros
        if b[j] == d[i]: #Si la letra de la fila corresponde al valor único
            n = n + e[j] #Se suma el valor correspondiente a esa fila
    print(d[i], end="") #Se imprime el valor único
    print(',', end="") #Se imprime la separación por coma
    print(n) #Se imprime la suma
## A,37
## B,36
## C,27
## D,23
## E,67
##
