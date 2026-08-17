class Shape:
    """
    Base class representing a generic shape.
    """
    def draw(self):
        print("Drawing a generic shape.")


class Circle(Shape):
    """
    Subclass Circle overriding the draw method.
    """
    def draw(self):
        print("Drawing a Circle.")


class Square(Shape):
    """
    Subclass Square overriding the draw method.
    """
    def draw(self):
        print("Drawing a Square.")


class Duck:
    def quack(self):
        print("Quack, quack!")


class Person:
    def quack(self):
        print("I am mimicking a duck: Quack!")


def make_it_quack(entity):
    """
    Demonstrates Python's 'Duck Typing' (Dynamic Polymorphism).
    It doesn't check the type/inheritance, only if the object has the required interface.
    """
    entity.quack()


class Calculator:
    """
    Demonstrates simulating Method Overloading (Static Polymorphism).
    Python does not support true method overloading by default. We simulate it
    using default arguments or variable-length arguments (*args, **kwargs).
    """
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        return a + b


class Vector:
    """
    Demonstrates Operator Overloading (Static Polymorphism on operators).
    Python allows overloading operators using special double underscore (dunder) methods.
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Vector to Vector")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


def main():
    print("--- 1. Run-time Polymorphism (Method Overriding) ---")
    # Method resolution happens dynamically at runtime (late binding)
    shapes = [Circle(), Square(), Shape()]
    for shape in shapes:
        shape.draw()
    print()

    print("--- 2. Duck Typing (Dynamic Polymorphism without Inheritance) ---")
    make_it_quack(Duck())
    make_it_quack(Person())
    print()

    print("--- 3. Static Polymorphism Simulation (Method Overloading) ---")
    calc = Calculator()
    print(f"Adding 2 values: {calc.add(5, 10)}")
    print(f"Adding 3 values: {calc.add(5, 10, 15)}")
    print()

    print("--- 4. Operator Overloading (Dunder Method) ---")
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    result = v1 + v2  # Triggers v1.__add__(v2)
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"Result (v1 + v2): {result}")


if __name__ == "__main__":
    main()
