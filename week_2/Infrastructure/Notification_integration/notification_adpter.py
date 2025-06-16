from infrastructure.account import Account

# Interface for sending messages
class MessageSender(Account):

    @abstractmethod
    def send_email(self, recipient: str, subject: str, body: str):
        pass

    @abstractmethod
    def send_sms(self, number: str, message: str):
        pass


# Real provider (simulated via print/logging)
class RealMessageSender(MessageSender):
    def send_email(self, recipient: str, subject: str, body: str):
        print(f"[EMAIL] To: {recipient} | Subject: {subject} | Body: {body}")

    def send_sms(self, number: str, message: str):
        print(f"[SMS] To: {number} | Message: {message}")


# Mock provider for testing
class MockMessageSender(MessageSender):
    def __init__(self):
        self.sent_emails = []
        self.sent_sms = []

    def send_email(self, recipient: str, subject: str, body: str):
        self.sent_emails.append((recipient, subject, body))

    def send_sms(self, number: str, message: str):
        self.sent_sms.append((number, message))
