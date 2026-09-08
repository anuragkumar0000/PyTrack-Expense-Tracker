import json
from datetime import date

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()


def add_expense():
    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    note = input("Enter note: ")

    expense = {
        "date": str(date.today()),
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def show_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- All Expenses -----")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Date: {expense['date']}")
        print(f"   Category: {expense['category']}")
        print(f"   Amount: ₹{expense['amount']}")
        print(f"   Note: {expense['note']}")
        print("------------------------")


def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expense: ₹{total}")


def main():
    while True:
        print("\n===== PyTrack V2 =====")
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
