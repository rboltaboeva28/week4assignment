name = input("What is your name? ")
gpa = float(input("Enter your GPA(0.0-4.0): "))
credit_hr = int(input("Enter your total credit hours: "))
is_eligible = gpa >= 3.5 and credit_hr >= 12
gpa_needed = (3.5 - gpa) * (gpa < 3.5)
credits_needed = (12 - credit_hr) * (credit_hr < 12)

print(f"Student's name: {name}, GPA: {gpa}, Total credit hours: {credit_hr}")
print(f"Eligible for Dean's list: {is_eligible}")
print(f"GPA points needed: {gpa_needed}")
print(f"Credits needed: {credits_needed}")
