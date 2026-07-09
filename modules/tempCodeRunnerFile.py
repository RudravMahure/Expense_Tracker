from config import MONTHLY_BUDGET_FILE

def add_monthly_expense(var_monthly_expense): #this function is used to add the monthly expenses in the file
    print(var_monthly_expense)
    with open(MONTHLY_BUDGET_FILE,"w") as file:
        file.write(str(var_monthly_expense))
