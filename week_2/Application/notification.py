class User:
    def __init__(self, user_id, name, email, phone_number):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone_number = phone_number


class Account:
    def __init__(self, account_id, user, balance):
        self.account_id = account_id
        self.user = user
        self.balance = balance


class Transaction:
    def __init__(self, source_account, destination_account, amount, transaction_type='TRANSFER'):
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.transaction_type = transaction_type

class EmailService:
    def send_email(self, to, subject, body):
        print(f"[EMAIL to {to}] {subject}\n{body}\n")


class SMSService:
    def send_sms(self, to, message):
        print(f"[SMS to {to}] {message}")


class NotificationService:
    def __init__(self, email_service, sms_service):
        self.email_service = email_service
        self.sms_service = sms_service

    def notify(self, transaction: Transaction):
        source_user = transaction.source_account.user
        dest_user = transaction.destination_account.user
        amount = transaction.amount

        # Notify source user
        source_subject = "Funds Transferred"
        source_body = f"Hello {source_user.name},\nYou have transferred ${amount} to account {transaction.destination_account.account_id}."
        self.email_service.send_email(source_user.email, source_subject, source_body)
        self.sms_service.send_sms(source_user.phone_number, f"You transferred ${amount}.")

        # Notify destination user
        dest_subject = "Funds Received"
        dest_body = f"Hello {dest_user.name},\nYou have received ${amount} from account {transaction.source_account.account_id}."
        self.email_service.send_email(dest_user.email, dest_subject, dest_body)
        self.sms_service.send_sms(dest_user.phone_number, f"You received ${amount}.")
