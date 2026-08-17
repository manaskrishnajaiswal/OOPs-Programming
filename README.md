# OOPs Programming in Python

Welcome to the **OOPs Programming** repository! This project serves as a starting point for learning Object-Oriented Programming (OOP) concepts, using Python as the core programming language.

## Project Structure

*   [`main.py`](./main.py): A simple Python entry script that prints `Hello World` to the console.
*   [`string_demo.py`](./string_demo.py): Demonstrates standard Python string manipulation and common operations.
*   [`input_example.py`](./input_example.py): Demonstrates console input/output using Python's `input()` function.
*   [`type_casting_demo.py`](./type_casting_demo.py): Demonstrates type conversion between common numerical types.
*   [`constants_demo.py`](./constants_demo.py): Demonstrates constant conventions in Python.
*   [`arrays_demo.py`](./arrays_demo.py): Demonstrates 1D arrays, for loops, and 2D arrays using Python lists.
*   [`conditionals_demo.py`](./conditionals_demo.py): Demonstrates conditional logic (`if`-`elif`-`else`) and `match`-`case` statements.
*   [`loops_demo.py`](./loops_demo.py): Demonstrates `for`, `while`, and simulated `do-while` loops.
*   [`exception_handling_demo.py`](./exception_handling_demo.py): Demonstrates runtime error catching using `try`-`except`-`finally`.
*   [`employee_demo.py`](./employee_demo.py): Demonstrates core OOP concepts (classes, objects, attributes, and behaviors) with a model of an Employee entity.
*   [`bank_account_demo.py`](./bank_account_demo.py): Demonstrates attributes, methods, getters, setters, encapsulation, and error validation using a Bank Account model.
*   [`constructor_demo.py`](./constructor_demo.py): Demonstrates non-parameterized, parameterized, copy-constructor simulation, constructor overloading, and constructor chaining.
*   [`encapsulation_demo.py`](./encapsulation_demo.py): Demonstrates encapsulation (data hiding), name mangling, and state validation in Python.
*   [`access_modifiers_demo.py`](./access_modifiers_demo.py): Demonstrates Public, Protected, and Private access levels (naming conventions and name mangling) in Python.
*   [`inheritance_demo.py`](./inheritance_demo.py): Demonstrates single, multilevel, hierarchical, and multiple inheritance (MRO resolution of the diamond problem) in Python.
*   [`polymorphism_demo.py`](./polymorphism_demo.py): Demonstrates static polymorphism simulation, operator overloading, dynamic polymorphism (overriding), and duck typing in Python.
*   [`abstraction_demo.py`](./abstraction_demo.py): Demonstrates abstract classes, abstract subclass chains, interface simulation, and static methods in Python.
*   [`interface_demo.py`](./interface_demo.py): Demonstrates interface declaration, multiple interfaces, interface inheritance, and loose coupling in Python.
*   [`static_demo.py`](./static_demo.py): Demonstrates class variables, static methods, class methods, and definition-time execution (static block equivalent) in Python.
*   [`nested_classes_demo.py`](./nested_classes_demo.py): Demonstrates static nested classes, non-static inner classes, method-scoped local classes, and anonymous lambda behaviors in Python.
*   [`relationships_demo.py`](./relationships_demo.py): Demonstrates class relationships (Association, Aggregation, and Composition) and nested lifecycle bindings in Python.
*   [`cloning_demo.py`](./cloning_demo.py): Demonstrates shallow copying, deep copying, custom cloning hooks (`__copy__`, `__deepcopy__`), and reference mutation effects in Python.
*   [`generics_demo.py`](./generics_demo.py): Demonstrates generic classes, generic functions, bounded type parameters, Union wildcards, and Python's lack of runtime type enforcement.
*   [`file_handling_demo.py`](./file_handling_demo.py): Demonstrates writing, reading, pathlib properties, context managers, and custom log appending in Python.

## How to Run

Follow these instructions to run the Python scripts locally.

### Prerequisites

*   Python 3.10 or higher installed.

### Execution

Run any of the Python scripts using the python interpreter:

```bash
python main.py
```

Output:
```text
Hello World
```

---

## Introduction to OOP

> [!NOTE]
> **Pre-Requisites**: Before diving deep into OOPs, please note that this learning path is based on the Python programming language due to its readable syntax and wide usage in data science, web development, and scripting. For a quick refresher on language syntax, you can browse the basic demos listed below.

Object-Oriented Programming (OOP) is a programming paradigm (a style of writing code) based on the concept of **objects**, which can contain data and executable code:
*   **Data**: Represented as attributes (often called fields or properties).
*   **Code**: Represented as methods.

Objects are instances of **classes**, which act as blueprints or templates defining the properties (attributes) and behaviors (methods) common to all objects of that type.

---

### Procedural vs. Object-Oriented Programming

| Aspect | Procedural Programming | Object-Oriented Programming (OOP) |
| :--- | :--- | :--- |
| **Approach** | Focuses on a step-by-step sequence of actions. Control flows sequentially. | Focuses on modeling real-world entities as objects with data & behaviors combined. |
| **Data Handling** | Data is globally accessible. High risk of accidental modifications, making maintenance harder. | Data is encapsulated within objects. Access is restricted through methods for better security. |
| **Code Reusability** | Limited reusability. Functions can be reused, but lacks inheritance and polymorphism. | High reusability through inheritance (extending child classes) and polymorphism (generic operations). |
| **Scalability** | Harder to scale; adding features requires editing multiple functions, risking breaking code. | Scales well for large systems; features are added by creating or modifying classes with minimal side-effects. |
| **Modularity** | Structured via functions, but lacks rigorous separation of logic and data. | Structured via classes/objects, facilitating cleaner organization and maintainability. |
| **Real-World Modeling** | Less aligned with real-world entities. Focuses on operations rather than relationships. | Closely mirrors real-world scenarios by representing entities as objects with state and behavior. |

---

### Core Pillars & Advantages of OOP

1.  **Modularity**: Breaking down a complex problem into smaller, manageable, and reusable components (classes).
    *   *Example*: A banking system split into `Account`, `Customer`, and `Transaction` classes.
2.  **Code Reusability**: Extending and reusing existing functionality to reduce duplication and speed up development.
    *   *Example*: A `Vehicle` parent class extended by `Car` and `Bike` classes.
3.  **Scalability**: The ease of introducing new functionality without breaking or altering existing code.
4.  **Security**: Protecting sensitive data by encapsulating attributes inside objects and exposing only necessary interfaces.
    *   *Example*: Restricting direct access to a `self._balance` attribute in a bank account.

#### Real-Life Analogy: A Bank System
*   **Classes**: The templates defining system entities (e.g., `Account`, `Customer`, `Transaction`).
*   **Objects**: Specific instances of those entities (e.g., `Raj's Account`, `John's Transaction`).
*   **Attributes**: The states of entities (e.g., name, balance, account number).
*   **Methods**: Actions that entities perform (e.g., `deposit()`, `withdraw()`, `transfer()`).

#### Why is OOP better for large-scale applications?
OOP is ideal for large-scale systems because it enforces modularity, enabling complex projects to be broken into smaller, decoupled components. Through features like inheritance and polymorphism, it allows developer teams to build scalable, secure, and highly maintainable codebases with minimal disruption to existing functionality.

---

## Python Basics

### 2. Comments
Comments are ignored by the computer. They are for humans to read.

```python
# This is a single line comment

"""
This is a 
multi-line comment (or docstring)
"""
```

### 3. Data Types
Python is dynamically typed but strongly typed. It has several built-in data types to store different values:

