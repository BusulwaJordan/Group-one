import threading

class AccountRepository:
    def __init__(self, accounts):
        self._accounts = {acc.account_id: acc for acc in accounts}
        self._lock = threading.Lock()  # Simulate concurrency control

    def get_account(self, account_id):
        return self._accounts.get(account_id)

    def can_transfer(self, source_account_id, amount):
        account = self.get_account(source_account_id)
        if account is None:
            raise ValueError("Source account does not exist")
        return account.balance >= amount

    def update_balances_atomically(self, source_account_id, destination_account_id, amount):
        with self._lock:
            source = self.get_account(source_account_id)
            destination = self.get_account(destination_account_id)

            if not source or not destination:
                raise ValueError("Invalid source or destination account")

            if source.balance < amount:
                raise ValueError("Insufficient funds in source account")

            # Atomic-like update
            source.withdraw(amount)
            destination.deposit(amount)

            print(f"[REPO] Transferred ${amount} from Account {source_account_id} to {destination_account_id}")
            return source, destination
