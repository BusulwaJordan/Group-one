import unittest
from datetime import datetime, timedelta
from decimal import Decimal
from domain.entities.account import Account, AccountType
from domain.services.interest_calculator import InterestCalculator

class TestInterestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method"""
        # Create a test savings account with 1000.00 initial balance and 1% interest rate
        self.savings_account = Account(
            account_id=1,
            balance=1000.00,
            owner_id="test_owner",
            account_type=AccountType.SAVINGS
        )
        
        # Create a test checking account with 1000.00 initial balance (0% interest rate)
        self.checking_account = Account(
            account_id=2,
            balance=1000.00,
            owner_id="test_owner",
            account_type=AccountType.CHECKING
        )

    def test_calculate_monthly_interest_savings(self):
        """Test interest calculation for savings account"""
        # Set current date to 30 days after account creation
        current_date = self.savings_account.creation_date + timedelta(days=30)
        
        # Calculate interest
        interest = InterestCalculator.calculate_monthly_interest(
            self.savings_account, 
            current_date
        )
        
        # Expected interest for 30 days at 1% annual rate
        # (1000 * 0.01 * 30/365) ≈ 0.82 
        self.assertAlmostEqual(float(interest), 0.82, places=2)

    def test_calculate_monthly_interest_checking(self):
        """Test interest calculation for checking account (should be zero)"""
        current_date = self.checking_account.creation_date + timedelta(days=30)
        interest = InterestCalculator.calculate_monthly_interest(
            self.checking_account, 
            current_date
        )
        self.assertEqual(interest, Decimal("0.00"))

    def test_inactive_account_no_interest(self):
        """Test that inactive accounts don't earn interest"""
        self.savings_account.status = "CLOSED"
        current_date = self.savings_account.creation_date + timedelta(days=30)
        interest = InterestCalculator.calculate_monthly_interest(
            self.savings_account, 
            current_date
        )
        self.assertEqual(interest, Decimal("0.00"))

if __name__ == '__main__':
    unittest.main()