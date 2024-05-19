# Budget tracker
# Assumptions: Currency is €, decimal separator is the dot.
import re
import sys
from decimal import Decimal
import json

# Initialize budget
budget = Decimal("0")

inc_dict = {}
inc_type = ["salary", "interest or dividends", "benefits", "miscellaneous"]

exp_dict = {}
exp_type = [
    "housing",
    "transportation",
    "bills",
    "groceries",
    "education",
    "health",
    "personal outkeep",
    "travel expenses",
    "subscriptions",
    "insurance",
    "entertainment",
    "debt",
]


# Save the data to a JSON file
def save_data():
    data = {
        "budget": str(budget),
        "income": {k: str(v) for k, v in inc_dict.items()},
        "expenses": {k: str(v) for k, v in exp_dict.items()},
    }

    with open("budget_tracker_data.json", "w") as file:
        json.dump(data, file)


# Load the data from the JSON file:
def load_data():
    try:
        with open("budget_tracker_data.json", "r") as file:
            data = json.load(file)
            global budget
            budget = Decimal(data["budget"])
            global inc_dict
            inc_dict = {k: Decimal(v) for k, v in data["income"].items()}
            global exp_dict
            exp_dict = {k: Decimal(v) for k, v in data["expenses"].items()}
    except FileNotFoundError:
        # If the file doesn't exist, we pass so it starts with 0
        pass


def main():
    # Ask user for operation (what do you wanna do, then if statements)
    while True:
        op = (
            input(
                "Which operation would you like to perform?\n- Deposit\n- Expenses\n- Balance\n- Exit\n"
            )
            .lower()
            .strip()
        )

        if "deposit" in op:
            dep_amount = input(
                "\nPlease input the amount that you want to deposit. (Type 'Back' to return to the main menu.):\n"
            ).lower()
            if "back" in dep_amount:
                print()
                continue
            dep_type = (
                input(
                    "\nPlease choose the type of income:\n- Salary\n- Interest or Dividends\n- Benefits\n- Miscellaneous\n\n"
                )
                .lower()
                .lstrip()
                .rstrip()
            )
            deposit(dep_amount, dep_type)
            continue

        elif "expenses" in op:
            exp_amount = input(
                "\nPlease input the amount that you want to withdraw: (Type 'Back' to return to the main menu):\n"
            ).lower()
            if "back" in exp_amount:
                print()
                continue
            exp_type = (
                input(
                    "\nPlease choose the type of expense:\n- Housing\n- Transportation\n- Bills\n- Groceries\n- Education\n- Health\n- Personal Upkeep\n- Travel Expenses\n- Subscriptions\n- Insurance\n- Entertainment\n- Debt\n"
                )
                .lower()
                .lstrip()
                .rstrip()
            )
            expenses(exp_amount, exp_type)
            continue

        elif "balance" in op:
            balance(op)
            continue

        elif "exit" in op:
            sys.exit("\nThank you for using our services.\n")

        else:
            print("\nPlease input a valid operation.\n")


# Function for deposits (amount, type)
def deposit(dep_amount, dep_type):
    global budget

    amount = dep_amount.lower()
    income_type = dep_type.lower()

    if amount == "back":
        return budget

    pattern = r"\b\d+(\.\d{1,2})?\b\s*€?"
    if matches := re.search(pattern, amount):
        amount_str = matches.group()
        # Convert the amount string to a Decimal object directly
        amount = Decimal(amount_str.replace(",", "").replace("€", ""))
        budget += amount  # Update budget
        print("\nThe amount has been deposited.\n")

        if income_type in inc_type:
            inc_dict[income_type] = amount
            print("The operation was successful.\n")
        else:
            print("Please input a correct type of income.\n")
    else:
        print("Input is not a correct amount.")

    return budget


# Function for expenses (amount, type)
def expenses(exp_amount, exp_type):
    global budget

    amount = exp_amount.lower()
    expense_type = exp_type.lower()

    if amount == "back":
        return budget

    pattern = r"\b\d+(\.\d{1,2})?\b\s*€?"
    if matches := re.search(pattern, amount):
        amount_str = matches.group()
        # Convert the amount string to a Decimal object directly
        amount = Decimal(amount_str.replace(",", "").replace("€", ""))
        if budget < amount:
            print("\nOperation unsuccessful: Not enough budget for withdrawal.")
            return budget
        else:
            budget -= amount  # Update budget
            if expense_type in exp_type:
                exp_dict[expense_type] = amount
                print("\nThe operation was successful.\n")
            else:
                print("Please input a correct type of expense.\n")
                return budget
    else:
        print("\nPlease input a correct amount.\n")

    return budget


# Function to check balance and display the dicts
def balance(op):
    global budget

    while True:
        op = input(
            "\nPlease type the operation you wish to perform:\n- Check Balance\n- View Income\n- View Expenses\n(Type 'Back' to return to the main menu)\n"
        ).lower()
        if "back" in op:
            print()
            break
        elif "check balance" in op:
            print("\nOverall Budget:", budget, "€\n")
            return budget
        elif "view income" in op:
            print()
            for key, value in inc_dict.items():
                print(f"{key.capitalize()}: {value}€")
            print(f"\nOverall Budget: {budget}€\n")
            return budget
        elif "view expenses" in op:
            print()
            for key, value in exp_dict.items():
                print(f"{key.capitalize()}: {value}€")
            print(f"\nOverall Budget: {budget}€\n")
            return budget
        else:
            print("\nInvalid operation.\n")


if __name__ == "__main__":
    main()
