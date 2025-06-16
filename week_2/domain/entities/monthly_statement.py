from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List
from .transaction import Transaction

@dataclass
class MonthlyStatement:
    account_id: int
    month: int
    year: int
    opening_balance: Decimal
    closing_balance: Decimal
    transactions: List[Transaction]
    interest_earned: Decimal
    statement_date: datetime

    def calculate_total_deposits(self) -> Decimal:
        return sum(t.amount for t in self.transactions if t.transaction_type == "DEPOSIT")

    def calculate_total_withdrawals(self) -> Decimal:
        return sum(t.amount for t in self.transactions if t.transaction_type == "WITHDRAWAL")

    def calculate_total_transfers(self) -> Decimal:
        return sum(t.amount for t in self.transactions if t.transaction_type == "TRANSFER")