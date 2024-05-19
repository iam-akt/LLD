#main
from models.user import User
from models.split import Split
from models.expensedata import ExpenseData
from repository.expenseRepository import ExpenseRepositort
from services.splitwiseServie import SplitWiseSerive
from services.userService import UserSerivce
from enums.type import Type
from enums.expenseType import ExpenseType

print("enter number of users: ")
expenseRepositort=ExpenseRepositort()
userservice = UserSerivce(expenseRepositort)
splitWiseSerive=SplitWiseSerive(expenseRepositort)
for i in range(int(input())):
    print("enter name of user: ")
    userservice.addUser(User(str(input()),i,234567890))
while(True):
    print("enter input: ")
    scan=str(input())
    data=list(scan.split(" "))
    type=data[0]
    if type==Type.Expense.name:
            username=data[1]
            ttlmember = int(data[3])
            expenseindex= 4+int(data[3])
            expensetype = data[expenseindex]
            splits=[]
            if expensetype==ExpenseType.Equal.name:
                    for i in range(ttlmember):
                        splits.append(Split(userservice.getUser(data[4+i]),int(data[2])/ttlmember))
                    splitWiseSerive.addExpense(int(data[2]),username,splits,ExpenseData(data[-1]))
            elif expensetype==ExpenseType.Exact.name:
                    for i in range(ttlmember):
                        splits.append(Split(userservice.getUser(data[4+i]),int(data[expenseindex+i+1])))
                    splitWiseSerive.addExpense(int(data[2]),username,splits,ExpenseData(data[-1]))
            elif expensetype==ExpenseType.Percent.name:
                    for i in range(ttlmember):
                        splits.append(Split(userservice.getUser(data[4+i]),(int(data[2])*(int(data[expenseindex+i+1])))/100))
                    splitWiseSerive.addExpense(int(data[2]),username,splits,ExpenseData(data[-1]))
    elif type==Type.Show.name:
            if len(data)==2:
                splitWiseSerive.balance(data[1])
            else:
                splitWiseSerive.balances()
    elif type== Type.quit.name:
            print("exiting_______________________")
            break