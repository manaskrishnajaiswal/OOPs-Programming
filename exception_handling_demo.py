# 1. Custom Exception Class
class InvalidAgeError(Exception):
    """
    Custom exception raised for invalid age values during voting checks.
    """
    def __init__(self, age: int, message="Not eligible to vote due to age constraints"):
        self.age = age
        self.message = f"{message}: {age}"
        super().__init__(self.message)


# 2. Raising Exceptions & Propagation
def verify_voting_age(age: int):
    """
    Checks age eligibility. Raises standard ValueError for negative inputs
    and custom InvalidAgeError for minor age inputs.
    """
    if age < 0:
        # Standard built-in exception
        raise ValueError("Age cannot be negative.")
    if age < 18:
        # Custom exception
        raise InvalidAgeError(age)
    print(f"Age {age} verified. Eligible to vote.")


def main():
    print("--- 1. Handling Multiple Specific Exceptions ---")
    try:
        arr = [1, 2, 3]
        # First error: index out of bounds
        print(arr[5])  
        
        # Second error: division by zero (won't reach this because first error exits try block)
        result = 10 / 0
        print(result)
    except IndexError:
        print("Caught: IndexError (index out of range).")
    except ZeroDivisionError:
        print("Caught: ZeroDivisionError (division by zero).")
    print()

    print("--- 2. Try-Except-Else-Finally Blocks ---")
    try:
        result = 10 / 2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Caught Division by Zero.")
    else:
        # Executes only if no exception is raised inside the try block
        print("Else Block -> Executed because try block ran successfully.")
    finally:
        # Always executes regardless of errors or try-except outcomes
        print("Finally Block -> Resource cleanup completed.")
    print()

    print("--- 3. Raising Custom Exceptions ---")
    test_ages = [20, 15, -3]
    for age in test_ages:
        try:
            print(f"Verifying Age: {age}")
            verify_voting_age(age)
        except InvalidAgeError as e:
            print(f"Caught Custom Exception -> {e.message}")
        except ValueError as e:
            print(f"Caught standard exception -> {e}")
        print()

    print("--- 4. Real-life Scenario: File Handling ---")
    try:
        # Attempting to read a file that does not exist
        with open("nonexistent.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("Caught FileNotFoundError: 'nonexistent.txt' does not exist. Gracefully continuing.")
    print()

    print("Program execution continues and finishes safely.")


if __name__ == "__main__":
    main()
