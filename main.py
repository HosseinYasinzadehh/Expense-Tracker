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

def view_expenses(expenses):
    num = 1

    if len(expenses) == 0:
        print("nothing for view")
    else:
        for exp in expenses:
            print(f"{num}. {exp['description']} - ${exp['amount']}")
            num += 1

def show_total(expenses):
    total = 0

    for exp in expenses:
        total += exp["amount"]

    return total

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
        view_expenses(expenses)
    elif user_choice == 3:
        total = show_total(expenses)
        print(f"total = ${total}")
    elif user_choice == 4:
        print(f"your choice = {user_choice}")
    else:
        print("enter number between 1 to 5")
        continue

