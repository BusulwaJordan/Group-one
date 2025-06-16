from ..entities.account import Account
from ..entities.transaction import Transaction, TransactionType

class TransferException(Exception):
    pass

class TransferService:
    def __init__(self, account_service, transaction_service):
        self.account_service = account_service
        self.transaction_service = transaction_service

    def transfer(self, source_account_id, destination_account_id, amount):
        source_account = self.account_service.find_by_id(source_account_id)
        destination_account = self.account_service.find_by_id(destination_account_id)

        if source_account is None or destination_account is None:
            raise TransferException("Invalid account(s)")

        if not source_account.can_transfer(amount):
            raise TransferException("Insufficient funds for transfer")

        # Start atomic transfer
        try:
            source_account.withdraw(amount)
            destination_account.deposit(amount)

            transaction = Transaction(
                transaction_id=self.transaction_service.generate_transaction_id(),
                source_account_id=source_account_id,
                destination_account_id=destination_account_id,
                amount=amount,
                transaction_type=TransactionType.TRANSFER
            )
            self.transaction_service.save(transaction)
        except Exception as e:
            # Rollback if any operation fails
            raise TransferException(f"Transfer failed: {str(e)}")
