print("=== University Bookstore Checkout ===")


name = input("Customer name: ")

is_faculty_staff = input("Is the customer faculty/staff? (yes/no): ") == "yes"
is_textbook_order = input("Is this a textbook order? (yes/no): ") == "yes"

title1 = input("Which book do you want to buy for the first one?\n")
price1 = float(input("How much does it cost?\n"))
quantity1   = int(input("How many of this book do you want?\n"))

title2 = input("Which book do you want to buy for the second one?\n")
price2 = float(input("How much does it cost?\n"))
quantity2   = int(input("How many of this book do you want?\n"))

title3 = input("Which book do you want to buy for the third one?\n")
price3 = float(input("How much does it cost?\n"))
quantity3   = int(input("How many of this book do you want?\n"))


line1 = price1 * quantity1
line2 = price2 * quantity2
line3 = price3 * quantity3

subtotal = line1 + line2 + line3
number_of_books = quantity1 + quantity2 + quantity3


faculty_discount     = 0.20 * subtotal * is_faculty_staff
textbook_discount    = 0.25 * subtotal * is_textbook_order


main_discount = (faculty_discount * (faculty_discount >= textbook_discount)
               + textbook_discount * (textbook_discount > faculty_discount))

bulk_eligible = (number_of_books >= 10)
bulk_discount = 0.08 * subtotal * bulk_eligible

total_discounts = main_discount + bulk_discount


small_order_fee = 10000 * (number_of_books < 3) 


subtotal_after_discounts = subtotal - total_discounts + small_order_fee


tax = 0.05 * subtotal_after_discounts * (is_textbook_order == False)


total_before_tax = subtotal_after_discounts  
shipping = 20000 * (total_before_tax < 200000)


final_total = total_before_tax + tax + shipping


faculty_eligible   = is_faculty_staff
textbook_eligible  = is_textbook_order
bulk_eligible_flag = bulk_eligible
fee_applied        = (small_order_fee > 0)
tax_exempt         = is_textbook_order 
free_shipping      = (shipping == 0)

applied_faculty   = (faculty_discount >= textbook_discount) and (faculty_discount > 0)
applied_textbook  = (textbook_discount > faculty_discount)
applied_label = (applied_faculty and "Faculty") or (applied_textbook and "Textbook") or "None"


print("\n=== ITEMIZED RECEIPT ===")
print(f"Customer: {name}")
print(f"Faculty/Staff: {faculty_eligible}  | Textbook order: {textbook_eligible}")
print("\nItems:")
print(f"  1) {title1} - {quantity1} × {price1:.2f} = {line1:.2f}")
print(f"  2) {title2} - {quantity2} × {price2:.2f} = {line2:.2f}")
print(f"  3) {title3} - {quantity3} × {price3:.2f} = {line3:.2f}")

print(f"\nSubtotal before discounts: {subtotal:.2f}")

print("\nDiscount eligibility and amounts:")
print(f"  Faculty eligible: {faculty_eligible}  | amount: {faculty_discount:.2f}")
print(f"  Textbook eligible: {textbook_eligible} | amount: {textbook_discount:.2f}")
print(f"  Main discount applied: {applied_label} | amount: {main_discount:.2f}")
print(f"  Bulk eligible (>=10 books): {bulk_eligible_flag} | amount: {bulk_discount:.2f}")

print(f"\nTotal discounts: {total_discounts:.2f}")

print(f"\nSmall order fee applied (<3 books): {fee_applied} | fee: {small_order_fee:.2f}")
print(f"Subtotal after discounts and fees: {subtotal_after_discounts:.2f}")

print(f"\nTax applied (5% if NOT textbook): {not tax_exempt} | tax: {tax:.2f}")
print(f"Shipping (free if total_before_tax >= 200000): {free_shipping} | shipping: {shipping:.2f}")

print(f"\nFINAL TOTAL: {final_total:.2f}")

net_savings = total_discounts - (small_order_fee + shipping + tax)
print(f"Net savings (discounts - fees - tax): {net_savings:.2f}")