| Data Type | Description | Example |
| :--- | :--- | :--- |
| `int` | Integers of arbitrary precision | `my_int = 42` |
| `float` | Double-precision decimals | `my_float = 3.14` |
| `str` | Textual data | `my_string = "Hello"` |
| `bool` | Boolean state | `my_bool = True` |
| `list` | Ordered, mutable sequence | `my_list = [1, 2, 3]` |
| `tuple` | Ordered, immutable sequence | `my_tuple = (1, 2)` |
| `dict` | Key-value pairs | `my_dict = {"key": "val"}` |
| `set` | Unordered collection of unique items | `my_set = {1, 2}` |

### 4. Operators
Operators are special symbols used to perform operations on variables and values.

#### Arithmetic Operators
| Operator | Name | Description |
| :--- | :--- | :--- |
| `+` | Addition | Adds two values. |
| `-` | Subtraction | Subtracts the right operand from the left. |
| `*` | Multiplication | Multiplies two values. |
| `/` | Division | Divides the left operand by the right (returns a float). |
| `//` | Floor Division | Divides the left operand by the right, truncating decimals. |
| `%` | Modulo | Returns the remainder of a division operation. |
| `**` | Exponentiation | Performs power calculation. |

#### Unary Operators & Negation
Unlike Java, Python does not have increment (`++`) or decrement (`--`) operators. Instead, Python uses:
*   Increment/Decrement: `a += 1` / `a -= 1`
*   Negation: `-x`
*   Logical negation: `not flag`

#### Relational Operators
Used to compare two values. They return a boolean result (`True` or `False`).

| Operator | Name | Description |
| :--- | :--- | :--- |
| `==` | Equal to | Checks if two values are equal. |
| `!=` | Not equal to | Checks if two values are not equal. |
| `>` | Greater than | Checks if the left value is greater than the right. |
| `<` | Less than | Checks if the left value is less than the right. |
| `>=` | Greater than or equal to | Checks if the left value is greater than or equal to the right. |
| `<=` | Less than or equal to | Checks if the left value is less than or equal to the right. |

#### Logical Operators
Used to determine the logic between variables or values.

| Operator | Description | Example |
| :--- | :--- | :--- |
| `and` | Returns `True` if both statements are true. | `x > 5 and x < 10` |
| `or` | Returns `True` if at least one of the statements is true. | `x > 5 or x < 2` |
| `not` | Inverts the boolean value. | `not flag` |

#### Assignment Operators
Used to assign values to variables.

| Operator | Name | Description |
| :--- | :--- | :--- |
| `=` | Assignment | Assigns the value on the right to the variable on the left. |
| `+=` | Add and Assign | Adds a value to the variable and assigns the result. |
| `-=` | Subtract and Assign | Subtracts a value from the variable and assigns the result. |
| `*=` | Multiply and Assign | Multiplies the variable by a value and assigns the result. |
| `/=` | Divide and Assign | Divides the variable by a value and assigns the result. |
| `%=` | Modulo and Assign | Assigns the remainder of the division to the variable. |

### 5. Strings
Strings are immutable sequence objects in Python used to store text.

*   **Immutable**: Once created, a `str` object cannot be changed. Modifying it creates a new object in memory.

#### Common String Operations

See the complete runnable implementation in [`string_demo.py`](./string_demo.py):

```python
s1 = "Hello"
arr = ['W', 'o', 'r', 'l', 'd']
s2 = "".join(arr)  # Join char list to string

print(s1 + " " + s2)       # Concatenate: Hello World
print(s1[1])               # Index access: 'e'
print(len(s1))             # Length: 5
print(s1[0:2])             # Slicing (substring): "He"
print(s1 == "Hello")       # Check content equality: True
```

### 6. Input & Output
For retrieving user input from the console, Python provides the built-in `input()` function.

See the complete runnable implementation in [`input_example.py`](./input_example.py):

```python
print("Enter age (int) and name (string) on separate lines:")
try:
    age = int(input())
    name = input()
    print(f"{name} is {age}")
except ValueError:
    print("Invalid input format.")
```

> [!NOTE]
> **What about fast I/O?**
> In Python, `sys.stdin.readline` can be imported from the `sys` module and is faster than standard `input()`. It reads an entire line including the trailing newline character, making it useful for competitive programming.

### 7. Type Casting
Type casting is the process of converting a variable from one data type to another.

*   **Implicit Casting**: Done automatically by the Python interpreter when mixing types (e.g. adding an integer to a float yields a float).
*   **Explicit Casting**: Performed manually using conversion functions like `int()`, `float()`, `str()`, etc.

See the complete runnable implementation in [`type_casting_demo.py`](./type_casting_demo.py):

```python
my_int = 9
my_float = float(my_int)  # Explicit casting: 9.0
heavy_int = int(9.78)     # Explicit casting: 9 (fraction lost)
```

### 8. Constants
Python has no built-in `const` or `final` keyword. We represent constants by naming convention using **UPPERCASE** letters.

See the complete runnable implementation in [`constants_demo.py`](./constants_demo.py):

```python
# Convention: Use UPPERCASE for constants
PI = 3.14
```

### 9. Lists (Arrays)
Python uses mutable sequences called **Lists** to store multiple values (equivalent to arrays).

See the complete runnable implementation in [`arrays_demo.py`](./arrays_demo.py):

```python
scores = [90, 80, 70]
print(len(scores))  # 3
print(scores[0])    # 90

# Iteration
for i in scores:
    print(i)

# 2D Array
matrix = [ [1, 2], [3, 4] ]
```

### 10. Conditional Statements

#### If, Elif, Else
Allows executing code blocks conditionally.

See the complete runnable implementation in [`conditionals_demo.py`](./conditionals_demo.py):

```python
marks = 85
if marks > 90:
    print("A")
elif marks > 80:
    print("B")
else:
    print("C")
```

#### Match-Case Statement (Python 3.10+)
Selects one of many code blocks to be executed, similar to `switch` in other languages.

```python
day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")  # Wildcard pattern (acts as default)
```

### 11. Loops
Loops are used to repeatedly execute a block of code while a specified condition is met.

See the complete runnable implementation in [`loops_demo.py`](./loops_demo.py):

#### For Loop
Iterates over a sequence (e.g. a range, list, or string).
```python
for i in range(5):
    print(i)
```

#### While Loop
Executes as long as the condition remains true.
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

#### Do-While Loop Simulation
Python has no native do-while loop, but it can be simulated using an infinite loop and a break statement:
```python
j = 0
while True:
    print(j)  # Runs at least once
    j += 1
    if j >= 5:
        break
```

### 12. Exception Handling

**Exception Handling** is a mechanism in Python that helps manage runtime errors and maintain the normal flow of a program. An exception is an unwanted or unexpected event that disrupts the standard execution sequence.

See the complete runnable implementation in [`exception_handling_demo.py`](./exception_handling_demo.py).

#### Importance of Exception Handling
*   **Prevents Crashes**: Ensures a single error doesn't terminate the entire process abruptly.
*   **Graceful Recovery**: Allows the application to log errors, report details, or rollback operations safely.
*   **Separates Logic**: Decouples standard business logic from error handling logic.
*   **Cleanup Operations**: Guarantees resource release (e.g., closing files/sockets) using `finally`.

---

#### The Try-Except-Else-Finally Mechanism

Python provides the following blocks for control:
1.  **`try`**: Encapsulates code that may throw an exception.
2.  **`except`**: Catches and handles specific exceptions. Multiple `except` blocks can handle different exception types. *Rule: Catch blocks should be ordered from most specific to most general.*
3.  **`else`**: Run only if **no** exceptions were raised in the `try` block.
4.  **`finally`**: Executed unconditionally (always runs), whether an exception occurred or not. Crucial for resource cleanup.

