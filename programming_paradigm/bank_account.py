class BankAccount:
    """This class models banking operations."""

    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
            self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

account = BankAccount()

account.deposit(20)
account.display_balance()


account.withdraw(5)
account.display_balance()