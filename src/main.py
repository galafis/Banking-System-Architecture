import uuid

class Account:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_id = str(uuid.uuid4())
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account ID: {self.account_id}\nHolder: {self.account_holder}\nBalance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, initial_balance=0.0):
        account = Account(account_holder, initial_balance)
        self.accounts[account.account_id] = account
        print(f"Account created for {account_holder} with ID {account.account_id}")
        return account

    def get_account(self, account_id):
        return self.accounts.get(account_id)

    def transfer(self, from_account_id, to_account_id, amount):
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)

        if not from_account or not to_account:
            print("One or both accounts not found.")
            return False
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            print(f"Transferred ${amount:.2f} from {from_account.account_holder} to {to_account.account_holder}")
            return True
        print("Transfer failed: Insufficient funds or invalid amount.")
        return False

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
