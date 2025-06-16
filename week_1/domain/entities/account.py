from datetime import datetime
from decimal import Decimal
from typing import List

class AccountType:
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"

class Account:
    def __init__(self, account_id: int, balance: float, owner_id: str, account_type: str):
        self.account_id = account_id
        self.balance = Decimal(str(balance))
        self.owner_id = owner_id
        self.account_type = account_type
        self.creation_date = datetime.now()
        self.status = "ACTIVE"
        self.daily_withdrawal_limit = Decimal("1000.00")
        self.daily_withdrawals = Decimal("0.00")
        self.interest_rate = Decimal("0.01") if account_type == AccountType.SAVINGS else Decimal("0.00")
        self.last_interest_calculation = self.creation_date

    def get_balance(self) -> Decimal:
        return self.balance

    def withdraw(self, amount: Decimal) -> None:
        if self.status != "ACTIVE":
            raise ValueError("Account is not active")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        if self.daily_withdrawals + amount > self.daily_withdrawal_limit:
            raise ValueError("Daily withdrawal limit exceeded")
        self.balance -= amount
        self.daily_withdrawals += amount

    def deposit(self, amount: Decimal) -> None:
        if self.status != "ACTIVE":
            raise ValueError("Account is not active")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def calculate_interest(self, current_date: datetime) -> Decimal:
        if self.account_type != AccountType.SAVINGS:
            return Decimal("0.00")
        
        days = (current_date - self.last_interest_calculation).days
        interest = self.balance * (self.interest_rate / Decimal("365")) * Decimal(str(days))
        self.last_interest_calculation = current_date
        return interest

    def apply_interest(self, interest: Decimal) -> None:
        if interest > 0:
            self.deposit(interest)

    def reset_daily_limits(self) -> None:
        self.daily_withdrawals = Decimal("0.00")

    def close(self) -> None:
        self.status = "CLOSED"
