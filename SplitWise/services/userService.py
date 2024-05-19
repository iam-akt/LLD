from models.user import User


class UserSerivce:
    def __init__(self,repository):
        self.repository=repository
    def addUser(self,user):
        self.repository.addUser(user)
    def getUser(self,userName):
        return self.repository.getUser(userName)