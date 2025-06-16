from datetime import datetime
from decimal import Decimal
from typing import List
from domain.entities.monthly_statement import MonthlyStatement
from domain.entities.transaction import Transaction
from Infrastructure.Repositories.account import AccountRepository
from Infrastructure.Repositories.transaction import TransactionRepository

class StatementService:
    """Service for generating and managing monthly account statements"""
    
    def __init__(self, account_repository: AccountRepository, 
                 transaction_repository: TransactionRepository):
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository

    def generate_monthly_statement(self, account_id: int, month: int, year: int) -> MonthlyStatement:
        """Generate a monthly statement for a specific account and period"""
        
        account = self.account_repository.get_account(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found")

        # Get all transactions for the account in the specified month
        transactions = self._get_monthly_transactions(account_id, month, year)
        
        # Calculate opening and closing balances
        opening_balance = self._calculate_opening_balance(account_id, month, year)
        closing_balance = account.balance
        
        # Calculate interest earned
        interest_earned = account.calculate_interest(datetime.now())

        return MonthlyStatement(
            account_id=account_id,
            month=month,
            year=year,
            opening_balance=opening_balance,
            closing_balance=closing_balance,
            transactions=transactions,
            interest_earned=interest_earned,
            statement_date=datetime.now()
        )

    def _get_monthly_transactions(self, account_id: int, month: int, year: int) -> List[Transaction]:
        """get all the transactions for an account for a specific month"""
        # return all transactions
        return self.transaction_repository.get_transactions_for_account(account_id)

    def _calculate_opening_balance(self, account_id: int, month: int, year: int) -> Decimal:
        """Calculate the opening balance for the specified month"""
        # return a dummy value
        return Decimal("0.00")