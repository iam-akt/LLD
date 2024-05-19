from _typeshed import self


class Player:
    def __init__(self,name,id,position):
        self.name=name
        self.id=id
        self.playerPosition=position
        self.isWin=False
        self.rank=None
    def get_player_name(self):
        return self.name
    def get_player_id(self):
        return self.id
    def get_win(self):
        return self.isWin
    def get_player_position(self):
        return self.playerPosition
    def get_rank(self):
        return self.rank
    def set_player_name(self,name):
        self.name=name
    def set_player_id(self,id):
        self.id=id
    def set_win(self,isWin):
        self.isWin=isWin
    def set_player_position(self,position):
        self.playerPosition=position
    def set_rank(self,rank):
        self.rank=rank