"""A beginner-friendly command-line personal expense tracker."""

import csv
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.csv")
FIELDS = ["date", "description", "category", "amount"]


def load_expenses():
    """Read expenses from the CSV file. Return an empty list if it doesn't exist."""
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_expense(expense):
    """Append one expense to the CSV file, writing headers when needed."""
    file_exists = DATA_FILE.exists()

    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if not file_exists or DATA_FILE.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(expense)


def ask_amount():
    """Ask for a positive amount and return it as a two-decimal string."""
    while True:
        raw_amount = input("Amount (e.g. 2500.50): ").strip().replace(",", "")
        try:
            amount = Decimal(raw_amount)
            if not amount.is_finite() or amount <= 0:
                raise InvalidOperation
            return f"{amount:.2f}"
        except (InvalidOperation, ValueError):
            print("Please enter a valid amount greater than zero.")


def add_expense():
    print("\n--- Add an expense ---")
    description = input("Description: ").strip()
    while not description:
        print("Description cannot be empty.")
        description = input("Description: ").strip()

    category = input("Category (e.g. Food, Transport, Bills): ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Category: ").strip()

    raw_date = input(f"Date [press Enter for {date.today()}] (YYYY-MM-DD): ").strip()
    if not raw_date:
        expense_date = date.today().isoformat()
    else:
        try:
            expense_date = datetime.strptime(raw_date, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("Invalid date. Using today's date instead.")
            expense_date = date.today().isoformat()

    amount = ask_amount()
    save_expense({
        "date": expense_date,
        "description": description,
        "category": category.title(),
        "amount": amount,
    })
    print("Expense saved successfully!")


def list_expenses():
    expenses = load_expenses()
    print("\n--- Your expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'DATE':<12} {'DESCRIPTION':<25} {'CATEGORY':<16} {'AMOUNT':>12}")
    print("-" * 68)
    for item in sorted(expenses, key=lambda row: row["date"], reverse=True):
        print(
            f"{item['date']:<12} {item['description'][:24]:<25} "
            f"{item['category'][:15]:<16} {Decimal(item['amount']):>12,.2f}"
        )


def show_summary():
    expenses = load_expenses()
    print("\n--- Spending summary ---")
    if not expenses:
        print("No expenses to summarize yet.")
        return

    totals = {}
    overall = Decimal("0.00")
    for item in expenses:
        amount = Decimal(item["amount"])
        category = item["category"]
        totals[category] = totals.get(category, Decimal("0.00")) + amount
        overall += amount

    print(f"Total spending: {overall:,.2f}")
    print("\nBy category:")
    for category, total in sorted(totals.items(), key=lambda pair: pair[1], reverse=True):
        print(f"  {category:<18} {total:>12,.2f}")


def main():
    print("================================")
    print("      PERSONAL EXPENSE TRACKER")
    print("================================")

    while True:
        print("\n1. Add an expense")
        print("2. View all expenses")
        print("3. View spending summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye. Keep tracking your spending!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
