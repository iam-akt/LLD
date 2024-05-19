from models.expense import Expense
class ExpenseRepositort:
    def __init__(self):
        self.expenses=[]
        self.userMap={}
        self.balanceSheet={}
    def addUser(self,user):
        self.userMap[user.get_user_name()]=user
        self.balanceSheet[user.get_user_name()]={}
    def getUser(self,userName):
        return self.userMap[userName]
    def showBalance(self,userName):
        balance=[]
        for key,value in self.balanceSheet[userName].items():
            if value!=0:
                balance.append(self.checkSign(userName,key,value))
        return balance
    def showBalances(self):
        balance=[]
        for i in self.balanceSheet:
            for key,value in self.balanceSheet[i].items():
                if value!=0:
                    balance.append(self.checkSign(i,key,value))
        return balance
    def checkSign(self,userName1,userName2,amount):
        if amount<0:
            return userName1+" owes "+userName2+": "+str(-1*amount)
        elif amount>0:
            return userName1+" lends "+userName2+": "+str(amount)
        return ""
    def addExpense(self,amount,paidBy,splits,expenseData):
        expense = Expense(amount,paidBy,splits,expenseData)
        self.expenses.append(expense)
        for i in expense.getsplits():
            paidTo=i.getUser().get_user_name()
            if paidTo not in self.balanceSheet[paidBy]:
                self.balanceSheet[paidBy][paidTo]=0
            self.balanceSheet[paidBy][paidTo]+=i.getamount()
            if paidBy not in self.balanceSheet[paidTo]:
                self.balanceSheet[paidTo][paidBy]=0
            self.balanceSheet[paidTo][paidBy]-=i.getamount()