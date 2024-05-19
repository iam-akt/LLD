class Player:
    def __init__(self,name,symbol,id):
        self.name=name
        self.id=id
        self.symbol=symbol
        self.isWin=False
    def get_player_name(self):
        return self.name
    def get_player_id(self):
        return self.id
    def get_symbol(self):
        return self.symbol
    def get_win(self):
        return self.isWin
    def set_player_name(self,name):
        self.name=name
    def set_player_id(self,id):
        self.id=id
    def set_symbol(self,symbol):
        self.symbol=symbol
    def set_win(self,isWin):
        self.isWin=isWin