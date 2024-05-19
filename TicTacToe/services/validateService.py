class Validation:
    def __init__(self,board):
        self.board=board
    def checkEmpty(self,x,y):
        return self.board[x][y]=="_"
    def checkValid(self,x,y):
        row,col=[len(self.board)]*2
        return (x<row and x>=0 and y<col and y>=0)
    def checkBoard(self,x,y,symbol):
        row,col,left,right=[True]*4
        for i in range(len(self.board)):
            if self.board[x][i]==symbol:
                row=False
            if self.board[i][y]==symbol:
                col=False
            if self.board[i][i]==symbol:
                row=False
            if self.board[i][len(self.board)-i-1]==symbol:
                row=False
        return row or col or left or right