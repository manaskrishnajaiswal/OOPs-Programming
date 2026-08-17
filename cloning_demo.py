import copy

# Nested reference class
class Address:
    def __init__(self, city: str):
        self.city = city


# Standard Class demonstrating default copy/deepcopy behavior
class StandardPerson:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address


# Custom Class demonstrating customized shallow/deep cloning behavior
class CustomPerson:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    # Custom __copy__ hook called by copy.copy(obj)
    def __copy__(self):
        print("  -> Custom __copy__ hook triggered.")
        # Returns a new Person but shares the exact same address reference (shallow)
        return CustomPerson(self.name, self.address)

    # Custom __deepcopy__ hook called by copy.deepcopy(obj)
    def __deepcopy__(self, memo):
        print("  -> Custom __deepcopy__ hook triggered.")
        # Recursively copies the address object. 
        # The 'memo' dictionary prevents infinite loops in cyclic references.
        new_address = copy.deepcopy(self.address, memo)
        return CustomPerson(self.name, new_address)


def main():
    print("--- 1. Standard Shallow vs. Deep Cloning ---")
    addr = Address("Mumbai")
    original = StandardPerson("Rahul", addr)

    # Standard shallow copy
    shallow_clone = copy.copy(original)

    # Standard deep copy
    deep_clone = copy.deepcopy(original)

    print(f"Original Person address ID: {id(original.address)}")
    print(f"Shallow Clone address ID:   {id(shallow_clone.address)} (Shared reference)")
    print(f"Deep Clone address ID:      {id(deep_clone.address)} (Independent reference)")
    print()

    print("--- 2. Mutating Nested Attributes ---")
    print(f"Initial State -> Original: {original.address.city}, Shallow: {shallow_clone.address.city}, Deep: {deep_clone.address.city}")
    
    # Mutating nested reference using shallow clone
    shallow_clone.address.city = "New Delhi"
    print(f"After Shallow Mutation -> Original: {original.address.city}, Shallow: {shallow_clone.address.city}, Deep: {deep_clone.address.city}")

    # Mutating nested reference using deep clone
    deep_clone.address.city = "Bangalore"
    print(f"After Deep Mutation -> Original: {original.address.city}, Shallow: {shallow_clone.address.city}, Deep: {deep_clone.address.city}")
    print()

    print("--- 3. Custom Cloning Behavior Hooks ---")
    custom_addr = Address("Chennai")
    custom_original = CustomPerson("Amit", custom_addr)

    print("Triggering copy.copy():")
    custom_shallow = copy.copy(custom_original)

    print("Triggering copy.deepcopy():")
    custom_deep = copy.deepcopy(custom_original)


if __name__ == "__main__":
    main()
