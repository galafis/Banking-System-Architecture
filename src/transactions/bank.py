from src.accounts.account import Account


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, initial_balance=0.0):
        account = Account(account_holder, initial_balance)
        self.accounts[account.account_id] = account
        return account

    def get_account(self, account_id):
        return self.accounts.get(account_id)

    def transfer(self, from_account_id, to_account_id, amount):
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)

        if not from_account or not to_account:
            return False
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

