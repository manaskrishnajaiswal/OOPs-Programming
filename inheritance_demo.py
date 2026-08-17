class SchoolMember:
    """
    Parent class (superclass) representing a member of a school.
    """
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id

    def display_info(self):
        print(f"School Member -> Name: {self.name}, ID: {self.member_id}")


# 1. Single Inheritance
class Student(SchoolMember):
    """
    Subclass representing a Student. Inherits directly from SchoolMember.
    Demonstrates single inheritance and method overriding.
    """
    def __init__(self, name: str, member_id: str, grade: str):
        # Call the parent class constructor using super()
        super().__init__(name, member_id)
        self.grade = grade

    # Method Overriding: Redefines display_info for specialized student output
    def display_info(self):
        print(f"Student -> Name: {self.name}, ID: {self.member_id}, Grade: {self.grade}")


# 2. Multilevel Inheritance
class GraduateStudent(Student):
    """
    Subclass representing a Graduate Student. Inherits from Student.
    Demonstrates multilevel inheritance (SchoolMember -> Student -> GraduateStudent).
    """
    def __init__(self, name: str, member_id: str, grade: str, research_topic: str):
        super().__init__(name, member_id, grade)
        self.research_topic = research_topic

    # Method Overriding: Extends the display behavior
    def display_info(self):
        super().display_info()  # Calls Student's display_info
        print(f"  Research Topic: {self.research_topic}")


# 3. Hierarchical Inheritance
class Teacher(SchoolMember):
    """
    Subclass representing a Teacher. Inherits directly from SchoolMember.
    Demonstrates hierarchical inheritance (SchoolMember is parent to both Student and Teacher).
    """
    def __init__(self, name: str, member_id: str, subject: str):
        super().__init__(name, member_id)
        self.subject = subject

    # Method Overriding
    def display_info(self):
        print(f"Teacher -> Name: {self.name}, ID: {self.member_id}, Subject: {self.subject}")


# 4. Multiple Inheritance & The Diamond Problem
class A:
    def process(self):
        print("  Process in class A")


class B(A):
    def process(self):
        print("  Process in class B")
        super().process()


class C(A):
    def process(self):
        print("  Process in class C")
        super().process()


class D(B, C):
    """
    Demonstrates Multiple Inheritance.
    Class D inherits from both B and C. In languages like Java, this is not allowed due to the Diamond Problem.
    In Python, MRO (Method Resolution Order) resolving rules ensure a clean, deterministic execution path.
    """
    def process(self):
        print("  Process in class D")
        super().process()


def main():
    print("--- 1. Single Inheritance & Overriding ---")
    student = Student("Alice", "S101", "10th Grade")
    student.display_info()
    print()

    print("--- 2. Multilevel Inheritance ---")
    grad = GraduateStudent("Bob", "G202", "Graduate", "Quantum Computing")
    grad.display_info()
    print()

    print("--- 3. Hierarchical Inheritance ---")
    teacher = Teacher("Mr. Smith", "T303", "Physics")
    teacher.display_info()
    print()

    print("--- 4. Multiple Inheritance & Diamond Problem Resolution ---")
    print("Executing D.process() which invokes super() chaining:")
    d = D()
    d.process()

    print("\nMethod Resolution Order (MRO) list for D:")
    for index, cls in enumerate(D.__mro__):
        print(f"  [{index}] {cls.__name__}")


if __name__ == "__main__":
    main()
