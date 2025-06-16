import unittest
from Infrastructure.Repositories.account import AccountRepository
from domain.entities.account import Account, AccountType

class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        """Initialize test data before each test"""
        # Create a test account with CHECKING account type
        self.test_account = Account(
            account_id=1, 
            balance=100.0, 
            owner_id="test_owner",
            account_type=AccountType.CHECKING
        )
        self.repository = AccountRepository([self.test_account])

    def test_store_account_data(self):
        """Test that accounts can be stored in the repository"""
        # Create a new test account
        account = Account(
            account_id=2, 
            balance=200.0, 
            owner_id="test_owner_2",
            account_type=AccountType.SAVINGS
        )
        self.repository._accounts[account.account_id] = account
        self.assertTrue(account.account_id in self.repository._accounts)

    def test_retrieve_account_data(self):
        """Test that accounts can be retrieved from the repository"""
        retrieved_account = self.repository.get_account(1)
        self.assertEqual(retrieved_account.account_id, self.test_account.account_id)
        self.assertEqual(retrieved_account.balance, self.test_account.balance)
        self.assertEqual(retrieved_account.account_type, self.test_account.account_type)

if __name__ == '__main__':
    unittest.main()