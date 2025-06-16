from domain.entities.account import Account

class AccountService:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_id] = account

    def find_by_id(self, account_id):
        return self.accounts.get(account_id)
