from typing import TypeVar, Generic, Union, Any

# 1. Declare type variables for generic parameters
T = TypeVar("T")  # Unconstrained type parameter


# 2. Generic Class Definition
class Box(Generic[T]):
    """
    A generic class representing a container.
    """
    def __init__(self, value: T):
        self.value: T = value

    def set(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value


# 3. Generic Method / Function
def print_and_return(data: T) -> T:
    """
    Generic utility function that prints and returns the passed data.
    """
    print(f"Generic Data: {data} (Type: {type(data).__name__})")
    return data


# 4. Bounded Type Parameters
class Vehicle:
    def start_engine(self) -> str:
        return "Generic engine started."


class Car(Vehicle):
    def start_engine(self) -> str:
        return "Car engine purring."


# Restricting the type variable V to be a Vehicle or subclass of Vehicle
V = TypeVar("V", bound=Vehicle)


def ignite_vehicle(vehicle: V) -> None:
    # Guaranteed safe access to start_engine due to bound constraint
    print(f"Ignition: {vehicle.start_engine()}")


# 5. Wildcards (Union / Any)
def process_union(data: Union[int, str]) -> None:
    """
    Simulates wildcard restriction using Union.
    """
    print(f"Union processing: {data} (Type: {type(data).__name__})")


def main():
    print("--- 1. Generic Class (Box[T]) ---")
    int_box = Box[int](100)
    str_box = Box[str]("Hello Generics")

    print(f"Int Box Value: {int_box.get()}")
    print(f"Str Box Value: {str_box.get()}")
    print()

    print("--- 2. Generic Function ---")
    # Works seamlessly across different types
    print_and_return(42)
    print_and_return("Generics in Python")
    print_and_return(3.14159)
    print()

    print("--- 3. Bounded Type Parameters ---")
    my_car = Car()
    ignite_vehicle(my_car)
    # ignite_vehicle("Not a vehicle") -> Static type checkers will flag this as an error
    print()

    print("--- 4. Union / Wildcard Simulation ---")
    process_union(10)
    process_union("Accepted String")
    # process_union(5.5) -> Static type checkers flag float
    print()

    print("--- 5. Runtime Behavior (Type Erasure Equivalent) ---")
    # Python does not enforce generic type hints at runtime.
    # The following code bypasses static constraints and executes without raising errors.
    bad_box = Box[int](10)
    bad_box.set("Bypassing Int Constraint")  # Static error, but executes at runtime
    print(f"Runtime Value: {bad_box.get()} (Type: {type(bad_box.get()).__name__})")


if __name__ == "__main__":
    main()
