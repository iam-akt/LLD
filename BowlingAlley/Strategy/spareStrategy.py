from Strategy.strategy import StrategyInterface


class SpareStrategy(StrategyInterface):
    def __init__(self):
        self.spare_bonus=5
    def bonus(self):
        return self.spare_bonus
