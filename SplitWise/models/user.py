class User:
    def __init__(self,name,id,mobileNumber):
        self.name=name
        self.id=id
        self.mobileNumber=mobileNumber
    def get_user_name(self):
        return self.name
    def get_user_id(self):
        return self.id
    def get_user_mobile(self):
        return self.mobileNumber
    def set_user_name(self,name):
        self.name=name
    def set_player_id(self,id):
        self.id=id
    def set_user_mobile(self,mobileNumber):
        self.mobileNumber=mobileNumber