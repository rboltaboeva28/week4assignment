# print("\n--- T-Minus Countdown ----") 
# counter  = 5
# while counter >0:
#     print(f"{counter}...")
#     counter -=1

# print("Blast off!")


# print("\n--- Exploring the range() function ---")

# print("Printing numbers from 0 to 4:")
# for i in range(5):
#     print(f"Current number is {i}")

# print("\nPrinting numbers from 1 to 5:")
# for number in range(1,6):
#     print(f"The number is {number}")

# print("\nPrinting even numbers from 2 to 10:")
# for num in range(2,11,2):
#     print(f"Even number: {num}")

# print("\n--- Finding the first number divisible by 7(using break) ---")
# for number in range(10,21):
#     print(f"Checking {number}...")
#     if number % 7 == 0:
#         print(f"Found it! The first number divisible by 7 is {number}.")
#         break


# print("\n--- Printing only even numbers (using continue) ---")
# for number in range(1,11):
#     if not number % 2 == 0:
#         continue
#     print(f"Even number: {number}")


# print("\n ---Drawing a 4x5 Rectangle ---")
# height = 4
# width = 5

# for row_num in range(height):
#     for col_num in range(width):
#         print("* ", end="")

#     print()    



# secret_number = 7
# max_attempts = 5

# print(f"\nI'm thinking of a number. You have {max_attempts} attempts to guess it.")


# for num in range(1, max_attempts + 1):
#     print(f"\n--- Attempt {num} ---")
#     guess = int(input("Enter your guess: "))

#     if guess == secret_number:
#         print(f"Congratulations! You found it.The number was {secret_number}")
#         break

#     elif guess > secret_number:
#      print("Too high! Try a lower number.")


    # else:
    #     print("Too low! Try a higher number.")

    # if num == max_attempts:
    #    print(f"\nSorry, you've run out of attempts. The secret nymber was {secret_number}.")





    

# print("\n=== Museum Admission Calculator ===")
# print("Enter exhibit type: general, special, or vip")
# print("Type 'done' when finished selecting exhibits")

# total = 0.0
# while True:
#     exhibit_type = input("\nEnter exhibit type: ")
#     if exhibit_type == "general":
#         print("Price: $9.00")
#         total += 9

#     elif exhibit_type == "special":
#         print("Price: $14.00")
#         total += 14

#     elif exhibit_type == "vip":
#         print("Price: $20.00")
#         total += 20

#     elif exhibit_type == "done":
#         break 


#     else:
#         print("Invalid exhibition type. Please enter general, special, or vip.")

#     print(f"Current total: ${total:.2f}")

# print("\n=== Admission Summary ===")
# print(f"Subtotal: ${total:.2f}")
# if total >= 55:
#     total -= 8
#     print("Group Visit Discount: -$8.00")
# print(f"Final total: ${total:.2f}")
# print("Thank you for visiting!")



# print("\n--- Fibonacci Sequence Generator ---")
# n = int(input("How many Fibonacci numbers would you like to generate? "))

# a = 0
# b = 1

# for i in range (n):
#     print(a, end=" ")
#     a, b = b,  a + b




# score1 = 85
# score2 = 92
# score3 = 78

# # Calculate statistics using built-in functions
# highest = max(score1, score2, score3)
# lowest = min(score1, score2, score3)
# average = (score1 + score2 + score3) / 3
# rounded_average = round(average, 2)
# score_range = abs(highest - lowest)

# # Weighted calculation using pow
# weighted1 = pow(score1, 2)
# weighted2 = pow(score2, 2)
# weighted3 = pow(score3, 2)
# total_weighted = weighted1 + weighted2 + weighted3

# print("Grade Analysis:")
# print(f"Scores: {score1}, {score2}, {score3}")
# print(f"Highest: {highest}")
# print(f"Lowest: {lowest}")
# print(f"Average: {rounded_average}")
# print(f"Range: {score_range}")
# print(f"Weighted total (squared): {total_weighted}")



# def count_uppercase(password):
#     count = 0
#     for char in password:
#         if char >= 'A' and char <= 'Z':
#             count += 1
#     return count


# def count_lowercase(password):
#     count = 0
#     for char in password:
#         if char >= 'a' and char <= 'z':
#             count += 1
#     return count


# def count_digits(password):
#     count = 0
#     for char in password:
#         if char >= '0' and char <= '9':
#             count += 1
#     return count


# def has_special_char(password):
#     special_chars =" !@#$%^&*"
#     for char in password:
#         if char in special_chars:
#             return True
#     return False


# def calculate_strength(password):
#     score = 0

#     if count_uppercase(password) >= 2:
#         score += 1

#     if count_lowercase(password) >= 2:
#         score += 1

#     if count_digits(password) >= 2:
#         score += 1

#     if has_special_char(password):
#         score += 1

#     if len(password)>= 8:
#         score += 1

#     return score

# def get_strength_label(score):
#     if score <= 1:
#         return "Very Weak"
    
#     elif score == 2:
#         return "Weak"
    
#     elif score == 3:
#         return "Medium"
    
#     elif score == 4:
#         return "Strong"
    
#     else:
#         return "Very Strong"
    


# print("\nPassword Strength Analysis")
# print("-"*40)


# password1 = "abc"
# score1 = calculate_strength(password1)
# label1 = get_strength_label(score1)
# print(f"Password: {password1}")
# print(f"   Uppercase: {count_uppercase(password1)}, Lowercase: {count_lowercase(password1)}, Digits: {count_digits(password1)}")
# print(f"   Strength Score: {score1}/5")
# print(f"   Strength Label: {label1}\n")


# password2 = "Hello"
# score2 = calculate_strength(password2)
# label2 = get_strength_label(score2)
# print(f"Password: {password2}")
# print(f"   Uppercase: {count_uppercase(password2)}, Lowercase: {count_lowercase(password2)}, Digits: {count_digits(password2)}")
# print(f"   Strength Score: {score2}/5")
# print(f"   Strength Label: {label2}\n")


# password3 = "Hello123"
# score3 = calculate_strength(password3)
# label3 = get_strength_label(score3)
# print(f"Password: {password3}")
# print(f"   Uppercase: {count_uppercase(password3)}, Lowercase: {count_lowercase(password3)}, Digits: {count_digits(password3)}")
# print(f"   Strength Score: {score3}/5")
# print(f"   Strength Label: {label3}\n")


# password4 = "Pass@123"
# score4 = calculate_strength(password4)
# label4 = get_strength_label(score4)
# print(f"Password: {password4}")
# print(f"   Uppercase: {count_uppercase(password4)}, Lowercase: {count_lowercase(password4)}, Digits: {count_digits(password4)}")
# print(f"   Strength Score: {score4}/5")
# print(f"   Strength Label: {label4}\n")


# password5 = "MyP@ssW0rd1"
# score5 = calculate_strength(password5)
# label5 = get_strength_label(score5)
# print(f"Password: {password5}")
# print(f"   Uppercase: {count_uppercase(password5)}, Lowercase: {count_lowercase(password5)}, Digits: {count_digits(password5)}")
# print(f"   Strength Score: {score5}/5")
# print(f"   Strength Label: {label5}\n")


