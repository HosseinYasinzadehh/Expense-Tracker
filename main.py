expenses = []

MENU = """
1. Add expense
2. View expenses
3. Show total
4. Delete expense
5. Exit
"""

def add_expense(expenses):
    desc = input("Please enter description: ")

    while True:
        try:
            amount = int(input("Please enter amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    new_exp = {"description": desc, "amount": amount}
    expenses.append(new_exp)

while True:
    print("💰 Expense Tracker")
    print(MENU)


    try:
        user_choice = int(input("Choose an option: "))
    except ValueError:
        print("enter number between 1 to 5")
        continue
    if user_choice == 5:
        break
    elif user_choice == 1:
        add_expense(expenses)
    elif user_choice == 2:
        print(f"your choice = {user_choice}")
    elif user_choice == 3:
        print(f"your choice = {user_choice}")
    elif user_choice == 4:
        print(f"your choice = {user_choice}")
    else:
        print("enter number between 1 to 5")
        continue

