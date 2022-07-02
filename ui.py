from operator import index
from random import randint


class Main:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columnas = columna
        self.boards = [[], []]
        self.cards = [[], []]

    def menuGame(self):
        print('**************************************')
        print('Juego "Encuentra su par"')
        print('**************************************')

        print('Ingrese el numero de filas y columnas del Juego')
        print('El toal de casillero (filas x columnas) debe ser par!')

        self.fila = int(input('Ingrese el numero de filas: '))
        self.columna = int(input('Ingrese el numero de columnas: '))

    def printBoard(self):

        print(end="   ")
        for x in range(1, self.columna+1, 1):
            print(" ",x, end="")
        print()
        for i in range(1, self.fila+1, 1):
            print(i, end="")
            print('|', end="")
            for j in range(2, self.columna+1, 1):
                print(self.boards[j:i], end="")
                print('|', end="")
            print()

    def shuffleCard(self):

        ascci = 65
        limit = int(ascci + (self.fila * self.columna)/2)
        letter = []

        for k in range(ascci, limit, 1):
            letter.append(chr(k))
            letter.append(chr(k))

        for i in range(0, self.fila, 1):
            for j in range(0, self.columna, 1):
                index = randint(0, len(letter)-1)
                self.cards = letter[index]

                del letter[index]
                print(letter)



# print('**************************************')
# print('Juego "Encuentra su par"')
# print('**************************************')

# print('Ingrese el numero de filas y columnas del Juego')
# print('El toal de casillero (filas x columnas) debe ser par!')


# fila = int(input('Ingrese el numero de filas: '))
# columna = int(input('Ingrese el numero de columnas: '))
# print(end = "   ")
# for x in range(1,columna+1,1):
#     print(x, end=" ")
# print()
# for i in range(1,fila+1,1):
#     print(i, end=" ")
#     print('|', end=" ")
#     for j in range(1, columna+1,1):
#         print('|', end=" ")
#     print()
