import sys
import os

parent_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(parent_dir)
#the above code is used to search the parent directory or above directory for imported file


#import statements
from modules.expense_manager import add_monthly_expense
from modules.expense_manager import add_expense
from modules.expense_manager import view_expense
from modules.expense_manager import view_remaining_amount

exit_menu_boolean = True #boolean variable for menu loop
        
while exit_menu_boolean:  #Loop to display the menu
    print("Press 1: Adding monthly budget")
    print("Press 2: Enter you expense")
    print("Press 3: View total expense")
    print("Press 4: Balance remaining from monthly expense")
    print("Press 5: Exit the menu")
    try:
        functionality = int(input("Enter a number:")) #it is use to choose option from the menu
        match functionality:
            case 1:
                print("\n")
                monthly_budget = float(input("Enter your monthly budget:"))
                add_monthly_expense(monthly_budget)
                print("\n")
            case 2:
                print("\n")
                expense_amount = float(input("Expense amount:"))
                expense_describe = str(input("Expense Details:"))
                expense_date = str(input("Enter expense date(DD-MM-YYYY):"))
                expense_list = [expense_amount,expense_describe,expense_date]
                add_expense(expense_list)
                print("\n")
            case 3:
                print("\n")
                view_expense()
                print("\n")
            case 4:
                print("\n")
                view_remaining_amount()
                print("\n")
            case 5:
                print("\n")
                exit_menu_boolean = False
                print("\n")
            case _:
                print("\n")
                print("Enter proper input")
                print("\n")   
    except ValueError:
        print("Program exit with excpetion")
        exit_menu_boolean = False

print("Thank you using our system")