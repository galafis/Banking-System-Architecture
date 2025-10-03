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

