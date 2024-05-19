from functools import total_ordering
from Enum.bonus import Bonus
from Factory.bonusFactory import BonusFactory
from Models.scoreBoard import ScoreBoard
from Constants.constant import Constant

class ScoreBoardService(ScoreBoard):
    def __init__(self):
        self.rolls=[0]*Constant.Max_Roll
    def roll(self, noofpins,set):
        self.rolls[set]=noofpins
    def isStrike(self,set):
        return self.rolls[set]==10
    def isSpare(self,set):
        return self.rolls[set]+self.rolls[set+1]==10
    def score(self):
        set=0
        totalScore=0
        for i in range(Constant.Total_Sets):
            if self.isStrike(set):
                totalScore+=Constant.Total_Pins+BonusFactory().getStrategy(Bonus.Strike.name).bonus()
            elif self.isSpare(set):
                totalScore+=Constant.Total_Pins+BonusFactory().getStrategy(Bonus.Spare.name).bonus()
            else:
                totalScore+=self.rolls[set]+self.rolls[set+1]
            set+=2
        return totalScore+self.rolls[set]


