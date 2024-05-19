# Budget Tracker

## Video Demo

[Video here](https://youtu.be/jYwk2mChIRw)

## Description

The Budget Tracker is a simple yet powerful Python script designed to help users manage their finances effectively. It allows users to keep track of their income and expenses, providing a clear overview of their overall budget. Whether you're looking to save money, manage your spending, or just keep track of your financial health, the Budget Tracker provides a straightforward and efficient way to do so.

The script features an intuitive interface that prompts users for their financial transactions and stores this data in a JSON file. This ensures that all your financial information is saved between sessions, providing persistent data storage.

## Features

- **Deposit Money:** Easily add money to your budget. Specify the amount and type of income (e.g., salary, interest, dividends).
- **Withdraw Money:** Record your expenses by withdrawing money from your budget. Specify the amount and type of expense (e.g., housing, groceries, transportation).
- **View Current Balance:** Check your overall budget at any time to see your current financial status.
- **Detailed Breakdown:** View detailed breakdowns of your income and expenses to understand where your money is coming from and where it's going.
- **Data persistence:** All financial data is saved in a JSON file, ensuring your information is preserved across sessions.

## Installation

1. Clone the repository:

```
git clone https://github.com/gerynash13/Budget-Tracker.git
```

2. Navigate to the project directory:

```
cd budget-tracker
```

> [!NOTE]
> Since only built-in modules are being used in this file, there's no need to install dependencies.

## Usage

1. Run the script:

```
python budget-tracker.py
```

2. Follow the on-screen instructions to perform operations such as depositing money, withdrawing it for expenses, and check the overall balance.

3. To exit the program, select the Exit option in the main menu.

## Example

1. **Deposit Money:**

    - The script will prompt you the amount you wish to deposit and the type of income. For example, you can deposit 100€ as salary:
    ```
    Please input the amount that you want to deposit. (Type 'Back' to return to the main menu.):
    100
    Please choose the type of income:
    - Salary
    - Interest or Dividends
    - Benefits
    - Miscellaneous
    salary
    ```

2. **Withdraw Money:**

    - The script will prompt you the amount you wish to withdraw and the type of expense. For example, you can withdraw 50€ for groceries:
    ```
    Please input the amount that you want to withdraw: (Type 'Back' to return to the main menu):
    50
    Please choose the type of expense:
    - Housing
    - Transportation
    - Bills
    - Groceries
    - Education
    - Health
    - Personal Upkeep
    - Travel Expenses
    - Subscriptions
    - Insurance
    - Entertainment
    - Debt
    groceries
    ```

3. **View Balance:**

    - The script will provide options to view your current balance, detailed income and expenses. For example:
    ```
    Please type the operation you wish to perform:
    - Check Balance
    - View Income
    - View Expenses
    (Type 'Back' to return to the main menu)
    check balance

    Overall Budget: 50€
    ```

## Data Storage

The script stores data in a JSON file named `budget_tracker_data.json`. This file contains information about the budget, income, and expenses. Data is loaded from this file when the script starts, and it is saved to this file whenever there are changes. Here's an example of what the JSON file might look like:

```
{
    "budget": "50.00",
    "income": {
        "salary": "100.00"
    },
    "expenses": {
        "groceries": "50.00"
    }
}
```

Whenever you deposit money or record an expense, the script updates this file to ensure that your data is always up-to-date. When you restart the script, it loads the data from the file, allowing you to continue where you left off.

## Contributing

Contibutions are welcome!

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). You are free to use, modify and distribute this software in accordance with the license terms.

## Acknowledgements

- Thanks to the Python community for providing excellent resources and libraries that made this project possible.
- Inspiration for this project came from a need to simplify personal financial management.
