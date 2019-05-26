#coding=utf-8
x = open('data.csv','r').readlines() #Leo el archivo
x = [z.replace('\n', '') for z in x] #Reemplazo retornos de carro por vacíos
x = [z.split('\t') for z in x] #Se separan donde esté una separación
m =sum([int(z[1]) for z in x[0:]]) #Se vuelven enteros los valores de la segunda columna de la lista y se suman
print(m) #Se imprime la suma
