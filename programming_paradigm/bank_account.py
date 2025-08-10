class BankAccount:
    """
    A simple class to represent a bank account.

    Attributes:
        _account_balance (float): The current balance of the account.
    """
    def __init__(self, initial_balance=0.0):
        """
        Initializes the bank account with an optional initial balance.

        Args:
            initial_balance (float): The starting balance, must be non-negative.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit, must be positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the specified amount from the balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw, must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:,.2f}")