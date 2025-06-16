from ..entities.transaction import Transaction

class TransactionService:
    def __init__(self):
        self.transactions = {}
        self.transaction_counter = 0

    def generate_transaction_id(self):
        self.transaction_counter += 1
        return f"txn-{self.transaction_counter}"

    def save(self, transaction):
        self.transactions[transaction.transaction_id] = transaction
from ..entities.transaction import Transaction

class TransactionService:
    def __init__(self):
        self.transactions = {}
        self.transaction_counter = 0

    def generate_transaction_id(self):
        self.transaction_counter += 1
        return f"txn-{self.transaction_counter}"

    def save(self, transaction):
        self.transactions[transaction.transaction_id] = transaction
