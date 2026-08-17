from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract Class representing an Animal.
    Cannot be instantiated directly.
    """
    def __init__(self, name: str):
        # Abstract classes can define constructors to initialize shared attributes
        self.name = name

    @abstractmethod
    def sound(self):
        """Abstract method - must be implemented by concrete subclasses."""
        pass

    def eat(self):
        """Concrete method - inherits directly by subclasses."""
        print(f"{self.name} is eating food.")


# 1. Abstract class extending another Abstract class
class WingedAnimal(Animal, ABC):
    """
    Abstract class inheriting from Animal. 
    Leaves sound() unimplemented and adds another abstract method fly().
    """
    @abstractmethod
    def fly(self):
        pass


# 2. Interfaces Simulation in Python
# Python doesn't have an 'interface' keyword. Instead, we use Abstract Base Classes (ABCs)
# containing only abstract methods, and implement them via Multiple Inheritance.
class SwimmerInterface(ABC):
    @abstractmethod
    def swim(self):
        pass


# 3. Concrete Subclasses providing implementations
class Dog(Animal, SwimmerInterface):
    """
    Concrete subclass. Implements sound() from Animal and swim() from SwimmerInterface.
    """
    def __init__(self, name: str):
        super().__init__(name)  # Invoke parent abstract constructor

    def sound(self):
        print(f"{self.name} says: Woof! Woof!")

    def swim(self):
        print(f"{self.name} is swimming in the pool.")


class Duck(WingedAnimal):
    """
    Concrete subclass. Implements sound() (inherited from Animal) and fly() (from WingedAnimal).
    """
    def __init__(self, name: str):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} says: Quack! Quack!")

    def fly(self):
        print(f"{self.name} is flying high in the sky.")


# 4. Static Method Demo
class MathHelper:
    """
    Demonstrates Static Methods.
    Static methods are bound to the class rather than its objects. They cannot
    access instance state (no self) or class state (no cls).
    """
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y


def main():
    print("--- 1. Abstract Class Instantiation Check ---")
    try:
        # Instantiating an abstract class directly will raise a TypeError
        animal = Animal("Generic Animal")
    except TypeError as e:
        print(f"Instantiation Blocked (Expected): {e}")
    print()

    print("--- 2. Concrete Subclass (Dog) ---")
    dog = Dog("Buddy")
    dog.sound()  # Overridden abstract method
    dog.eat()    # Inherited concrete method
    dog.swim()   # Implemented interface method
    print()

    print("--- 3. Multilevel Abstraction (Duck) ---")
    duck = Duck("Donald")
    duck.sound()
    duck.eat()
    duck.fly()
    print()

    print("--- 4. Static Methods ---")
    # Called on class directly without instantiation
    sum_result = MathHelper.add(12.5, 7.5)
    print(f"MathHelper.add(12.5, 7.5) = {sum_result}")


if __name__ == "__main__":
    main()
