def withdraw_funds(account, amount):
    if not isinstance(amount, (int, float)) or amount <0:
        raise ValueError("Invalid amount")
    current_balance = account["balance"]
    new_balance = current_balance - amount
    limit = account["limit"]

    if new_balance >= 0:
        account["balance"] = new_balance
    if new_balance < limit:
        raise ValueError("Overdraft limit exceeded")
    if limit <= new_balance < 0:
        account["balance"] = new_balance
        raise UserWarning("Overdraft used")
    
my_account = {'balance': 50.0, 'limit': -100.0}
attempts = [40, 60, 200] 

for i in attempts:
    print(f"\nAttempting to withdraw ${i}...")
    try:
        withdraw_funds(my_account, i)
    except UserWarning as w:
        print(f"Alert: {w}. Balance: {my_account['balance']}")
    except ValueError as e:
        print(f"Transaction failed: {e}")
    else:
        print("Transaction successful")
    finally:
        print(f"Current balance: {my_account['balance']}")


# def withdraw_funds(account, amount):
#     curr_balance = account.get("balance")
#     limit = account.get("limit")
#     for attempt in attempts:
#         print(f"Attempting to withdraw ${attempt}...")
#         curr_balance -= attempt
#         try:
#             if limit < curr_balance < 0:
#                 raise UserWarning("Alert: Overdraft used")
#             elif limit > curr_balance:
#                 curr_balance += attempt
#                 raise ValueError("Transaction Failed: Overdraft limit exceeded")
#         except UserWarning as e:
#             print(f"{e}. Balance is {curr_balance}")
#             print("Transaction completed with warning.")
#         except ValueError as e:
#             print(e)
#         else:
#             print(f"Transaction successful.")
#         finally:
#             print(f"Current Balance: {curr_balance}\n")


# my_account = {'balance': 50.0, 'limit': -100.0}
# attempts = [40, 60, 200] 
# withdraw_funds(my_account, attempts)
