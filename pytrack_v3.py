import json
from datetime import date

FILE_NAME = "expenses.json"
INCOME_FILE = "income.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def load_income():
    try:
        with open(INCOME_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0


def save_income():
    with open(INCOME_FILE, "w") as file:
        json.dump(income, file)


expenses = load_expenses()
income = load_income()


def add_income():
    global income

    try:
        amount = float(input("Enter income amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    income += amount
    save_income()

    print("Income added successfully!")


def add_expense():
    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
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


def show_balance():
    total = sum(expense["amount"] for expense in expenses)
    balance = income - total

    print("\n----- Balance Summary -----")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{total}")
    print(f"Balance: ₹{balance}")


def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    show_expenses()

    try:
        number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid number!")
        return

    if number < 1 or number > len(expenses):
        print("Invalid expense number!")
        return

    deleted = expenses.pop(number - 1)
    save_expenses()

    print(f"Expense '{deleted['category']}' deleted successfully!")


def search_category():
    category = input("Enter category to search: ").lower()
    found = False

    print("\n----- Search Results -----")

    for expense in expenses:
        if expense["category"].lower() == category:
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print(f"Amount: ₹{expense['amount']}")
            print(f"Note: {expense['note']}")
            print("------------------------")
            found = True

    if not found:
        print("No expenses found for this category.")


def category_summary():
    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    print("\n----- Category Summary -----")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")


def main():
    while True:
        print("\n===== PyTrack V3 =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Expenses")
        print("4. Total Expense")
        print("5. Show Balance")
        print("6. Delete Expense")
        print("7. Search by Category")
        print("8. Category Summary")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_expenses()
        elif choice == "4":
            total_expense()
        elif choice == "5":
            show_balance()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            search_category()
        elif choice == "8":
            category_summary()
        elif choice == "9":
            print("Thank you for using PyTrack V3!")
            break
        else:
            print("Invalid choice. Please try again.")


main()