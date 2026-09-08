expenses = []


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    expense = {
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)
    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- All Expenses -----")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category: {expense['category']}")
        print(f"   Amount: ₹{expense['amount']}")
        print(f"   Note: {expense['note']}")
        print("------------------------")


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expense: ₹{total}")


def main():
    while True:
        print("\n===== PyTrack =====")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Thank you for using PyTrack!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
