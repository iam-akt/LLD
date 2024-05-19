class Expense:
    def __init__(self,amount,paidBy,splits,expenseData):
        self.amount=amount
        self.paidBy=paidBy
        self.splits=splits
        self.expenseData=expenseData
    def getamount(self):
        return self.amount
    def getPaidBy(self):
        return self.paidBy
    def getsplits(self):
        return self.splits
    