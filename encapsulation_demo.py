class EncapsulatedBankAccount:
    """
    Demonstrates Encapsulation (Data Hiding) in Python.
    Bundles data (name, balance) and methods (getters, setters, deposit) together,
    restricting direct attribute access to maintain object integrity.
    """
    def __init__(self, holder_name: str, balance: float):
        # Private attributes using double underscores to trigger name mangling
        self.__holder_name = holder_name
        self.__balance = balance

    # Getter for holder_name
    def get_holder_name(self) -> str:
        return self.__holder_name

    # Setter for holder_name
    def set_holder_name(self, name: str):
        if not name.strip():
            print("Validation Error: Name cannot be empty.")
            return
        self.__holder_name = name

    # Getter for balance
    def get_balance(self) -> float:
        return self.__balance

    # Controlled modifier (deposit) with validation logic
    def deposit(self, amount: float):
        if amount <= 0:
            print("Validation Error: Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Successfully deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}")


def main():
    # Instantiating the encapsulated object
    print("--- Instantiating EncapsulatedBankAccount ---")
    acc = EncapsulatedBankAccount("Raj", 1000.0)
    
    # 1. Accessing via public interface (Getters)
    print(f"Account Holder: {acc.get_holder_name()}")
    print(f"Account Balance: ${acc.get_balance():.2f}")
    print()

    # 2. Testing controlled modification (validation)
    print("--- Performing Controlled Modifications ---")
    acc.set_holder_name("Raj Kumar")
    acc.deposit(500.0)
    acc.deposit(-100.0)  # Should trigger validation print
    print(f"Updated Account Holder: {acc.get_holder_name()}")
    print(f"Updated Balance: ${acc.get_balance():.2f}")
    print()

    # 3. Attempting direct access to private attributes
    print("--- Attempting Direct Private Attribute Access ---")
    try:
        # Direct access fails with AttributeError
        print(acc.__balance)
    except AttributeError as e:
        print(f"Access Denied (AttributeError): {e}")

    # 4. Demonstrating Python's naming convention nature (Mangled Access)
    print("\n--- Accessing via Mangled Name (Python Naming Convention Mechanism) ---")
    mangled_balance = acc._EncapsulatedBankAccount__balance
    print(f"Accessed via _EncapsulatedBankAccount__balance: ${mangled_balance:.2f}")


if __name__ == "__main__":
    main()
