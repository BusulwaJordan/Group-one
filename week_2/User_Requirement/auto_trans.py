
class Account:
    """shows the owner's account """
    def __init__(self, account_id, owner_id, balance):
        self.account_id = account_id
        self.owner_id = owner_id
        self.balance = balance

    def deposit(self, amount, dispatcher=None):
        self.balance += amount
        self._notify("deposit", amount, dispatcher)

    def withdraw(self, amount, dispatcher=None):
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._notify("withdrawal", amount, dispatcher)

    def _notify(self, tx_type, amount, dispatcher):
        """ broadcast messages (events) to anyone who's interested
          by Registering alisteners (like email or SMS)"""
        if dispatcher:
            dispatcher.dispatch("transaction_finalized", {
                "type": tx_type,
                "amount": amount,
                "account": self.account_id,
                "message": f"{tx_type.capitalize()} of ${amount:.2f} on account {self.account_id}"
            })


class Transfer:
    def __init__(self, source: Account, dest: Account, amount: float):
        self.source = source
        self.dest = dest
        self.amount = amount
        self.status = "PENDING"

    def execute(self, dispatcher=None):
        if self.status != "PENDING":
            raise ValueError("Already executed")
        self.source.withdraw(self.amount)
        self.dest.deposit(self.amount)
        self.status = "COMPLETED"

        if dispatcher:
            dispatcher.dispatch("transaction_finalized", {
                "type": "transfer",
                "amount": self.amount,
                "from": self.source.account_id,
                "to": self.dest.account_id,
                "message": f"Transfer of ${self.amount:.2f} from {self.source.account_id} to {self.dest.account_id}"
            })
