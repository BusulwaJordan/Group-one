import unittest
from datetime import datetime
from decimal import Decimal
from domain.entities.account import Account, AccountType
from domain.entities.transaction import Transaction
from Application.statement_service import StatementService
from Infrastructure.Repositories.account import AccountRepository
from Infrastructure.Repositories.transaction import TransactionRepository

class TestStatementService(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        # Create test account
        self.test_account = Account(
            account_id=1,
            balance=1000.00,
            owner_id="test_owner",
            account_type=AccountType.SAVINGS
        )
        
        # Create repositories
        self.account_repository = AccountRepository([self.test_account])
        self.transaction_repository = TransactionRepository()
        
        # Create statement service
        self.statement_service = StatementService(
            self.account_repository,
            self.transaction_repository
        )

    def test_generate_monthly_statement(self):
        """Test monthly statement generation"""
        # Generate statement for current month
        current_date = datetime.now()
        statement = self.statement_service.generate_monthly_statement(
            account_id=1,
            month=current_date.month,
            year=current_date.year
        )
        
        # Verify statement properties
        self.assertEqual(statement.account_id, 1)
        self.assertEqual(statement.month, current_date.month)
        self.assertEqual(statement.year, current_date.year)
        self.assertEqual(statement.opening_balance, Decimal("0.00"))
        self.assertEqual(statement.closing_balance, Decimal("1000.00"))

    def test_generate_statement_invalid_account(self):
        """Test statement generation for non-existent account"""
        current_date = datetime.now()
        with self.assertRaises(ValueError):
            self.statement_service.generate_monthly_statement(
                account_id=999,  # Non-existent account
                month=current_date.month,
                year=current_date.year
            )

if __name__ == '__main__':
    unittest.main()