import random
class Dice:
    def __init__(self,N):
        self.numberOfDice=N
    def getDiceNumbers(self):
        return random.randint(1,self.numberOfDice*6)