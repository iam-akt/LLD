from models.board import Board
from exception.exception import ExceptionHandling
class TicTacToeService:
    def __init__(self,players,size):
        self.players=players
        self.board=Board(size)
    def playGame(self):
        self.board.printBoard()
        while True:
            player=self.players[0]
            print("enter position for ",player.get_player_name(),": ")
            x,y=map(int,input().split())
            if self.checkValid(x,y) and self.checkEmpty(x,y):
                self.board.setSymbol(x,y,player.get_symbol())
                self.board.printBoard()
                if self.checkWinner(x,y,player.get_symbol()):
                    return player
                self.players.append(self.players.pop(0))
            else:
                print("invalid input")
    def checkEmpty(self,x,y):
        return self.board.getBoard()[x][y]=="_"
    def checkValid(self,x,y):
        row,col=[len(self.board.getBoard())]*2
        return (x<row and x>=0 and y<col and y>=0)
    def checkWinner(self,x,y,symbol):
        row,col,left,right=True,True,True,True
        for i in range(len(self.board.getBoard())):
            if self.board.getBoard()[x][i]!=symbol:
                row=False
            if self.board.getBoard()[i][y]!=symbol:
                col=False
            if self.board.getBoard()[i][i]!=symbol:
                left=False
            if self.board.getBoard()[i][len(self.board.getBoard())-i-1]!=symbol:
                right=False
        return row or col or left or right