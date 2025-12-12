print("=== Arcade Game Center Calculator ===")
print("Enter game type: classic, modern, or premium")
print("Type 'done' when finished playing")

total = 0.0
while True:
    type = input("Enter game type: ")
    if type == "done":
        break
    elif type == "classic":
        print("Price: $0.50")
        total += 0.50
    elif type == "modern":
        print("Price: $1.50")
        total += 1.50
    elif type == "premium":
        print("Price: $2.50")
        total += 2.50
    else:
        print("Invalid game type. Please enter classic, modern, or premium.")
    print(f"Current total: ${total:.2f}")


print("=== Game Summary ===")
print(f"Subtotal: ${total:.2f}")
if total >= 10:
    print(f"Token Bonus Credit: -$1.50")
    final_total = total - 1.50
    print(f"Final Total: ${final_total:.2f}")
print("Thank you for playing!")