import csv
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Category', 'Description', 'Amount'])

    def add_expense(self, category, description, amount):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])
        print(f"Added: {description} (${amount}) to {category}")

    def view_summary(self):
        if not os.path.exists(self.filename):
            print("No expenses found.")
            return

        total = 0
        categories = {}
        
        print("\n--- Expense Summary ---")
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                amount = float(row['Amount'])
                total += amount
                cat = row['Category']
                categories[cat] = categories.get(cat, 0) + amount
                print(f"{row['Date']} | {row['Category']:<10} | {row['Description']:<15} | ${row['Amount']}")
        
        print("-" * 30)
        print(f"Total Spent: ${total:.2f}")
        for cat, amt in categories.items():
            print(f"{cat}: ${amt:.2f}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            cat = input("Category: ")
            desc = input("Description: ")
            try:
                amt = float(input("Amount: "))
                tracker.add_expense(cat, desc, amt)
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            tracker.view_summary()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
