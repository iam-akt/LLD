from _typeshed import self
from model.board import Board

class SnakeLadderService:
    def __init__(self,ladders,snakes,players,dice):
        self.board=Board(ladders,snakes,players)
        self.dice=dice
    def playGame(self):
        i=1
        response=[]
        players=self.board.get_players()
        ladders=self.board.get_ladders()
        snakes=self.board.get_snakes()
        while(players!=[]):
            outputString=""
            player=players.pop(0)
            outputString+=player.get_player_name()
            currentPosition=player.get_player_position()
            throwDice=self.dice.getDiceNumbers()
            newPosition=currentPosition+throwDice
            if newPosition<=100:
                outputString+=" rolled a "+str(throwDice)+" and moved from "+str(currentPosition)
                if newPosition in ladders:
                    outputString+=" after ladder ride "
                    player.set_player_position(ladders[newPosition])
                elif newPosition in snakes:
                    outputString+=" after snakes dinner "
                    player.set_player_position(snakes[newPosition])
                else:
                    player.set_player_position(newPosition)
                outputString+=" to "+str(player.get_player_position())
                print(outputString)
            if self.isPlayerWon(player):
                player.isWin=True
                player.set_rank(i)
                i+=1
                response.append(player)
            else:
                players.append(player)
        return response
    def isPlayerWon(self,player):
        return player.get_player_position()>=100
    

