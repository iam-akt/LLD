from Enum.bonus import Bonus
from Strategy.defaultStrategy import DefaultStrategy
from Strategy.spareStrategy import SpareStrategy
from Strategy.strikeStrategy import StrikeStrategy

class BonusFactory:
    def getStrategy(self,bonus):
        if bonus==Bonus.Spare.name:
            return SpareStrategy()
        elif bonus==Bonus.Strike.name:
            return StrikeStrategy()
        else:
            return DefaultStrategy()
        