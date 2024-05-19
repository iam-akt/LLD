class Board:
    def __init__(self,ladders,snakes,players):
        self.ladders=ladders
        self.snakes=snakes
        self.players=players
    def get_snakes(self):
        return self.snakes
    def get_ladders(self):
        return self.ladders
    def get_players(self):
        return self.players