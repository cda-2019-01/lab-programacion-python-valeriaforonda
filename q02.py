#coding=utf-8
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
b = [(z[0]) for z in x[0:]] #Se extraen los valores de la primera columna
c = set(b) #Se obtienen los valores únicos de la primera columna
d = list(c) #Esos valores únicos, se convierten de string a lista
d.sort() #Se ordenan los valores únicos
lenb = len(b) #Se calcula la longitud del vector b (cantidad de filas totales)
lend = len(d) #Se calcula la longitud del vector d (cantidad de valores únicos)
for i in range(0,lend): #Se inicia el ciclo, desde la posición 0 hasta el total de valores únicos
    n=0 #Se inicializa el conteo en cero
    for j in range(0,lenb): #Ciclo que recorre cada uno de los registros (filas)
        if b[j] == d[i]: #Si la letra de cada fila coincide con la letra del vector de valores únicos, entra al ciclo
            n = n +1 #Y suma 1 al contador
    print(d[i], end="") #Se imprime la letra única
    print(',', end="") #Se imprime la separación por comas
    print(n) #Se imprime el contador
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
