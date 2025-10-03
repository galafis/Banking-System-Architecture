import unittest
from src.accounts.account import Account
from src.transactions.bank import Bank

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("Test User", 1000.00)

    def test_deposit(self):
        self.assertTrue(self.account.deposit(200.00))
        self.assertEqual(self.account.get_balance(), 1200.00)
        self.assertFalse(self.account.deposit(-50.00))
        self.assertEqual(self.account.get_balance(), 1200.00)

    def test_withdraw(self):
        self.assertTrue(self.account.withdraw(150.00))
        self.assertEqual(self.account.get_balance(), 850.00)
        self.assertFalse(self.account.withdraw(1000.00)) # Insufficient funds
        self.assertEqual(self.account.get_balance(), 850.00)
        self.assertFalse(self.account.withdraw(-50.00))
        self.assertEqual(self.account.get_balance(), 850.00)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000.00)

    def test_str(self):
        self.assertIn("Account ID:", str(self.account))
        self.assertIn("Holder: Test User", str(self.account))
        self.assertIn("Balance: $1000.00", str(self.account))

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.account1 = self.bank.create_account("Alice", 1000.00)
        self.account2 = self.bank.create_account("Bob", 500.00)

    def test_create_account(self):
        account = self.bank.create_account("Charlie", 200.00)
        self.assertIsNotNone(account)
        self.assertIn(account.account_id, self.bank.accounts)
        self.assertEqual(account.account_holder, "Charlie")
        self.assertEqual(account.get_balance(), 200.00)

    def test_get_account(self):
        retrieved_account = self.bank.get_account(self.account1.account_id)
        self.assertEqual(retrieved_account.account_holder, "Alice")
        self.assertIsNone(self.bank.get_account("non_existent_id"))

    def test_transfer_success(self):
        self.assertTrue(self.bank.transfer(self.account1.account_id, self.account2.account_id, 300.00))
        self.assertEqual(self.account1.get_balance(), 700.00)
        self.assertEqual(self.account2.get_balance(), 800.00)

    def test_transfer_insufficient_funds(self):
        self.assertFalse(self.bank.transfer(self.account1.account_id, self.account2.account_id, 1500.00))
        self.assertEqual(self.account1.get_balance(), 1000.00)
        self.assertEqual(self.account2.get_balance(), 500.00)

    def test_transfer_invalid_account(self):
        self.assertFalse(self.bank.transfer("non_existent_id", self.account2.account_id, 100.00))
        self.assertFalse(self.bank.transfer(self.account1.account_id, "non_existent_id", 100.00))
        self.assertEqual(self.account1.get_balance(), 1000.00)
        self.assertEqual(self.account2.get_balance(), 500.00)

if __name__ == '__main__':
    unittest.main()

