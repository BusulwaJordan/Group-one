class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount


class Transaction:
    def __init__(self, source_account, destination_account, amount):
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.transaction_type = 'TRANSFER'

    def save(self):
        # Simulate saving to a database (e.g., using ORM)
        print(f"Transaction: {self.source_account.account_id} -> {self.destination_account.account_id} Amount: {self.amount}")


class FundTransferService:
    def __init__(self, accounts):
        self.accounts = {account.account_id: account for account in accounts}

    def transfer_funds(self, source_account_id, destination_account_id, amount):
        source_account = self.accounts.get(source_account_id)
        destination_account = self.accounts.get(destination_account_id)

        if not source_account or not destination_account:
            raise ValueError("Invalid source or destination account ID")

        if not source_account.withdraw(amount):
            raise ValueError("Insufficient funds in source account")

        destination_account.deposit(amount)

        # Create and save the transaction
        transaction = Transaction(source_account, destination_account, amount)
        transaction.save()

