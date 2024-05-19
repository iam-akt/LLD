from model.player import Player
from model.dice import Dice
from services.snakeladderService import SnakeLadderService

#main

ladders = {}
snakes = {}
players=[]
print("Enter number snake and ladders ")
numberOfSnakes,numberOfLadders=map(int,input().split())
print("enter snakes")
for _ in range(numberOfSnakes):
    start,end=map(int,input().split())
    snakes[start]=end
print("enter ladders: ")
for _ in range(numberOfLadders):
    start,end=map(int,input().split())
    ladders[start]=end
print("enter number of players: ")
numberOfPlayers = int(input())
print("enter players")
for i in range(numberOfPlayers):
    print("enter ith player name")
    players.append(Player(str(input()),i+1,0))
print("Enter number of dice: ")
dice=Dice(int(input()))
snakeladderService=SnakeLadderService(ladders,snakes,players,dice)
board=snakeladderService.playGame()
for i in board:
    print("---------------------")
    print("name: ",i.get_player_name())
    print("rank: ",i.get_rank())
    print("---------------------")