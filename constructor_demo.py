class NonParameterizedDemo:
    """
    Demonstrates a Non-parameterized Constructor.
    Does not take arguments other than 'self'.
    """
    def __init__(self):
        self.message = "Hello from Non-Parameterized Constructor!"


class ParameterizedDemo:
    """
    Demonstrates a Parameterized Constructor.
    Takes user arguments to initialize attributes.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class CopyConstructorDemo:
    """
    Demonstrates manual implementation of a Copy Constructor in Python.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Class method acting as a copy constructor
    @classmethod
    def from_existing(cls, existing_obj):
        return cls(existing_obj.name, existing_obj.age)


class OverloadingDemo:
    """
    Demonstrates how to simulate constructor overloading in Python.
    Since Python does not natively support overloading, we use default parameters
    and class methods as alternative constructors.
    """
    # Overloading via default parameters
    def __init__(self, name: str = "Guest", age: int = 18):
        self.name = name
        self.age = age

    # Overloading via alternative class method constructor
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        from datetime import datetime
        current_year = datetime.now().year
        calculated_age = current_year - birth_year
        return cls(name, calculated_age)


class ParentClass:
    """
    Parent class to demonstrate constructor chaining.
    """
    def __init__(self, brand: str):
        self.brand = brand
        print(f"Parent constructor invoked. Brand: {self.brand}")


class ChildClass(ParentClass):
    """
    Child class to demonstrate constructor chaining using super().__init__().
    """
    def __init__(self, brand: str, model: str):
        # Chaining to Parent constructor
        super().__init__(brand)
        self.model = model
        print(f"Child constructor invoked. Model: {self.model}")


def main():
    # 1. Non-parameterized Constructor
    print("--- 1. Non-parameterized Constructor ---")
    obj1 = NonParameterizedDemo()
    print(obj1.message)
    print()

    # 2. Parameterized Constructor
    print("--- 2. Parameterized Constructor ---")
    obj2 = ParameterizedDemo("Alice", 25)
    print(f"Name: {obj2.name}, Age: {obj2.age}")
    print()

    # 3. Copy Constructor
    print("--- 3. Copy Constructor ---")
    original = CopyConstructorDemo("Bob", 30)
    copied = CopyConstructorDemo.from_existing(original)
    print(f"Original: Name={original.name}, Age={original.age}")
    print(f"Copied: Name={copied.name}, Age={copied.age}")
    print(f"Is same object reference? {original is copied}")
    print()

    # 4. Constructor Overloading Simulation
    print("--- 4. Constructor Overloading Simulation ---")
    default_user = OverloadingDemo()
    custom_user = OverloadingDemo("Charlie", 35)
    alternative_user = OverloadingDemo.from_birth_year("Diana", 1996)
    print(f"Default user: Name={default_user.name}, Age={default_user.age}")
    print(f"Custom user: Name={custom_user.name}, Age={custom_user.age}")
    print(f"Alternative (birth year) user: Name={alternative_user.name}, Age={alternative_user.age}")
    print()

    # 5. Constructor Chaining
    print("--- 5. Constructor Chaining ---")
    car = ChildClass("Tesla", "Model S")
    print(f"Car Details: Brand={car.brand}, Model={car.model}")


if __name__ == "__main__":
    main()
