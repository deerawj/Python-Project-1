class User:
    def __init__(self, name: str, email: str):
        self.name: str = name
        self.email: str = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self) -> float:
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self) -> int:
        return len(self.accounts)

    def remove_account(self, account) -> bool:
        if account in self.accounts:
            self.accounts.remove(account)
            return True
        else:
            return False

    def is_valid_email(self, email: str) -> bool:
        # This should work for most common cases;
        # but this is not perfect
        if "@" in email and "." in email:
            return True
        return False

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance()}"
