class Board:
    def __init__(self,size):
        self.size=size
        self.board=[["_" for _ in range(size)]for _ in range(size)]
    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j],end=" ")
            print()
        print()
    def getSymbol(self,x,y):
        return self.board[x][y]    
    def setSymbol(self,x,y,symbol):
        self.board[x][y]=symbol
    def getBoard(self):
        return self.board
