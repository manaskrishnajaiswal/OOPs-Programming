# 1. Outer Class containing Static and Non-Static Nested Class equivalents
class OuterClass:
    static_class_var = "Shared Outer Static Data"

    def __init__(self, instance_name: str):
        self.instance_var = f"Instance Data for {instance_name}"

    # 1.1 Static Nested Class Equivalent
    # Python nested classes are independent by default (no implicit outer instance pointer).
    # This aligns directly with Java's static nested classes.
    class StaticNestedClass:
        def display(self):
            # Accessing outer class state explicitly via class name
            print(f"Static Nested -> Accessing outer class variable: {OuterClass.static_class_var}")

    # 1.2 Non-Static Inner Class Equivalent
    # To mimic a Java non-static inner class (which gets direct outer instance access),
    # we must pass the outer instance explicitly to the constructor.
    class InnerClass:
        def __init__(self, outer):
            self.outer = outer  # Store reference to outer instance explicitly

        def display(self):
            # Accessing outer instance members via stored reference
            print(f"Inner Class -> Accessing outer instance variable: {self.outer.instance_var}")


# 2. Local Inner Classes (Classes inside Methods)
class ScopeDemo:
    def run_enclosing_method(self):
        local_value = "Method Scope Variable"

        # Local class definition inside a method
        class LocalInnerClass:
            def __init__(self, value: str):
                self.captured = value  # Capturing value explicitly for clarity

            def display(self):
                print(f"Local Inner Class -> Captured value: {self.captured}")

        # Instantiate and use the class within the method scope
        local_obj = LocalInnerClass(local_value)
        local_obj.display()


# 3. Practical Organizational Grouping (Config Schema Example)
class DatabaseConnection:
    """
    Shows a clean organizational grouping. Nested classes keep the helper configuration 
    logic scoped under the host class, preventing global module namespace clutter.
    """
    def __init__(self, db_name: str, host: str, port: int):
        self.db_name = db_name
        self.config = self.Config(host, port)  # Instantiate nested helper class

    # Nested Config class grouped under DatabaseConnection namespace
    class Config:
        def __init__(self, host: str, port: int):
            self.host = host
            self.port = port

        def get_connection_string(self):
            return f"postgresql://{self.host}:{self.port}"


def main():
    print("--- 1. Static Nested Class Equivalent ---")
    nested_obj = OuterClass.StaticNestedClass()
    nested_obj.display()
    print()

    print("--- 2. Non-Static Inner Class Equivalent ---")
    outer_obj = OuterClass("Server_A")
    inner_obj = OuterClass.InnerClass(outer_obj)
    inner_obj.display()
    print()

    print("--- 3. Local Inner Class (Method Scope) ---")
    scope = ScopeDemo()
    scope.run_enclosing_method()
    print()

    print("--- 4. Anonymous Behavior Equivalent (Lambdas) ---")
    # Lambdas act as lightweight anonymous functions for simple one-off tasks
    square = lambda x: x * x
    print(f"Lambda square of 8: {square(8)}")
    print()

    print("--- 5. Organizational Grouping (Config Schema) ---")
    db = DatabaseConnection("AnalyticsDB", "localhost", 5432)
    print(f"Connected to Database: {db.db_name}")
    print(f"Connection URI: {db.config.get_connection_string()}")


if __name__ == "__main__":
    main()
