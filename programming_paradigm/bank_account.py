class BankAccount:
    """Represents a bank account with basic operations."""

    def __init__(self, initial_balance=0):
        """Initializes the account balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraws the specified amount if sufficient funds exist."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Displays the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")



