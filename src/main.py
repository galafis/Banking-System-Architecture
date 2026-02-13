from src.transactions.bank import Bank

def main():
    bank = Bank()

    print("\n--- Creating Accounts ---")
    account1 = bank.create_account("Alice Smith", 1000.00)
    account2 = bank.create_account("Bob Johnson", 500.00)
    account3 = bank.create_account("Charlie Brown")

    print("\n--- Account Balances ---")
    print(account1)
    print(account2)
    print(account3)

    print("\n--- Performing Transactions ---")
    account1.deposit(200.00)
    print(f"Alice's balance after deposit: ${account1.get_balance():.2f}")

    account2.withdraw(150.00)
    print(f"Bob's balance after withdrawal: ${account2.get_balance():.2f}")

    bank.transfer(account1.account_id, account2.account_id, 300.00)
    print(f"Alice's balance after transfer: ${account1.get_balance():.2f}")
    print(f"Bob's balance after transfer: ${account2.get_balance():.2f}")

    bank.transfer(account3.account_id, account1.account_id, 50.00) # Should fail

    print("\n--- Final Account Balances ---")
    print(account1)
    print(account2)
    print(account3)

if __name__ == "__main__":
    main()

