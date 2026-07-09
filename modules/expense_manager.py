from config import MONTHLY_BUDGET_FILE
from config import ADD_EXPENSE_FILE

#adding monthly amount
def add_monthly_expense(var_monthly_expense): #this function is used to add the monthly expenses in the file
    with open(MONTHLY_BUDGET_FILE,"w") as file:
        file.write(str(var_monthly_expense))
    print("MONTHLY AMOUNT SET: ",var_monthly_expense)

#adding expense into file and subtracting from monthly budget
def add_expense(expense_list):
    #opening expense file and appending new record
    with open(ADD_EXPENSE_FILE,"a") as file: #adding 
        file.write(f"{str(expense_list)}\n")
    
    #opening the monthly budget file and read the value from the file    
    with open(MONTHLY_BUDGET_FILE,"r") as file: 
        var_monthly_amount = float(file.read())
    
    #if the entered amount is less than available budget then it is will subtract from available balance
    if float(expense_list[0])<=var_monthly_amount:   
        var_monthly_amount = var_monthly_amount - float(expense_list[0])
        with open(MONTHLY_BUDGET_FILE,"w") as fileone:
            fileone.write(str(var_monthly_amount))
    #if the entered amount is not less than available budget then it will print available balance
    else: 
        print("Available Balance is low")
        
    print("**EXPENSE ADD***") #printing the entered expense
    print(str(expense_list))
 
#view expense   
def view_expense():
    print("***MONTHLY EXPENSE***")
    with open(ADD_EXPENSE_FILE,"r") as file:
        for line in file:
            print(line.strip())
            
#view remaining amount
def view_remaining_amount():
    with open(MONTHLY_BUDGET_FILE,"r") as file:
        monthly_budget = file.read()
    print(f"REMAINING BALANCE: {float(monthly_budget)}")