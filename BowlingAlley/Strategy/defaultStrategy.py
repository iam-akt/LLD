from Strategy.strategy import StrategyInterface


class DefaultStrategy(StrategyInterface):
    def __init__(self):
        self.default_bonus=1
    def bonus(self):
        return self.default_bonus
