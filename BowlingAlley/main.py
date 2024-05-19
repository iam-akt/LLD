from Models.player import Player
from Services.BowlingService import BowlingService
from Services.scoreBoardService import ScoreBoardService
#main

print("enter number of players: ")
players=[]
for i in range(int(input())):
    print("Enter Player Name: ")
    players.append(Player(str(input()),i,ScoreBoardService()))
bowlingService=BowlingService(players)
bowlingService.playGame()
print("---------------------------------")
print("Winner is: ",bowlingService.getWinner())
print("---------------------------------")


