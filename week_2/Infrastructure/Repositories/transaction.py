import uuid
from account import AccountRepository

class Transaction:
    def __init__(self, source_account, destination_account, amount, transaction_type='TRANSFER'):
        self.transaction_id = str(uuid.uuid4())
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"[{self.transaction_type}] ${self.amount} from {self.source_account.account_id} to {self.destination_account.account_id} (ID: {self.transaction_id})"

class TransactionRepository:
    """ A class containg This method saves a transaction 
    into the _transactions dictionary.
    It uses transaction.transaction_id as
    the key and the transaction object itself as the value.
    It prints a log (simulated logging)
    to show the transaction was saved.
    Finally, it returns the ID of the 
    saved transaction."""
    def __init__(self):
        self._transactions = {}

    def save(self, transaction: Transaction):
        self._transactions[transaction.transaction_id] = transaction
        print(f"[REPO] Saved transaction: {transaction}")
        return transaction.transaction_id

    def find_by_transaction_id(self, transaction_id: str) -> Transaction:
        return self._transactions.get(transaction_id)


