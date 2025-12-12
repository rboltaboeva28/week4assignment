def withdraw_funds(account, amount):
    if not isinstance(amount, int) or amount <0:
        raise ValueError("Invalid amount")
    current_balance = account["balance"]
    new_balance = current_balance - amount
    if new_balance >= 0:
        account["balance"] = new_balance
    limit = account["limit"]
    if new_balance < 0 or new_balance >= limit:
        account["balance"] = new_balance
        raise UserWarning("Overdraft used")
    if new_balance < limit:
        raise ValueError("Overdraft limit exceeded")
    
my_account = {'balance': 50.0, 'limit': -100.0}
attempts = [40, 60, 200] 

for i in attempts:
    print(f"\nAttempting to withdraw ${i}...")
    try:
        withdraw_funds(my_account, i)
    except UserWarning:
        balance = my_account["balance"]
        print(f"Alert: Overdraft used. Balance: {balance}")
    except ValueError as e:
        print(f"Transaction failed.{e}")
    else:
        print("Transaction successful")
    finally:
        print(f"Current balance:{balance}")