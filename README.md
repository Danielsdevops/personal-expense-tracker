# Personal Expense Tracker

A simple command-line application built with Python. It helps users record daily expenses, view transaction history, and understand spending by category.

## Features

- Add expenses with a description, category, date, and amount.
- View saved expenses, newest first.
- See total spending and a breakdown by category.
- Store records locally in a CSV file.
- Validate amounts and required fields.
- Includes unit tests using Python's built-in `unittest` framework.

## Technologies

- Python 3
- CSV file handling
- `datetime` and `decimal`
- Unit testing with `unittest`

## Requirements

- Python 3.9 or newer
- No third-party packages required

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python3 main.py
   ```

4. Follow the on-screen menu. Your expenses will be saved in `expenses.csv` in the project folder.

## How to run the tests

```bash
python3 -m unittest -v
```

## Example

```text
================================
      PERSONAL EXPENSE TRACKER
================================

1. Add an expense
2. View all expenses
3. View spending summary
4. Exit
Choose an option (1-4): 3

--- Spending summary ---
Total spending: 5,500.00

By category:
  Food                    3,000.00
  Transport               2,500.00
```

*The example values above are illustrative.*

## Project structure

```text
personal-expense-tracker/
├── main.py
├── test_main.py
├── README.md
└── .gitignore
```

## Future improvements

- Add monthly reports.
- Export reports to Excel.
- Add income tracking and budgets.
- Build a graphical interface or web dashboard.
- Add charts to visualize spending.

## Author

Your Name

Replace `Your Name` with your name before publishing.
