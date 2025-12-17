data = """Lunch,12.50
Coffee,5.00
Office Supplies,23.75
Taxi,10.00
Coffee,8.25
Dinner,50.00"""

with open("expenses.txt", "w") as f:
    f.write(data)


total = 0
counter = 0
with open("expenses.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        cost = float(parts[1])
        total += cost
        counter += 1
        avg = total / counter

print("--- Expense Report ---")
print(f"Total Transactions: {counter}")
print(f"Total Spent: ${total:.2f}")
print(f"Average Expense: ${avg}")