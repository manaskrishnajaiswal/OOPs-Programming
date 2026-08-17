class Employee:
    """
    Represents an Employee entity with attributes and behaviors.
    """
    def __init__(self):
        # Attributes representing state (using internal single underscore convention)
        self._employee_name = ""
        self._salary = 0.0

    # Behaviors (methods representing functionality)
    def set_name(self, name: str):
        self._employee_name = name

    def set_salary(self, salary: float):
        self._salary = salary

    def get_name(self) -> str:
        return self._employee_name

    def get_salary(self) -> float:
        return self._salary


def main():
    # Creating instances (objects) of Employee class
    obj1 = Employee()
    obj2 = Employee()

    # Setting attributes
    obj1.set_name("Raj")
    obj1.set_salary(50000.0)

    obj2.set_name("Rahul")
    obj2.set_salary(60000.0)

    # Displaying details
    print(f"{obj1.get_name()}'s Salary: {obj1.get_salary()}")
    print(f"{obj2.get_name()}'s Salary: {obj2.get_salary()}")


if __name__ == "__main__":
    main()
