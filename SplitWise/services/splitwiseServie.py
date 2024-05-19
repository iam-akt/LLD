class SplitWiseSerive:
    def __init__(self,repository):
        self.repository=repository
    def addExpense(self,amount,paidBy,splits,expenseName):
        self.repository.addExpense(amount,paidBy,splits,expenseName)
    def balance(self,userName):
        balance=self.repository.showBalance(userName)
        if balance==[]:
            print("No Balance")
        else:
            for i in balance:
                print(i)
    def balances(self):
        balances=self.repository.showBalances()
        if balances==[]:
            print("No Balance")
        else:
            for i in balances:
                print(i)