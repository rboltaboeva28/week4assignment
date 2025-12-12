# def calculate_safe_average(data_list):
#     total = 0
#     count = 0
#     for item in data_list:
#         try:
#             number = float(item)
#             total += number
#             count += 1
#         except ValueError:
#             print(f"Skipping invalid data: {item}")
#     try:
#         average = total / count
#         return average
#     except ZeroDivisionError:
#         print("Warning: No valid numbers to average.")
#         return 0.0

# raw_data = [100, "missing", 95, 80, "N/A"]
# result = calculate_safe_average(raw_data)
# print(f"Average: {result}")




# def get_user_role(users_list, index, key):
#     try:    
#         user = users_list[index]
#         value = user[key]
#         return value
#     except IndexError:
#         return "Error: User ID out of range"
#     except KeyError as e:
#         return f"Error: The attribute {e} does not exist for this user."
#     except TypeError as e:
#         return f"Error: Indices must be integers. Details: {e}"

# users = [{"name": "Alice", "role": "admin"}, {"name": "Bob", "role": "user"}]
# print(get_user_role(users, 5, 'role'))   # Triggers IndexError
# print(get_user_role(users, 0, 'age'))    # Triggers KeyError





# def process_transaction(balance, amount):
#     print(f"Attempting to withdraw ${amount}")
#     try:    
#         amount_float = float(amount)
#         new_balance = balance - amount_float
#     except ValueError:
#         print("Error: Invalid amount entered.")
#         return balance
#     else:
#         print("Transaction approved.")
#         return new_balance
#     finally:
#         print("System: Saving transaction logs...")

# process_transaction(1000, 200)      # Triggers else and finally
# process_transaction(1000, "fifty"



# def clean_sensor_data(raw_readings):
#     valid_data = []
#     for reading in raw_readings:
#         try:
#             temp = float(reading)
#             if temp < -50.0 or temp > 60.0:
#                 raise ValueError(f"Out of range: {temp}")
#             valid_data.append(temp)
#         except ValueError as e:
#             print(f"Skipping entry '{reading}' : {e}")
#             continue
#     return valid_data

# data = ["23.5", "error", "105.0", "-10.0", "N/A", "40.5"]
# cleaned = clean_sensor_data(data)
# print(f"Cleaned Data: {cleaned}")