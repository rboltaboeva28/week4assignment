def perform_atomic_transfer(accounts, sender, receiver, amount):
    if sender not in accounts:
        raise KeyError(f"Sender {sender} not found")
    if accounts[sender] < amount:
        raise ValueError(f"Sender '{sender}' has insufficient funds")
    accounts[sender] -= amount
    print(f"-> Withdrew ${amount} from {sender}.")
    try:
        accounts[receiver] += amount
        print(f"-> Deposited ${amount} to {receiver}.")
        return True
    except KeyError:
        print(f"   [!] Transaction failed: \"Receiver '{receiver}' not found.\"")
        print(f"   [!] Rolling back: Refunding ${amount} to {sender}.")
        accounts[sender] += amount
        raise KeyError(f"Receiver '{receiver}' not found.")

def main():
    bank_db = {"Alice": 100.0, "Bob": 50.0}
    
    print("--- Test 1: Successful Transfer ---")
    try:
        perform_atomic_transfer(bank_db, "Alice", "Bob", 30.0)
        print("Transfer Complete.")
    except Exception as e:
        print(f"Main Error Handler: {e}")
    print(f"Current State: {bank_db}")
    
    print("\n--- Test 2: Failed Transfer (Bad Receiver) ---")
    try:
        perform_atomic_transfer(bank_db, "Alice", "Charlie", 20.0)
        print("Transfer Complete.")
    except Exception as e:
        print(f"Main Error Handler: {e}")
    print(f"Current State: {bank_db}")
    
    print("\n--- Test 3: Insufficient Funds ---")
    try:
        perform_atomic_transfer(bank_db, "Bob", "Alice", 100.0)  
        print("Transfer Complete.")
    except Exception as e:
        print(f"Main Error Handler: {e}")

if __name__ == "__main__":
    main()