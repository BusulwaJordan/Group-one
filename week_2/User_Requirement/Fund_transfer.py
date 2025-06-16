from dataclasses import dataclass
from datetime import datetime
import uuid

# --- Account Representation ---
@dataclass
class Account:
    account_id: str
    owner_id: str
    balance: float

   #deduct money from the account
    def debit(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    #Adds money to the account
    def credit(self, amount):
        self.balance += amount


# --- Transfer Operation Representation ---
@dataclass
class Transfer:
    transfer_id: str
    source_account: Account
    destination_account: Account
    amount: float
    timestamp: datetime
    status: str = "PENDING"
    reversible: bool = True

    def execute(self):
        if self.status != "PENDING":
            raise ValueError("Transfer already processed")
        self.source_account.debit(self.amount)
        self.destination_account.credit(self.amount)
        self.status = "COMPLETED"
        print(f"Transfer {self.transfer_id} executed.")

    def reverse(self):
        if self.status != "COMPLETED" or not self.reversible:
            raise ValueError("Cannot reverse this transfer")
        self.destination_account.debit(self.amount)
        self.source_account.credit(self.amount)
        self.status = "REVERSED"
        print(f"Transfer {self.transfer_id} reversed.")



class TransferService:
    """Transfer Service 
 Keeps a dictionary of all transfers"""
    def __init__(self):
        self.transfers = {}

    # Sets up a new transfer request.
    def create_transfer(self, source, dest, amount):
        if source.owner_id != dest.owner_id:
            raise PermissionError("Accounts must belong to the same user")
       
        #new Transfer object with a unique ID
        transfer_id = str(uuid.uuid4())
        transfer = Transfer(
            transfer_id=transfer_id,
            source_account=source,
            destination_account=dest,
            amount=amount,
            timestamp=datetime.now()
        )
        self.transfers[transfer_id] = transfer
        return transfer

