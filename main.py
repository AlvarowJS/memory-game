from operator import eq
from random import randint


class Main:

    def __init__(self, fila, columna):

        # constructor
        self.fila = fila
        self.columna = columna
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


    def printAsterisk(self):
        for i in range(0, self.fila, 1):
            for j in range(0, self.columna, 1):
                self.boards = '*'
                
                

    def printBoard(self):

        print(end="  ")
        for x in range(1, self.columna+1, 1):
            print(x, end=" ")
        print()
        for i in range(0, self.fila, 1):
            print(i+1, end="")
            print('|', end="")
            for j in range(0, self.columna, 1):
                print(self.boards, end="")
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
    def gameOver(self):
        for i in range(0, self.fila):
            for j in range(0, self.columna):
                if self.boards.__eq__('*'):
                    return False
        return True

    def checkInput(self, cards):
        while True:
            if not main.gameOver():
                first = str(input('Abra una casilla en formato Fila, Columna ej: 1,2 : '))
                fila1=int(first[0])
                columna1=int(first[2])

                print(type(int(fila1)))
                print(self.cards)
                # if not eq(self.boards[fila1-1][columna1-1],'*'):
                #     print('Ese casillero ya fue abierto')
                #     main.printBoard()
                #     continue
                # else:
                #     self.boards[fila1-1][columna1-1] = self.cards[fila1-columna1]
                #     main.printBoard()


                # second = str(input('Busca las casilla donde este la segunda letra: ',))
                # fila2 = second[0]
                # columna2 = second[2]

                # if not eq(self.boards[fila2-1][columna2-1],'*'):
                #     print('Ese casillero ya fue abierto')
                #     continue

                # else:
                #     self.boards[fila2-1][columna2-1] = self.cards[fila2-columna2]

                #     if eq(self.boards[fila1-1][columna1-1],self.boards[fila2-1][columna2-1]):
                #         main.printBoard()
                #     else:
                #         self.boards[fila1-1][columna1-1] = "*"
                #         self.boards[fila2-1][columna2-1] = "*"
                #         main.printBoard()
            else:
                print("Fin del juego ")    
                break

                
if __name__ == '__main__':
    main = Main(2, 2)
    cards = [[], []]
    main.menuGame()

    main.shuffleCard()
    main.printAsterisk()    
    main.printBoard()

    main.checkInput(cards)
    # main.printBoard()
