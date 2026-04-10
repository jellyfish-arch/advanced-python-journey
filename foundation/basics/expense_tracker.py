expenses = []

while True:
    amount = input("Enter expense (or 'q' to quit): ")
    if amount == 'q':
        break
    expenses.append(float(amount))

print("Total:", sum(expenses))
print("Average:", sum(expenses) / len(expenses) if expenses else 0)
