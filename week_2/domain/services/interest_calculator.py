from datetime import datetime
from decimal import Decimal
from typing import List
from ..entities.account import Account

class InterestCalculator:
    """Service class for calculating and applying interest to bank accounts.
    
    This class provides static methods to calculate and process monthly interest
    for both individual accounts and collections of accounts. Interest is only
    applied to active savings accounts at their specified interest rate.
    """
    
    @staticmethod
    def calculate_monthly_interest(account: Account, current_date: datetime) -> Decimal:
        """Calculate and apply monthly interest for a single account.
        
        Args:
            account: The Account object to calculate interest for
            current_date: The date to calculate interest up to
            
        Returns:
            Decimal: The amount of interest calculated and applied
            
        Note:
            - Only active accounts earn interest
            - Only savings accounts earn interest at their specified rate
            - Interest is calculated based on the number of days since last calculation
        """
        if account.status != "ACTIVE":
            return Decimal("0.00")
            
        interest = account.calculate_interest(current_date)
        account.apply_interest(interest)
        return interest

    @staticmethod
    def process_monthly_interest(accounts: List[Account]) -> None:
        """Process monthly interest for a collection of accounts.
        
        Args:
            accounts: List of Account objects to process interest for
            
        Note:
            This method processes interest for all accounts using the current date.
            It's typically called by a scheduled task once per month.
        """
        current_date = datetime.now()
        for account in accounts:
            InterestCalculator.calculate_monthly_interest(account, current_date)