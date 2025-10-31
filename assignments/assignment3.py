print("\n=== Book Rental System ===")
print("Enter membership type: student, regular, or premium")
print("Type 'done' when finished selecting books\n")

total = 0.0
while True:
    memebership_type = input("Enter memebership type: ")
    if memebership_type == 'done':
        break

    elif memebership_type == "student":
        total+=2
        print("Price: $2.00")

    elif memebership_type == "regular":
        total+=4
        print("Price: $4.00")

    elif memebership_type == "premium":
        total+=6
        print("Price: $6.00")

    else:
        print("Invalid memebership type. Please enter student, regular, or premium")


    print(f"Current total: ${total:.2f}\n")


print("\n=== Rental Summary ===")
print(f"Subtotal: ${total:.2f}")
if total >= 15.00:
    total -= 2.50
    print("Bulk rental discount: -$2.50")
print(f"Final Total: ${total:.2f}")
print("Thank you for your rental!")