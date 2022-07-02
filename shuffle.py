
from random import randint

card = [[],[]]
fila = int(input('Ingrese el numero de filas: '))
columna = int(input('Ingrese el numero de columnas'))
ascci = 65
limit = int(ascci + (fila * columna)/2)
size = limit - ascci
letter = []

for k in range(ascci, limit,1):
    letter.append(chr(k))
    letter.append(chr(k))

print(letter)
for i in range(0, fila, 1):
    for j in range(0, columna, 1):
        index = randint(0,len(letter)-1)       
        card = letter[index]
        
        del letter[index]
        print(letter)
# print(letter)       

