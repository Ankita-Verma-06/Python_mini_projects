import os

def add_expense(filename="expense.txt"):
    category = input("Enter expense category (e.g. food, travel, health, rent): ").strip()

    try:
        amount = float(input("Enter the amount of expense: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
    except ValueError as e:
        print(e, "Please enter a valid positive number.")
        return

    description = input("Enter a description: ").strip()

    try:

        with open("expense.txt", "a") as file:
            file.write(f"{category},{amount},{description}\n")
        print("Expense data logged successfully!")
    except Exception as e:
        print("An unexpected error occurred while writing to the file.")

def summarize(filename="expense.txt"):
    try:
        with open("expense.txt", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No expense history found. Start by adding some expenses.")
        return

    if not lines:
        print("The expense file is empty.")
        return

    summary = {}
    total_expenses = 0.0

    print("\n--- Detailed Logs ---")
    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        category = parts[0]
        amount = float(parts[1])
        description = parts[2]

        print("Category:", category, "| Amount: Rs.", amount, "| Description:", description)

        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

        total_expenses = total_expenses + amount

    print("\n--- Breakdown By Category ---")
    for category in summary:
        print(category ,":", "Rs.",summary[category])

    print("Total Combined Spending: Rs.",total_expenses,"\n")

def main():

    filename = "expense.txt"

    while True:
        print("1. Add Expense")
        print("2. View & Summarize Expenses")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense(filename)
        elif choice == "2":
            summarize(filename)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.\n")

main()
