from Constants.constant import Constant
from Models.player import Player
import random

class BowlingService:
    def __init__(self,players):
        self.players=players
        self.winner=Player()
    def playGame(self):
        maxScore=0
        for player in self.players:
            standingPins=Constant.Total_Pins
            for i in range(Constant.Max_Roll):
                numOfPinsDown=self.takeShot(standingPins)
                standingPins-=numOfPinsDown
                if i%2==1:
                    standingPins=self.refill()
                else:
                    if standingPins==0:
                        i+=1
                player.get_player_scoreBoard().roll(numOfPinsDown,i)
            totalScore=player.get_player_scoreBoard().score()
            if maxScore<totalScore:
                maxScore=totalScore
                self.winner=player
    def takeShot(self,standingPins):
        return random.randint(0,standingPins)
    def refill(self):
        return Constant.Total_Pins
    def getWinner(self):
        self.winner.set_win(True)
        return self.winner.get_player_name()

    