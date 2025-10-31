title1 = input("Which book do you want to buy for the first one?\n")
price1 = float(input("How much does it cost?\n"))
quantity1 = int("How many of this book do you want?\n")

title2 = input("Which book do you want to buy for the second one?")
price2 = float(input("How much does it cost?\n"))
quantity2 = int("How many of this book do you want?\n")

title3 = input("Which book do you want to buy for the third one?")
price3 = float(input("How much does it cost?\n"))
quantity3 = int("How many of this book do you want?\n")

name = input("Enter your name: ")
is_faculty_staff = input("Is the customer faculty/staff? (yes/no): ") =="yes"
is_textbook_order = input("is this a textbook order? (yes/no): ") == "yes"
number_of_books = quantity1 + quantity2 + quantity3
subtotal = (price1 * quantity1)+(price2 * quantity2) + (price3 * quantity3) 
j = number_of_books  > 9
faculty_discount = subtotal * 0.2 * is_faculty_staff
textbook_discount = subtotal * 0.25 * is_textbook_order
bulkdiscount = number_of_books * 0.08 * j

main_discount = faculty_discount * (faculty_discount >=textbook_discount) + textbook_discount * (textbook_discount > faculty_discount)
small_order_fee = (number_of_books <3) * 10000