from Strategy.strategy import StrategyInterface


class StrikeStrategy(StrategyInterface):
    def __init__(self):
        self.strike_bonus=10
    def bonus(self):
        return self.strike_bonus
