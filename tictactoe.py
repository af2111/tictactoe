from os import system
class Board:
    #initiere board 
    board = [
             [" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]
              ]
    #definition um board auszugeben
    def printBoard(self):
        print("Current Board: \n")
        for i in range(len(board.board)):
            print("|", end="")
            for field in board.board[i]:
                print(field + "|", end="")
            print("\n")
    def fullBoard(self):
        for row in self.board:
            for entry in row:
                if entry == " ":
                    return False
        return True
    #def um das board upzudaten
    def updateBoard(self, col, row, char):
        if self.board[col][row] == " ":
            self.board[col][row] = char
            print("Board wurde updated.")
        elif self.board[col][row] != " ":
            print("Feld ist besetzt. Bitte versuche es erneut.")
            return 0
        else:
            print("Ein Fehler ist aufgetreten. Wir bitten um dein Verständnis.")
    #check den winner
    def checkWinner(self):
        for i in range(len(self.board)):
            #check for horizontal
            if self.board[i][0] != " " and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != " " and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][0] != " " and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[2][0] != " " and self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return self.board[2][0]
        return 0
def gameloop():
    if gameloop.count % 2 == 0:
        char = 'x'
    elif gameloop.count % 2 == 1:
        char = 'o'
    board.printBoard()
    while True:
        while True:
            try:
                col = int(input("In welcher Zeile?")) - 1
                row = int(input("In welcher Spalte? ")) - 1
                system("clear")
                

                break
            except ValueError:
                system("clear")
                print("Ungültige Zahl. Gib neue Werte an.")
            
        try:
            if board.updateBoard(col, row, char) == 0:
                gameloop.count -= 1
            break
        except IndexError:
            print("Bitte gib als Zahl nur 1, 2 oder 3 an. Gib nun neue Zahlen an.")

    if board.checkWinner() == 'x':
        print("x hat gewonnen!")
        return
    elif board.checkWinner() == 'o':
        print("o hat gewonnen!")
        return
    elif board.fullBoard() and board.checkWinner() == 0:
        print("Unentschieden!")
        return
    gameloop.count += 1
    gameloop()
 


if __name__ == "__main__":
    system("clear")
    gameloop.count = 0
    board = Board()
    gameloop()