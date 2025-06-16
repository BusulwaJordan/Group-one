class TransactionType:
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER = "TRANSFER"

class Transaction:
    def __init__(self, transaction_id, source_account_id, destination_account_id, amount, transaction_type):
        self.transaction_id = transaction_id
        self.source_account_id = source_account_id
        self.destination_account_id = destination_account_id
        self.amount = amount
        self.transaction_type = transaction_type
