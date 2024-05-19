from models.players import Player
from services.tictactoeService import TicTacToeService
#main
print("enter player1 name and symbol: ")
player1=Player(str(input()),str(input()),1)

print("enter player2 name and symbol: ")
player2=Player(str(input()),str(input()),2)

players=[player1,player2]
print("enter size of board: ")
tictactoeService = TicTacToeService(players, int(input()))
winner = tictactoeService.playGame()
print("Winner is: ",winner.get_player_name())