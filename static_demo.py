class Counter:
    # 1. Class Variable (Static Variable) - Shared across all instances
    count = 0

    # 2. Static Block Equivalent
    # Code written directly inside the class body runs once at class definition time.
    print("Counter class body executed (One-time Static Setup Equivalent).")

    def __init__(self, name: str):
        # Increment the shared class variable when a new object is instantiated
        Counter.count += 1
        self.name = name
        self.instance_id = Counter.count

    # 3. Static Method (@staticmethod)
    # Behave like plain functions inside the class namespace. No 'self' or 'cls' parameter.
    @staticmethod
    def display_count():
        print(f"Static Method -> Total instances created: {Counter.count}")

    # 4. Class Method (@classmethod)
    # Receives the class 'cls' as the first parameter. Can access/modify class state.
    @classmethod
    def reset_count(cls):
        print("Class Method -> Resetting global counter to 0...")
        cls.count = 0

    # 5. Static Method accessing Instance Members (requires explicit object reference)
    @staticmethod
    def print_instance_details(obj):
        # Cannot access instance variables directly, must accept object parameter
        print(f"Static Method -> Object Name: {obj.name}, ID: {obj.instance_id}")


def main():
    print("\n--- 1. Instantiating Objects ---")
    c1 = Counter("Alice")
    c2 = Counter("Bob")
    print(f"c1 ID: {c1.instance_id}, c2 ID: {c2.instance_id}")
    print()

    print("--- 2. Calling Static Method ---")
    # Calling static method on the class directly
    Counter.display_count()
    print()

    print("--- 3. Calling Class Method ---")
    # Modifies class-level state
    Counter.reset_count()
    Counter.display_count()
    print()

    print("--- 4. Static and Instance Interaction ---")
    # Create new instance (count becomes 1)
    c3 = Counter("Charlie")
    Counter.print_instance_details(c3)


if __name__ == "__main__":
    main()