```python
try:
    arr = [1, 2, 3]
    val = arr[0] / 2
except IndexError:
    print("Error: List index out of bounds.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Operation succeeded, no errors occurred.")
finally:
    print("Block execution complete (cleanup).")
```

---

#### Raising Exceptions & Propagation (`raise`)

In Python, the `raise` keyword is used to manually throw an exception.
*   **Syntax**: `raise ExceptionType("Error Message")`
*   **No `throws` Keyword**: Python does not require you to declare exceptions in a function signature (unlike Java's `throws` keyword). Exceptions automatically propagate up the call stack until caught or causing a crash.

| Feature | `raise` keyword | `throws` declaration (No Python equivalent) |
| :--- | :--- | :--- |
| **Purpose** | Used to explicitly throw an exception. | Java syntax to declare exceptions a method might propagate. |
| **Location** | Inside a block/function body. | In function/method signatures. |
| **Enforcement** | Evaluated dynamically at runtime. | Checked exceptions are checked at compile-time. |

---

#### Custom Exceptions
Custom exceptions let you define application-specific errors. This is achieved by subclassing the built-in `Exception` class:

```python
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise CustomException("This is a custom application error!")
except CustomException as e:
    print(f"Caught: {e}")
```

---

#### Checked vs. Unchecked Exceptions
Unlike Java, **Python does not support Checked Exceptions**. All exceptions in Python are effectively unchecked: the language does not compile-time enforce wrapping operations in try-except blocks or declaring them in signatures. Exceptions are resolved dynamically at runtime.

---

## Core OOP Concepts

This section covers the primary building blocks of Object-Oriented Programming: classes, objects, attributes, behaviors, memory allocation, and lifecycle.

See the complete runnable implementation in [`employee_demo.py`](./employee_demo.py).

### 1. Class
In object-oriented programming, a **Class** is a blueprint or template for creating objects. It defines attributes (data) and methods (functions) that the objects created from the class will have.
*   **Memory**: A class does not occupy memory on its own. It is a structure from which individual objects are instantiated.

For example, consider the `Employee` class blueprint in [`employee_demo.py`](./employee_demo.py):
```python
class Employee:
    def __init__(self):
        self._employee_name = ""
        self._salary = 0.0

    def set_name(self, name: str): ...
    def set_salary(self, salary: float): ...
    def get_salary(self) -> float: ...
```

> [!TIP]
> **Keypoints**:
> *   The `Employee` class acts as a blueprint that defines a set of attributes and methods, providing a logical representation of a real-world employee.
> *   It defines attributes (`_employee_name` and `_salary`) and methods (`set_name`, `set_salary`, `get_salary`), outlining the capabilities of any future employee objects.

---

### 2. Object
An **Object** is an instance of a class. When an object is created from a class, memory is allocated for it, and it holds data as specified by the class. Objects interact with other parts of the program by invoking methods and modifying attributes.

For example, creating and configuring Employee objects in [`employee_demo.py`](./employee_demo.py):
```python
obj1 = Employee()
obj2 = Employee()

obj1.set_name("Raj")
obj1.set_salary(50000.0)

obj2.set_name("Rahul")
obj2.set_salary(60000.0)
```

#### Output
```text
Raj's Salary: 50000.0
Rahul's Salary: 60000.0
```

> [!TIP]
> **Keypoints**:
> *   The class itself does not occupy memory. It is the initialized objects (`obj1` and `obj2`) that consume memory resources.
> *   Objects are isolated. Although `obj1` and `obj2` share the same class blueprint, they are allocated separate regions in memory. Consequently, one object cannot directly access or modify the internal state of another object.
> *   The two instances represent distinct real-world employees (Raj and Rahul).

---

### 3. Attributes & Methods

*   **Attributes (Fields / Properties)**: Represent the data or characteristics of an object. They define the state of the object at any given moment.
    *   *Example*: In `Employee`, the attributes are `_employee_name` and `_salary`.
*   **Methods (Behaviors / Functions)**: Actions or operations that an object of a class can perform. They operate on attributes and define the object's functionality.
    *   *Example*: In `Employee`, the methods are `set_name()`, `set_salary()`, and `get_name()`.

To understand the interaction between attributes and methods, we look at a practical banking scenario.

See the complete runnable implementation in [`bank_account_demo.py`](./bank_account_demo.py).

#### BankAccount Case Study
In a real-world scenario, sensitive data (like the account balance) must be hidden from the outside world to ensure security and prevent unauthorized access. This is achieved by setting the attribute's access level to **private** and using methods to interact with it.

We design a `BankAccount` class with:
*   **Attributes**:
    *   `Name` (String): Storing the name of the account holder.
    *   `Balance` (Float): Storing the account balance. Set to **private** using double underscores `__balance` (invoking Python name mangling) to restrict direct access.
*   **Methods**:
    *   `Check Balance` (`get_balance`): Retrieves the current balance.
    *   `Deposit` (`deposit(amount)`): Adds to the balance after validating that the amount is positive.
    *   `Withdraw` (`withdraw(amount)`): Subtracts from the balance after validating that the amount is positive and that sufficient funds exist.

#### Interacting via Getters & Setters
Getters and setters provide controlled access to private data attributes:
*   **Getters**: Methods used to safely retrieve the value of an attribute (e.g., `get_balance()`).
*   **Setters**: Methods used to safely modify the value of an attribute under validation rules (e.g., `set_owner_name(name)`).

#### Python BankAccount Example

```python
class BankAccount:
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        self._owner_name = owner_name
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance  # Private attribute

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.__balance:
            print("Error: Insufficient funds.")
            return False
        self.__balance -= amount
        return True
```

> [!IMPORTANT]
> **Key Rules for Attributes & Methods**:
> 1.  **Encapsulation**: Mark variables private (with `_` or `__`) and only expose them via public methods (getters/setters) to protect data integrity.
> 2.  **Explicit Initialization**: In Python, all attributes must be explicitly declared and initialized inside the `__init__` constructor.
> 3.  **Method Parameters**: Methods can accept parameters to safely modify the internal state of the object (e.g., `deposit(amount)`).
> 4.  **Error Validation**: Methods must validate inputs (e.g., preventing negative deposit amounts or checking for insufficient balance before withdrawals) to maintain consistent states.

---

### 4. Creation and Deletion of Objects

#### Creation
Objects are instantiated from a class by calling the class name as if it were a function. This executes the `__init__` constructor method and allocates heap memory.
```python
obj = Employee()
```

#### Deletion
Memory cleanup and object destruction depend on the programming language's memory management model:
*   **Python**: Python automatically reclaims memory using reference counting and a cyclic garbage collector. When an object's reference count drops to zero, it is eligible for deletion.
*   **C++**: Requires manual memory management. Objects created on the heap via `new` must be explicitly deleted using the `delete` keyword to avoid memory leaks.

---

### 5. Memory Allocation: Stack vs. Heap

Different programming languages allocate memory for objects and variables using two key regions: Stack memory and Heap memory.

| Feature | Stack Memory | Heap Memory |
| :--- | :--- | :--- |
| **Data Stored** | Local variables, function frame pointers, reference pointers. | Actual object instances and their dynamically bound attributes. |
| **Allocation Style** | Automatic, LIFO (Last-In-First-Out) order when a function is invoked. | Dynamic allocation as objects are constructed. |
| **Lifetime** | Tied to the execution scope of the function. Cleared when the function exits. | Exists until dereferenced and reclaimed by Python's Garbage Collector. |
| **Access Speed** | Extremely fast. | Slower than stack access due to reference resolution. |

---

### 6. Constructors

A **Constructor** is a special method inside a class that is automatically called when an object of that class is created. Its main purpose is to initialize instance attributes and prepare the object for use.

In Python, the constructor is defined using the `__init__()` method.

See the complete runnable implementation in [`constructor_demo.py`](./constructor_demo.py).

> [!TIP]
> **Keypoints**:
> *   The constructor is always named `__init__`.
> *   It must include `self` as the first parameter, which refers to the current object instance.
> *   It has no return type and should not explicitly return any value.
> *   If no constructor is defined, Python automatically provides a default constructor.

#### Default Constructor Behavior
If you do not define an `__init__()` method, Python provides a default one that creates the object but initializes no attributes. 
*   **Variable Scoping**:
    *   *Instance Variables*: Defined inside methods (usually `__init__`) using `self.name`. If accessed before assignment, Python raises an `AttributeError`.
    *   *Local Variables*: Variables defined inside methods without `self`. If accessed before assignment, Python raises an `UnboundLocalError`.
    *   *Class Variables*: Shared variables declared directly in the class body.
    *   *Parent Constructor*: Not called automatically in inherited classes. Must be called using `super().__init__()`.

---

#### Types of Constructors

1.  **Non-parameterized Constructor**: Does not take any additional arguments besides `self`.
    ```python
    class NonParameterizedDemo:
        def __init__(self):
            self.message = "Hello World"
    ```
2.  **Parameterized Constructor**: Takes arguments along with `self` to customize object state upon creation.
    ```python
    class ParameterizedDemo:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
    ```
3.  **Copy Constructor**: Python does not support native copy constructors. However, they can be implemented manually by defining a constructor that takes another instance of the same class, or by using Python's `copy` module.
    ```python
    class CopyConstructorDemo:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

        @classmethod
        def from_existing(cls, existing):
            return cls(existing.name, existing.age)
    ```

---

#### Constructor Overloading Simulation
Python does not support traditional constructor overloading. A class can have only one `__init__()` method. However, we can simulate overloading using:
*   **Default parameter values**: Making arguments optional.
*   **Alternative constructors**: Using class methods (`@classmethod`) to provide multiple initialization strategies.

```python
class OverloadingDemo:
    def __init__(self, name: str = "Guest", age: int = 18):  # Default parameters
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):  # Alternative constructor
        from datetime import datetime
        calculated_age = datetime.now().year - birth_year
        return cls(name, calculated_age)
```

---

#### Constructor Chaining
Constructor chaining is a technique where a child class constructor delegates part of its initialization to the parent class constructor using `super().__init__()`.

*   **Reusability**: Reuses common initialization logic without code duplication.
*   **Method Resolution Order (MRO)**: Python follows MRO to lookup constructors in multiple inheritance scenarios.
*   **Best Practice**: Placing `super().__init__()` at the start of the child constructor ensures the parent attributes are initialized first.

```python
class ParentClass:
    def __init__(self, brand: str):
        self.brand = brand

class ChildClass(ParentClass):
    def __init__(self, brand: str, model: str):
        super().__init__(brand)  # Constructor Chaining
        self.model = model
```

---

## Encapsulation (Data Hiding in Python)

**Encapsulation** is a fundamental concept in Object-Oriented Programming (OOP) where the internal implementation details (data and logic) of an object are hidden from the outside world. It is the process of bundling the object's data (attributes) and methods (functions) together into a single unit (a class).

The primary goal of encapsulation is to protect the internal state of an object from unintended external modifications and to provide controlled access to it.

See the complete runnable implementation in [`encapsulation_demo.py`](./encapsulation_demo.py).

> [!NOTE]
> **Key Concept**:
> Encapsulation enforces data hiding, ensuring that attributes within a class are not directly accessible to external code. Instead, it provides **getter and setter** methods to access and modify these attributes. By making attributes private, the class retains full control over how data is accessed and modified, enforcing business logic and validation rule checks.

---

### Importance of Encapsulation

1.  **Data Security**: Sensitive data is hidden from external manipulation and can only be modified in a controlled, validated manner.
2.  **Flexibility & Maintenance**: If the internal class implementation needs to change (e.g. data structure storage change), you can modify it without breaking external client code as long as the public method interfaces remain unchanged.
3.  **Modular Code**: Bundling related data and behaviors together promotes clean, modular, and organized code that is easier to read and maintain.
4.  **Improved Debugging & Testing**: With controlled access, you can isolate and validate method behaviors (like getters and setters) independently.
5.  **Reduced Complexity**: By hiding complex internal workings and exposing only clean interfaces, encapsulation reduces the cognitive load on developers using the class.

---

### Key Takeaways in Python

*   **Private Data**: In Python, prefixing attributes with double underscores (e.g., `__balance`) triggers **name mangling**, making them private. This restricts direct access from outside the class:
    ```python
    try:
        print(acc.__balance)  # Raises AttributeError
    except AttributeError:
        pass
    ```
*   **Convention-Based**: Note that Python's private attributes are based on naming mechanism changes rather than hard language restrictions. You can technically access mangled properties using `_ClassName__attributeName` (e.g. `_EncapsulatedBankAccount__balance`), although doing so is strongly discouraged.
*   **Getter and Setter Interfaces**: Public getter and setter methods (such as `get_balance()` and `deposit(amount)`) serve as controlled entry points.
*   **State Integrity & Validation**: Setters/Modifiers can run validation checks (e.g., checking that deposit amount is positive) before altering attributes.

```python
class EncapsulatedBankAccount:
    def __init__(self, holder_name: str, balance: float):
        self.__holder_name = holder_name
        self.__balance = balance  # Private attribute

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float):
        if amount <= 0:
            print("Validation Error: Deposit amount must be positive.")
            return
        self.__balance += amount
```

> [!IMPORTANT]
> **Design vs. Mechanism**:
> Encapsulation is a **design principle** (the goal of hiding details and grouping data/logic). Access modifiers (private, public, protected attributes) and getter/setter methods are the **mechanisms** used to achieve encapsulation.

---

## Access Modifiers

**Access Modifiers** define the visibility and accessibility of classes, methods, variables, and other members of a program. They control which parts of the program can interact with a particular component, ensuring code safety and enforcing encapsulation boundaries.

See the complete runnable implementation in [`access_modifiers_demo.py`](./access_modifiers_demo.py).

### Purpose of Access Modifiers
1.  **Encapsulation**: Protects sensitive variables and methods from accidental external modification.
2.  **Controlled Access**: Empowers developers to define public APIs while keeping structural details hidden.
3.  **Security**: Enhances security and data integrity by restricting access to authorized classes.
4.  **Flexibility**: Permits controlled code sharing via inheritance hierarchy.

---

### Access Levels in Standard OOP vs. Python

Most Object-Oriented languages (like Java) support four distinct access levels. While Python does not enforce access levels at the compiler level, it uses **naming conventions** to simulate them:

#### 1. Public Access Modifier
*   **OOP definition**: Globally accessible from anywhere in the program.
*   **Python implementation**: Any attribute or method without a prefix is public by default.
*   *Key Points*: Used for APIs, public helpers, and universally available properties.
*   *Example*: `self.name` or `def display_name(self):`

#### 2. Protected Access Modifier
*   **OOP definition**: Accessible only within the same package and by subclasses.
*   **Python implementation**: Prefixed with a **single underscore** (e.g., `_serial_number`). This is a convention warning other developers that the member is protected; Python does not prevent external access.
*   *Key Points*: Promotes inheritance by allowing child classes access, while alerting outside code to avoid direct interaction.
*   *Example*: `self._serial_number` or `def _display_protected(self):`

#### 3. Private Access Modifier
*   **OOP definition**: Accessible only within the declaring class.
*   **Python implementation**: Prefixed with a **double underscore** (e.g., `__engine_code`). This triggers **name mangling**, altering the identifier internally (e.g., `_ClassName__attributeName`) to prevent direct external access and avoid naming collisions in subclasses.
*   *Key Points*: Enforces compile-time/runtime protection for highly sensitive states; subclass access is blocked.
*   *Example*: `self.__engine_code` or `def __display_private(self):`

#### 4. Default Access (Package-Private)
*   **OOP definition**: Accessible only within classes of the same package (Java's default).
*   **Python implementation**: Python doesn't have a direct equivalent of packages in the Java compilation sense, but internal module/package conventions typically use a single underscore prefix at the module level.

---

### Comparison of Scopes in OOP

| Access Modifier | Class Internal | Package / Module | Subclass (Inherited) | World (External) | Python Naming Mechanism |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Public** | ✔️ Yes | ✔️ Yes | ✔️ Yes | ✔️ Yes | Default (no prefix) |
| **Protected** | ✔️ Yes | ✔️ Yes | ✔️ Yes | ❌ No (discouraged) | Single underscore: `_var` |
| **Default** | ✔️ Yes | ✔️ Yes | ❌ No | ❌ No | (Package-private concept) |
| **Private** | ✔️ Yes | ❌ No | ❌ No | ❌ No | Double underscore: `__var` |

*Note: In Python, `✔️` and `❌` for protected and private represent the **design convention** rather than rigid compiler limits.*

---

## Inheritance

**Inheritance** is a core Object-Oriented Programming (OOP) concept that allows a class (subclass/child class) to inherit attributes and methods from another class (superclass/parent class). It promotes code reuse, reduces redundancy, and establishes hierarchical relationships.

See the complete runnable implementation in [`inheritance_demo.py`](./inheritance_demo.py).

### Core Components
*   **Parent Class (Superclass)**: The class whose properties and methods are inherited. It serves as a base template (e.g., `SchoolMember`).
*   **Subclass (Child Class)**: The class that inherits from the parent. It can reuse inherited attributes/methods, extend functionality, or override behaviors (e.g., `Student` or `Teacher`).

---

### Types of Inheritance in Python

1.  **Single Inheritance**: A child class inherits from a single parent class. (One-to-One relationship)
    *   *Example*: `Student` inherits from `SchoolMember`.
2.  **Multilevel Inheritance**: A child class inherits from another child class, creating an inheritance chain.
    *   *Example*: `GraduateStudent` inherits from `Student`, which inherits from `SchoolMember`.
3.  **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class. (One-to-Many relationship)
    *   *Example*: Both `Student` and `Teacher` inherit from `SchoolMember`.
4.  **Multiple Inheritance**: A class inherits from more than one parent class.
    *   *Python Support*: Python natively supports multiple inheritance (unlike Java, which restricts multiple inheritance using classes to avoid ambiguity).

---

### Advantages of Inheritance
*   **Reusability**: Write code once in a parent class and reuse it across multiple subclasses.
*   **Modularity**: Cleanly separates concerns into specific classes.
*   **Extensibility**: Add or alter features in a child class without touching the parent class.
*   **Maintainability**: Centralizing shared logic makes debugging and updates easier.

---

### Important Inheritance Concepts

#### 1. Method Overriding
Method overriding allows a subclass to provide a specific implementation of a method already defined in its parent class. This supports runtime polymorphism.
*   **Rules**:
    *   The overriding method in the child class must have the same name and parameter list.
    *   The child class method's access level cannot be more restrictive than the parent class's method.
    *   Python dynamically overrides methods at runtime.

#### 2. The `super()` Function
Used to access parent class members and constructors. In constructors, `super().__init__()` chains initialization.
*   *Best Practice*: Call `super().__init__()` at the start of the child constructor to ensure parent fields are set up first.

#### 3. Method Overloading vs. Overriding

| Aspect | Method Overloading | Method Overriding |
| :--- | :--- | :--- |
| **Definition** | Same method name with different parameter signatures. | Child class redefining a parent class method with the same signature. |
| **Inheritance** | Does not require inheritance; occurs within a single class. | Requires inheritance; occurs between parent and child classes. |
| **Parameters** | Must have different parameter lists (number, type, or order). | Must have the exact same parameter list. |
| **Python Support** | Python does not natively support overloading; simulated via default arguments. | Fully supported dynamically. |

---

### Multiple Inheritance & The Diamond Problem

The **Diamond Problem** occurs when a class inherits from two parent classes that both override a method from a common ancestor. This creates ambiguity: which parent's method should the child run?

```
      [Ancestor A]
       /        \
   [Parent B]  [Parent C]
       \        /
       [Child D]
```

*   **Java's Approach**: Disallows multiple inheritance with classes (only allowed via interfaces) to prevent conflicts.
*   **Python's Approach**: Natively allows multiple inheritance. It resolves ambiguity using **Method Resolution Order (MRO)** via the C3 Linearization algorithm. MRO dictates a deterministic, linear search path for methods:
    ```python
    # For class D(B, C):
    print(D.__mro__) 
    # Output path: D -> B -> C -> A -> object
    ```

---

## Polymorphism

**Polymorphism** is a key Object-Oriented Programming (OOP) concept describing the ability of a single entity (such as a method, operator, or object) to behave differently in different contexts. The term comes from the Greek words for "many forms."

See the complete runnable implementation in [`polymorphism_demo.py`](./polymorphism_demo.py).

---

### Types of Polymorphism: OOP Theory vs. Python

Standard OOP defines two main forms of polymorphism:

#### 1. Compile-Time Polymorphism (Static Polymorphism)
*   **OOP Theory**: The correct method invocation is resolved by the compiler at compile-time based on the method's signature (parameter types, count, and order). This is achieved through **Method Overloading**.
    *   *Examples*: `add(int, int)` vs. `add(double, double)`.
*   **Python Perspective**: Because Python is a dynamically typed, interpreted language, it does not resolve method binding during a compile phase. It does not natively support traditional method overloading (the last defined method overrides any previous ones). However, Python simulates static overloading behavior using:
    *   **Default parameter values**: Making some parameters optional.
    *   **Variable-length arguments**: Using `*args` and `**kwargs`.
    *   **Operator Overloading**: Python natively supports operator overloading using special "dunder" methods (e.g., `__add__`), letting standard operators (`+`, `*`, etc.) behave differently depending on the operand types.

#### 2. Run-Time Polymorphism (Dynamic Polymorphism)
*   **OOP Theory**: The method invocation is resolved dynamically during program execution. This is achieved via **Method Overriding** and **Dynamic Method Dispatch**, where the virtual machine decides which method to run based on the actual object type at runtime (late binding).
*   **Python Perspective**: Python natively and extensively supports dynamic polymorphism.
    *   **Method Overriding**: Subclasses can redefine parent methods to customize behavior.
    *   **Duck Typing**: *"If it walks like a duck and quacks like a duck, it's a duck."* Python doesn't require subclasses to inherit from a common base class to act polymorphically. As long as an object implements the expected method interface, Python invokes it dynamically.

---

### Comparison of Polymorphism Forms

| Property | Static Polymorphism (Overloading) | Dynamic Polymorphism (Overriding) |
| :--- | :--- | :--- |
| **Binding Time** | Compile-Time (Early Binding) | Run-Time (Late Binding / Dynamic Dispatch) |
| **Mechanism** | Method Overloading, Operator Overloading | Method Overriding, Duck Typing |
| **Speed** | Faster execution (binding already resolved) | Slower execution (requires runtime lookup) |
| **Requirements** | Methods share a name but differ in parameters | Classes have inheritance (or share method names in Duck Typing) |

---

## Abstraction

**Abstraction** is a fundamental Object-Oriented Programming (OOP) concept that focuses on hiding the complex internal implementation details of a system and exposing only the essential features or interface. It allows users to focus on *what* an object does rather than *how* it does it.

See the complete runnable implementation in [`abstraction_demo.py`](./abstraction_demo.py).

### Key Features of Abstraction
1.  **Hiding Implementation Details**: Simplifies interactions by shielding external code from complex internal logic.
2.  **Abstract Methods**: Declared in an abstract blueprint but contain no body/implementation. Subclasses are required to provide their concrete implementation.
3.  **Concrete Methods**: Fully implemented methods within an abstract base class. Subclasses inherit these behaviors directly but can override them if necessary.

---

### Methods of Achieving Abstraction: Standard OOP vs. Python

Most compile-time languages (like Java) achieve abstraction using explicit abstract classes and interfaces. Python, being dynamic, simulates and implements these concepts differently:

#### 1. Abstract Classes
*   **OOP Theory**: A class that cannot be instantiated directly and is meant to be subclassed. It can contain both abstract and concrete methods.
*   **Python implementation**: Created using the built-in `abc` (Abstract Base Class) module. A class inherits from `abc.ABC` and designates abstract methods using the `@abstractmethod` decorator.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name  # Abstract classes can have constructors

    @abstractmethod
    def sound(self):
        pass  # Unimplemented abstract method

    def eat(self):
        print(f"{self.name} is eating.")  # Concrete method
```

#### 2. Interfaces
*   **OOP Theory**: A contract defining only abstract method signatures that implementing classes must fulfill.
*   **Python implementation**: Python does not have a native `interface` keyword. It achieves interface behavior using **multiple inheritance** of Abstract Base Classes (ABCs) containing exclusively abstract methods.

```python
class SwimmerInterface(ABC):
    @abstractmethod
    def swim(self):
        pass
```

---

### Static and Default Methods

#### 1. Static Methods
Static methods belong to the class namespace rather than any specific instance of the class.
*   **Python implementation**: Declared using the `@staticmethod` decorator.
*   *Key Points*: They are invoked directly on the class itself and do not accept `self` or `cls` arguments, meaning they cannot access or modify instance or class state.
*   *Example*:
    ```python
    class MathHelper:
        @staticmethod
        def add(x, y):
            return x + y
    ```

#### 2. Default Methods (in Interfaces)
*   **OOP Theory**: Introduced in Java 8 to add concrete implementations to interfaces without breaking existing implementing classes.
*   **Python implementation**: Because Python interfaces are implemented using normal classes (ABCs), any method in a Python ABC that is not decorated with `@abstractmethod` is implicitly a concrete method with default implementation that subclasses inherit automatically.

---

### Important Questions & Key Takeaways

#### Q1: Can an abstract class extend another abstract class?
**Yes.** An abstract class can inherit from another abstract class. The child abstract class inherits all parent abstract methods but is **not** required to implement them. The final concrete subclass that ends the inheritance chain must implement all accumulated abstract methods before it can be instantiated.

```python
class WingedAnimal(Animal, ABC):
    @abstractmethod
    def fly(self):
        pass
```

#### Q2: Can an abstract class have a constructor and can we create an instance of it?
*   **Instantiation**: **No.** You cannot instantiate an abstract class directly. If you attempt to instantiate a class inheriting from `ABC` that contains unimplemented `@abstractmethod` decorators, Python raises a `TypeError`.
*   **Constructor**: **Yes.** An abstract class can define an `__init__` constructor. Subclasses call this constructor using `super().__init__()` to initialize shared attributes upon child instantiation.

---

## Interfaces

An **Interface** specifies a contract of behaviors that an implementing class must fulfill. It defines *what* a class should do without specifying *how* it should do it.

In Python, interfaces are typically represented using Abstract Base Classes (ABCs) that declare abstract methods without providing implementations.

See the complete runnable implementation in [`interface_demo.py`](./interface_demo.py).

---

### Core Questions & Key Design Rules

#### Q1: Can an interface have instance variables?
**No.** In standard Object-Oriented design, interfaces represent pure behavior contracts and cannot hold state. All variables declared within an interface are implicitly `public`, `static`, and `final` (constants).
*   *Python Perspective*: When designing an ABC to act as an interface, it should not define an `__init__` constructor or instance attributes.

#### Q2: Can interfaces have constructors?
**No.** Since interfaces cannot maintain object state (i.e. no instance variables) and cannot be instantiated directly, they do not have constructors. However, any concrete class implementing the interface can declare its own constructor to initialize its state.

#### Q3: Can a class implement multiple interfaces?
**Yes.** A class can implement multiple interfaces. This is a crucial feature in languages like Java that restrict multiple inheritance using classes to avoid ambiguity, yet allow multiple inheritance via interfaces.
*   *Python Perspective*: In Python, this is achieved by inheriting from multiple ABC interface classes:
    ```python
    class Duck(Flyable, Swimmable):
        def fly(self): ...
        def swim(self): ...
    ```

---

### Benefits of Interfaces

1.  **Multiple Inheritance**: Combines behavior requirements from different sources into a single concrete class.
2.  **Strict Contracts**: Establishes a uniform method signature requirement, ensuring design consistency across different classes.
3.  **Loose Coupling**: Programming to an interface rather than a concrete class makes systems flexible and easy to maintain.
    *   *Example*: A client function can accept any interchangeable `PaymentGateway` interface implementation (such as `PayPalGateway` or `StripeGateway`) without being coupled to a specific payment provider.

---

### Interface Inheritance
Interfaces can inherit from other interfaces. When an interface inherits another, it adds new methods to the contract defined by the parent interface. Implementing classes must fulfill the combined set of methods.

```python
class AnimalInterface(ABC):
    @abstractmethod
    def eat(self):
        pass

class MammalInterface(AnimalInterface, ABC):
    @abstractmethod
    def walk(self):
        pass  # MammalInterface inherits eat() and adds walk()
```

---

## Understanding "Static" in Python

Python does not have a dedicated `static` keyword like Java or C++. However, Python natively provides the same architectural patterns using **class variables**, **static methods**, and **module-level variables**. These are used when you want data or behavior to belong to the class (or module) rather than a specific object instance.

See the complete runnable implementation in [`static_demo.py`](./static_demo.py).

---

### Static variables vs. Class variables in Python

In Python, a **Class Variable** is defined directly inside the class body (outside methods). It is shared across all instances of a class, acting as the direct equivalent of Java's static variables.

```python
class Counter:
    count = 0  # Class variable (shared among all objects)

    def __init__(self):
        Counter.count += 1  # Increments shared counter
```

#### Module-Level "Static" Variables
In Python, a module is loaded once per process. Therefore, variables declared at the module level (outside any class or function) behave like "static globals". This is commonly used for shared configuration and global constants.

---

### Static Methods (`@staticmethod`) vs. Class Methods (`@classmethod`)

Python distinguishes between helper behaviors that don't need class access and those that do:

#### 1. Static Methods
Declared using the `@staticmethod` decorator. It behaves like a normal utility function placed inside the class namespace.
*   **Signatures**: Does not receive `self` or `cls` parameters automatically.
*   **Access**: Cannot access instance variables or class variables directly unless an object/class reference is explicitly passed as an argument.
*   *Example*:
    ```python
    class MathUtils:
        @staticmethod
        def add(a, b):
            return a + b
    ```

#### 2. Class Methods
Declared using the `@classmethod` decorator.
*   **Signatures**: Receives the class type `cls` automatically as the first parameter.
*   **Access**: Can inspect and modify class variables or instantiate class objects.
*   *Example*:
    ```python
    class Counter:
        count = 0

        @classmethod
        def reset_count(cls):
            cls.count = 0
    ```

---

### Static Blocks Equivalent in Python

Python has no native static initializer blocks (`static {}` in Java). However, Python has a strict rule: **The class body is executed once when the class is defined (load-time).**

Any code written directly inside the class body (outside methods) runs at definition time. This can be leveraged for one-time static setup:

```python
class Example:
    print("Class body executed (one-time initialization).")  # Runs once at load time
    value = 10
```

---

### Advantages of Static Members in Python

1.  **Shared State**: Class variables act as a single source of truth shared among all instances.
2.  **Utility Methods**: `@staticmethod` is ideal for placing standalone helper methods within the relevant class namespace.
3.  **Namespace Organization**: Groups related utility behaviors under a single class namespace.
4.  **One-Time Setup**: Definition-time class-body execution handles one-time resource initialization.

---

## Inner Classes (Nested Classes)

In Python, an **Inner Class** (or Nested Class) is a class defined entirely inside the body of another class. This allows you to logically group helper classes that are only relevant to the outer class context, improving organization and readability.

See the complete runnable implementation in [`nested_classes_demo.py`](./nested_classes_demo.py).

---

### Core Patterns in Python

Unlike Java, Python does not enforce strict access control (no private package restrictions) and does not automatically bind a nested object instance to its outer object instance.

#### 1. Static Nested Class Equivalent
*   **OOP Concept**: Independent nested classes that do not require an outer instance.
*   **Python Perspective**: Python nested classes are static/independent by default. They can access outer class variables if referenced explicitly via the outer class name.
*   *Example*:
    ```python
    class OuterClass:
        static_var = 100

        class StaticNestedClass:
            def display(self):
                print(OuterClass.static_var)  # Explicit reference
    ```

#### 2. Non-Static Inner Class Equivalent
*   **OOP Concept**: Nested classes that can implicitly access members of the outer class instance.
*   **Python Perspective**: There is no implicit binding to an outer object. If an inner class needs data from an outer instance, the outer instance must be passed and stored explicitly (usually during initialization).
*   *Example*:
    ```python
    class OuterClass:
        def __init__(self):
            self.instance_var = 42

        class InnerClass:
            def __init__(self, outer):
                self.outer = outer  # Explicit outer binding

            def display(self):
                print(self.outer.instance_var)
    ```

#### 3. Local Inner Classes (Method Scope)
*   **OOP Concept**: Classes declared inside methods/functions, restricted to that function's scope.
*   **Python Perspective**: You can declare classes inside any method. They are local to that function and are ideal for small, temporary helper objects that shouldn't pollute the module/global namespace.
*   *Best Practice*: Pass enclosing values explicitly via the local class constructor rather than relying on closures implicitly.

#### 4. Anonymous Inner Class Equivalent
*   **OOP Concept**: One-time custom helper implementations.
*   **Python Perspective**: Achieved using:
    *   **Lambda functions**: Lightweight anonymous functions (for simple, single-expression operations).
    *   **Inline helper classes**: Declared on the fly when multiple methods or states are required.

---

### Key Advantages & Design Use Cases

Nested classes in Python are primarily **organizational** tools:
1.  **Logical Grouping**: Organizes helper classes (like database configurations, API schemas, or validator templates) under their primary parent classes.
2.  **Prevents Namespace Clutter**: Restricts helper types to the class namespace instead of cluttering the module scope.
3.  **Self-Documenting Code**: Groups related schemas directly where they are used (e.g., nesting a `Config` class inside a `DatabaseConnection` class).

---

## Relationships Between Classes

In Object-Oriented Programming, classes act as the structural blueprints of a system. The interactions and associations between these classes define how objects collaborate to represent real-world processes.

These interactions are categorized into three major relationships based on ownership, coupling strength, and object lifecycle bindings.

See the complete runnable implementation in [`relationships_demo.py`](./relationships_demo.py).

---

### 1. Association
**Association** is the most general relationship between two classes. It represents a semantic connection or link where objects of one class interact with objects of another.
*   **Cardinality**: Connections can be one-to-one (e.g., `Person` and `Passport`), one-to-many (e.g., `Teacher` and `Student`s), or many-to-many (e.g., `Student` and `Course`s).
*   **Implementation**: Done by passing references or keeping collections of references inside objects.

---

### 2. Aggregation
**Aggregation** is a specialized, weaker form of association representing a **"Has-A"** or **"Whole-Part"** relationship.
*   **Lifecycle**: The related objects can exist independently. Destroying the container ("whole") does not affect the contained ("part") objects.
*   **Ownership**: The container class references the part class, but does not own or manage its lifespan.
*   *Example*: A `Department` aggregates `Employee`s. If the department is closed down, the employees still exist independently in memory.

---

### 3. Composition
**Composition** is a restrictive, strong form of aggregation representing a **"Part-Of"** relationship.
*   **Lifecycle**: The lifecycles of the related objects are tightly coupled. The contained objects cannot exist outside the lifecycle of the container. If the container ("whole") is destroyed, the parts are automatically destroyed.
*   **Ownership**: The container class owns and manages the lifecycle of the part class.
*   *Example*: A `House` is composed of `Room`s. If the house is demolished, the rooms cease to exist. In Python code, this is modeled by instantiating the `Room` objects inside the `House` class constructor rather than passing them in.

---

### Dual / Multiple Relationships
In complex software architectures, a class can participate in multiple relationships simultaneously. For example:
*   A `Library` class has an **aggregation** relationship with a `Book` class (books can be removed from a library and still exist).
*   The `Book` class has a **composition** relationship with a `Chapter` class (chapters cease to exist if the book is destroyed).

---

### Relationship Comparison Matrix

| Aspect | Association | Aggregation | Composition |
| :--- | :--- | :--- | :--- |
| **Relationship Type** | General connection | Weak "Has-A" (Whole-Part) | Strong "Part-Of" (Co-dependent) |
| **Ownership** | None (independent links) | Container references but does not own | Container owns lifecycle of parts |
| **Lifecycle Independence** | Both classes exist independently | Contained class can exist independently | Contained class is destroyed with container |
| **Real-world Example** | `Student` and `Course` | `Employee` and `Department` | `House` and `Room` |

---

## Object Cloning

**Object Cloning** refers to the process of creating an exact copy of an object. The cloned object occupies a separate memory location, allowing developers to inspect or mutate it without directly affecting the original object (with some caveats regarding shallow copying).

See the complete runnable implementation in [`cloning_demo.py`](./cloning_demo.py).

---

### Purpose of Object Cloning
1.  **Efficiency**: Replicating a complex object graph without invoking costly init operations or querying data stores repeatedly.
2.  **State Preservation**: Taking structural snapshot backups of object states (useful for rollback systems or undo/redo behaviors).
3.  **Reducing Coupling**: Preventing multiple components from holding shared references to a mutable object.
4.  **Prototyping**: Enabling objects to act as prototypes, where modifications are made to a cloned variant of a baseline template (Prototype design pattern).

---

### Shallow Cloning vs. Deep Cloning

Python facilitates object cloning using the standard library `copy` module. There are two primary levels of cloning:

#### 1. Shallow Cloning (`copy.copy`)
*   **Mechanism**: Copies the top-level outer object structure but copies the *references* to any nested objects or structures inside it.
*   **Implication**: The original and the cloned object share references to the same nested mutable attributes (e.g. lists, dicts, custom objects). If you modify a nested mutable attribute on the clone, the original object will also reflect this mutation.
*   *Example*:
    ```python
    import copy
    cloned_obj = copy.copy(original_obj)
    ```

#### 2. Deep Cloning (`copy.deepcopy`)
*   **Mechanism**: Recursively copies the outer object as well as all nested objects and references in its entire object graph.
*   **Implication**: Creates a fully independent copy. Modifying nested attributes on the cloned object will have no impact whatsoever on the original.
*   *Example*:
    ```python
    import copy
    cloned_obj = copy.deepcopy(original_obj)
    ```

---

### Customizing Cloning Behavior
Python classes can hook into cloning operations by overriding special methods:
*   `__copy__(self)`: Triggered when `copy.copy(obj)` is called. Should return a new shallow copy of the instance.
*   `__deepcopy__(self, memo)`: Triggered when `copy.deepcopy(obj)` is called. The `memo` dictionary tracks already-cloned objects to prevent infinite loops in cyclic graphs. Should return a new deep copy of the instance.

```python
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __copy__(self):
        return Person(self.name, self.address)  # Shares self.address reference

    def __deepcopy__(self, memo):
        # Recursively copies the nested address
        new_address = copy.deepcopy(self.address, memo)
        return Person(self.name, new_address)
```

---

### Cloning Comparison Matrix

| Aspect | Shallow Cloning | Deep Cloning |
| :--- | :--- | :--- |
| **Copies Outer Object** | ✔️ Yes | ✔️ Yes |
| **Copies Nested Objects** | ❌ No (shares references) | ✔️ Yes (recursively creates separate objects) |
| **Independent Nested Objects?** | ❌ No | ✔️ Yes |
| **Common Tool** | `copy.copy(obj)` | `copy.deepcopy(obj)` |
| **Primary Use Case** | When nested properties are immutable (integers, strings, tuples) and safe to share | When nested properties are mutable (lists, dicts, custom objects) and must be isolated |

---

## Generics in Python

Because Python is a dynamically typed language, it natively allows you to write functions and classes that work with multiple types out of the box. However, Python also supports **Generics** via the standard `typing` module to enable static type analysis (via `mypy` or `pyright`), improve code readability, and prevent unintended bugs before runtime.

See the complete runnable implementation in [`generics_demo.py`](./generics_demo.py).

---

### Key Benefits of Generics
1.  **Static Type Safety**: Allows static type checkers to catch type mismatches before execution.
2.  **Clear Documentation**: Explicates class and method parameter design rules for other developers.
3.  **Code Reusability**: Eliminates the need to duplicate classes or functions to support different types.

---

### Core Concepts

#### 1. Generic Classes
A generic class can store or work with different data types without duplicating class structures. This is achieved by subclassing `Generic` and defining type parameters using `TypeVar`.

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value

    def get(self) -> T:
        return self.value
```

#### 2. Generic Methods / Functions
Generic functions use `TypeVar` variables in their argument and return signatures to associate parameters.

```python
from typing import TypeVar

T = TypeVar("T")

def print_and_return(data: T) -> T:
    print(f"Data: {data}")
    return data
```

#### 3. Bounded Type Parameters
You can restrict a generic type parameter to a class or any of its subclasses using the `bound=` keyword in `TypeVar`. This ensures that you can safely access attributes or methods defined on the bound class.

```python
from typing import TypeVar

class Vehicle:
    def start_engine(self): pass

# V is constrained to be Vehicle or its subclasses
V = TypeVar("V", bound=Vehicle)

def start_ride(vehicle: V) -> None:
    vehicle.start_engine()  # Guaranteed safe call
```

#### 4. Wildcard Simulation
Python simulates wildcards using:
*   `Any`: Accepts any type whatsoever.
*   `Union`: Restricts inputs to one of several specific classes (e.g., `Union[int, str]`).

---

### Runtime Behavior & The "Type Erasure" Analogy

It is critical to note that **Python type hints are not enforced at runtime by the interpreter.**
*   At runtime, type annotations behave similarly to Java's **Type Erasure** because the Python virtual machine ignores type hints during execution.
*   For instance, declaring `box = Box[int](10)` will still allow you to call `box.set("a string")` during execution without raising a runtime error. Enforcing these constraints at runtime requires manual validation checks (e.g., using `isinstance()`).

---

## File Handling

**File Handling** is the process of reading from and writing to files to store and retrieve data persistently on disk. This is a crucial concept in software development for managing persistent configurations, logging diagnostic logs, and recording long-term data files.

See the complete runnable implementation in [`file_handling_demo.py`](./file_handling_demo.py).

---

### Importance of File Handling in OOP
Integrating File Handling within Object-Oriented designs allows objects to persist state, write structural system logs (logging), and read environmental variables or configuration schemas (configuration management).

---

### Built-in File Operations & Modes
Python uses the built-in `open(file, mode)` function to handle file operations. Common file opening modes include:
*   `"r"`: **Read Mode** (Default). Opens a file for reading; raises `FileNotFoundError` if the file doesn't exist.
*   `"w"`: **Write Mode**. Opens a file for writing; creates the file if it doesn't exist, and **truncates (overwrites)** all existing contents if it does.
*   `"a"`: **Append Mode**. Opens a file for appending data; creates the file if it doesn't exist, and writes new data at the end of the file.
*   `"x"`: **Exclusive Creation**. Creates the file, but fails and raises `FileExistsError` if the file already exists.
*   `"b"`: **Binary Mode**. Used for reading/writing binary data (like images or compiled bytes).
*   `"t"`: **Text Mode** (Default). Opens in standard text format.

---

### Checking File Metadata Properties
The standard library modules `pathlib` and `os` provide clean, object-oriented file properties checks:

```python
from pathlib import Path

p = Path("example.txt")
if p.exists():
    print(f"Name: {p.name}")
    print(f"Size: {p.stat().st_size} bytes")
    print(f"Absolute Path: {p.resolve()}")
```

---

### Context Manager (Resource Management)
Python uses the **`with` statement** as a context manager for handling file buffers. It guarantees that the file stream is automatically and safely closed when execution exits the block, even if runtime exceptions are raised. This behaves similarly to Java's **try-with-resources** statement.

```python
# Context manager handles opening/closing automatically
with open("example.txt", "r") as reader:
    for line in reader:
        print(line.strip())
```

---

### Common File Handling Issues

1.  **`FileNotFoundError`**: Raised when attempting to open a non-existent file in read (`"r"`) mode. Avoided by checking `path.exists()` beforehand.
2.  **`PermissionError`**: Raised when writing to files with insufficient system privileges (e.g., system files or write-protected directories).
3.  **Resource Leaks**: Failing to close files. Avoided by exclusively using `with` context managers.
4.  **Encoding Conflicts**: Different platforms write files in different text formats. *Best Practice: Always specify the encoding explicitly (e.g., `open("file.txt", "w", encoding="utf-8")`).*

---

## Summary
We covered the fundamental building blocks of Python:

*   **Structure**: Functions, entry scripts using `__main__` checker, and class structures.
*   **Data**: Native dynamic types, lists, dictionaries, constants, and strings.
*   **Logic**: Operators, conditional if-elif-else statements, and match-case.
*   **Control**: Loops (`for` ranges, `while`, and simulated do-while loops).
*   **Safety**: Exception handling via `try-except-finally` blocks.

Practice writing and executing these snippets in their respective demo files to get comfortable with Python syntax!
