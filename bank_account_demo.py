class BankAccount:
    """
    Represents a bank account with encapsulated attributes and validation-controlled methods.
    """
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        self._owner_name = owner_name
        # Double underscores '__' invoke Python's name mangling to simulate private attributes
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance

    # Getter for owner name
    def get_owner_name(self) -> str:
        return self._owner_name

    # Setter for owner name
    def set_owner_name(self, name: str):
        if not name.strip():
            raise ValueError("Owner name cannot be empty.")
        self._owner_name = name

    # Getter for balance
    def get_balance(self) -> float:
        return self.__balance

    # Method to deposit money
    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.__balance += amount
        print(f"Successfully deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}")
        return True

    # Method to withdraw money
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.__balance:
            print(f"Error: Insufficient funds. Available Balance: ${self.__balance:.2f}")
            return False
        self.__balance -= amount
        print(f"Successfully withdrew ${amount:.2f}. Remaining Balance: ${self.__balance:.2f}")
        return True


def main():
    # Creating a BankAccount object
    print("--- Creating Bank Account for Raj ---")
    account = BankAccount("Raj", 1000.0)
    print(f"Account Holder: {account.get_owner_name()}")
    print(f"Initial Balance: ${account.get_balance():.2f}\n")

    # Testing Deposits
    print("--- Testing Deposit ---")
    account.deposit(500.0)
    account.deposit(-50.0)  # Invalid deposit
    print()

    # Testing Withdrawals
    print("--- Testing Withdrawal ---")
    account.withdraw(300.0)
    account.withdraw(1500.0)  # Insufficient funds
    account.withdraw(-20.0)  # Invalid withdrawal
    print()

    # Final Summary
    print("--- Final State ---")
    print(f"Holder: {account.get_owner_name()}")
    print(f"Final Balance: ${account.get_balance():.2f}")


if __name__ == "__main__":
    main()
