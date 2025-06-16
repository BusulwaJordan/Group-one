from fund_transfer import Account
from notification import *

class LoggingTransactionService:
    def __init__(self, wrapped_service):
        self.wrapped = wrapped_service

    def withdraw(self, account_id, amount):
        print(f"[LOG] Attempting to withdraw ${amount} from account {account_id}")
        result = self.wrapped.withdraw(account_id, amount)
        print(f"[LOG] Withdrawal of ${amount} from account {account_id} successful")
        return result

    def deposit(self, account_id, amount):
        print(f"[LOG] Attempting to deposit ${amount} into account {account_id}")
        result = self.wrapped.deposit(account_id, amount)
        print(f"[LOG] Deposit of ${amount} into account {account_id} successful")
        return result

    def transfer_funds(self, source_account_id, destination_account_id, amount):
        print(f"[LOG] Initiating transfer of ${amount} from account {source_account_id} to {destination_account_id}")
        transaction = self.wrapped.transfer_funds(source_account_id, destination_account_id, amount)
        print(f"[LOG] Transfer completed: ${amount} from {source_account_id} to {destination_account_id}")
        return transaction
