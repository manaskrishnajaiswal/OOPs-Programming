# 1. Association (Many-to-Many interaction between Student and Course)
class Student:
    def __init__(self, name: str):
        self.name = name
        self.courses = []

    def enroll_in(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.students.append(self)  # Bi-directional reference linkage


class Course:
    def __init__(self, title: str):
        self.title = title
        self.students = []


# 2. Aggregation (Weak Has-A: Employee and Department)
class Employee:
    def __init__(self, name: str):
        # We prefix attributes with double underscores to reinforce private state
        self.__name = name

    def get_name(self):
        return self.__name


class Department:
    def __init__(self, name: str, employees=None):
        self.__name = name
        # Storing references to externally created employee objects (Aggregation)
        self.__employees = employees if employees else []

    def add_employee(self, employee: Employee):
        self.__employees.append(employee)

    def get_employees(self):
        return [emp.get_name() for emp in self.__employees]

    def get_name(self):
        return self.__name


# 3. Composition (Strong Part-Of: House and Room)
class Room:
    def __init__(self, room_type: str):
        self.__room_type = room_type

    def get_room_type(self):
        return self.__room_type


class House:
    def __init__(self, address: str):
        self.__address = address
        # The house creates and owns the rooms (Composition).
        # Rooms cannot exist outside the lifecycle of their parent House.
        self.__rooms = [Room("Living Room"), Room("Bedroom"), Room("Kitchen")]

    def get_rooms(self):
        return [r.get_room_type() for r in self.__rooms]

    def get_address(self):
        return self.__address


# 4. Combined Multi-Relationship Scenario (Library, Book, and Chapter)
class Chapter:
    def __init__(self, title: str):
        self.title = title


class Book:
    def __init__(self, title: str, chapters_list: list):
        self.title = title
        # COMPOSITION: Book creates and owns its Chapter instances internally
        self.chapters = [Chapter(c_title) for c_title in chapters_list]


class Library:
    def __init__(self, name: str):
        self.name = name
        # AGGREGATION: Library aggregates Book instances (books can exist without a library)
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)


def main():
    print("--- 1. Association (Student & Course) ---")
    alice = Student("Alice")
    bob = Student("Bob")
    python_course = Course("Introduction to Python")

    alice.enroll_in(python_course)
    bob.enroll_in(python_course)

    print(f"Course '{python_course.title}' has enrolled students: {[s.name for s in python_course.students]}")
    print()

    print("--- 2. Aggregation (Department & Employees) ---")
    emp1 = Employee("John Doe")
    emp2 = Employee("Sarah Connor")

    dept = Department("R&D", [emp1, emp2])
    print(f"Department '{dept.get_name()}' contains: {dept.get_employees()}")

    # Delete the department. The employee objects still exist independently in memory
    del dept
    print("Deleted Department instance.")
    print(f"Employee reference check -> {emp1.get_name()} still exists in memory.")
    print()

    print("--- 3. Composition (House & Rooms) ---")
    my_house = House("123 Baker St")
    print(f"House at '{my_house.get_address()}' owns rooms: {my_house.get_rooms()}")
    # If my_house is deleted, the internal Room instances are also garbage collected
    print()

    print("--- 4. Combined Scenario (Library - Book - Chapter) ---")
    # Chapters exist as part-of the Book (Composition)
    book = Book("Design Patterns", ["Chapter 1: Singleton", "Chapter 2: Factory"])
    
    # Book is aggregated inside the Library (Aggregation)
    lib = Library("City Archive")
    lib.add_book(book)

    print(f"Library '{lib.name}' holds: {lib.books[0].title}")
    print(f"Book '{book.title}' has chapters: {[c.title for c in book.chapters]}")


if __name__ == "__main__":
    main()
