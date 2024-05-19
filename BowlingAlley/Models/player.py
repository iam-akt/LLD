class Player:
    def __init__(self,name="abcd",id=None,scoreBoard=None):
        self.name=name
        self.id=id
        self.scoreBoard=scoreBoard
        self.isWin=False
    def get_player_name(self):
        return self.name
    def get_player_id(self):
        return self.id
    def get_win(self):
        return self.isWin
    def get_player_scoreBoard(self):
        return self.scoreBoard
    def set_player_name(self,name):
        self.name=name
    def set_player_id(self,id):
        self.id=id
    def set_win(self,isWin):
        self.isWin=isWin
    def set_player_scoreBoard(self,scoreBoard):
        self.scoreBoard=scoreBoard