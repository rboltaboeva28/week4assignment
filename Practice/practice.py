#this is me first Python program
# print("Hello, Risolat!")
# print("I'm glad to meet you")



# full_name = "Risolat Boltaboyeva"
# age = 25
# is_student = True
# print(f"I am {full_name}")
# print(f"I am {age} years old")
# print(f"Are you a student?: {is_student}")
# if is_student:
#     print("You are a astudent")
# else:
#     print("You are NOT a student")



# apples = 9
# apples %= 5
# print(apples)



# name = "Risolat"
# age = 17
# gpa = 4
# is_student =  True

# gpa = int(gpa)
# print(gpa)


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}")
# print(f"You are {age + 1} years old")



# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult")
# elif age < 0 :
#     print("You haven't been born yet")
# else:
#     print("You are a child")



# name = input("\nWhat is the outlaw's name?\n")
# alias = input("What is his known alias?(e.g., The Ghost Rider)\n")
# crime = input("What kind of crime did he commit?(e.g., Train Robbery)\n")
# reward = input("How much are you willing to give to find him?(e.g., $5000)\n")
# location = input("Where was he last seen?\n")

# print("\n****************************************")
# print("      WANTED: DEAD OR ALIVE      ")
# print("****************************************\n")
# print(f"Name:     {name}")
# print(f"Alias:    {alias}")
# print(f"\nWanted For: {crime}")
# print(f"Last Seen:  {location}")
# print("\n----------------------------------------")
# print(f"REWARD: {reward}")
# print("----------------------------------------")
# print(f"Issued by: The Sheriff's Office of {location}")
# print("****************************************")


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz") 
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
     



# print("--- Fibonacci Sequence Generator ---")
# num = int(input("How many Fibonacci numbers would you like to generate? "))

# a = 0
# b = 1

# for i in range (num):
#     print(a, end=" ")
#     a ,b = b, a + b


# print("--- Triangle Pattern Printer ---")
# height = int(input("Enter the desired height of the triangle: "))

# for i in range ( 1, height + 1):
#     for j in range(height - i):
#         print(" ", end=" ")
#     for k in range (2 * i - 1):
#         print("*", end=" ")
    
#     print()




# print("--- Running Total Calculator ---\nEnter numbers to add them up. Type 'done' to see the total.")
# total = 0.0
# while True:
#     num = (input("Enter a number or 'done': "))

#     if num == 'done':
#         break
#     else:
#         num = float(num)
#         total += num
#         print(f"Current total: {total}")


# print("\n--- Final Calculation ---")
# print(f"The final sum of all numbers is: {total}")

# import time
# for i in range(10,0, -1):
#         print(i)
#         time.sleep(1)
# print("Happy New Year!")



# print("\n=== Car Wash Service Calculator ===")
# print("Enter service package: basic, deluxe, or premium")
# print("Type 'done' when finished selecting services")



# total = 0
# while True:
#     package = input("\nEnter service package: ")
#     if package == 'done':
#         break
#     elif package == 'basic':
#         print("Price: $10.00")
#         total += 10
#     elif package == 'premium':
#         print("Price: $25.00")
#         total += 25
#     elif package == 'deluxe':
#         print("Price: $17.00")
#         total += 17
#     else:
#         print("Invalid package type. Please enter basic, deluxe, or premium.")

#     print(f"Current total: {total:.2f}")

# print("\n=== Service Summary ===")
# print(f"Subtotal: {total:.2f}")
# if total > 44:
#     total -= 6
#     print(f"Membership Savings: -$6.00")
# print(f"Final Total: ${total:.2f}")
# print("Thank you for choosing our service")



# name = input("What's your name? ")
# print(f"Hello,",name)

# for i in range(2):
#     for j in range(3):
#         print(f"{i},{j}")

# age = input("Enter your age: ")
# print(age + 5)
  

# def mystery(n):
#     if n <= 1:
#         return n
#     return mystery(n-1) + mystery(n-2)
# print(mystery(4))

# print("Hi" * 3)


# lst = [10, 20, 30]
# for x in lst:
#     x += 1
# print(lst)


# nums = [1, 2, 3]
# nums2 = nums
# nums2[0] = 99
# print(nums)


# nums = [10, 15, 20]
# for i in range(len(nums)):
#     nums[i] += 5
# print(nums)


# data = [5, 10, 15, 20]
# print(data[::2])



# age1 = input("Enter your name: ")
# age2  = input("Enter your name: ")
# print(age1 + age2)

# def greet(name):
#     name = input("What's your name? ")
#     print(f"Hello, {name}")
# raw_data = "one, two, three"
# parts = raw_data.split(",")
# cleaned_data = raw_data.strip().lower()
# joined_data = "-".join(parts)
# error_line = raw_data.split(",").lower()

line = "item1,,,item2"
parts = line.split(",")
print((parts))