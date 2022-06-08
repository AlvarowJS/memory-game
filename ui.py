print('**************************************')
print('Juego "Encuentra su par"')
print('**************************************')

print('Ingrese el numero de filas y columnas del Juego')
print('El toal de casillero (filas x columnas) debe ser par!')

fila = int(input('Ingrese el numero de filas: '))
columna = int(input('Ingrese el numero de columnas'))
print(end = "   ")
for x in range(1,columna+1,1):
    print(x, end=" ")
print()
for i in range(1,fila+1,1):
    print(i, end=" ")
    print('|', end=" ")
    for j in range(1, columna+1,1):
        print('|', end=" ")
    print()
    
    
