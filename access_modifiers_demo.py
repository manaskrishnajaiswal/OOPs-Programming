class ParentVehicle:
    """
    Demonstrates access levels in Python.
    - Public: name (accessible everywhere)
    - Protected: _serial_number (subclasses / package convention)
    - Private: __engine_code (name mangling, class internal only)
    """
    def __init__(self, name: str, serial_number: str, engine_code: str):
        self.name = name                 # Public: accessible everywhere
        self._serial_number = serial_number  # Protected: subclass convention
        self.__engine_code = engine_code     # Private: name mangling

    def display_public_info(self):
        print(f"Public Method -> Vehicle Name: {self.name}")

    def _display_protected_info(self):
        print(f"Protected Method -> Serial Number: {self._serial_number}")

    def __display_private_info(self):
        print(f"Private Method -> Engine Code: {self.__engine_code}")

    def test_internal_access(self):
        print("--- Inside Parent Class (Internal Access) ---")
        # Internal access works for all levels
        print(f"Public name: {self.name}")
        print(f"Protected _serial_number: {self._serial_number}")
        print(f"Private __engine_code: {self.__engine_code}")
        self.__display_private_info()


class ChildCar(ParentVehicle):
    """
    Subclass demonstrating inheritance access behavior.
    """
    def __init__(self, name: str, serial_number: str, engine_code: str, model: str):
        super().__init__(name, serial_number, engine_code)
        self.model = model

    def test_subclass_access(self):
        print("\n--- Inside Child Class (Subclass Access) ---")
        # Public is accessible
        print(f"Public name inherited: {self.name}")
        # Protected is accessible (by convention)
        print(f"Protected _serial_number inherited: {self._serial_number}")
        self._display_protected_info()
        
        # Private is NOT directly accessible
        try:
            print(self.__engine_code)
        except AttributeError as e:
            print(f"Private __engine_code inherited check failed: {e}")


def main():
    vehicle = ParentVehicle("Generic Car", "SN12345", "ENG9988X")
    vehicle.test_internal_access()

    child = ChildCar("Sport Coupe", "SN67890", "ENG7766Y", "GT-500")
    child.test_subclass_access()

    print("\n--- From External Code (World Access) ---")
    # 1. Public is fully accessible
    print(f"Accessing Public name: {vehicle.name}")
    vehicle.display_public_info()

    # 2. Protected is accessible, but discouraged by convention
    print(f"Accessing Protected _serial_number (discouraged): {vehicle._serial_number}")
    vehicle._display_protected_info()

    # 3. Private is strictly blocked by name mangling
    try:
        print(vehicle.__engine_code)
    except AttributeError as e:
        print(f"Accessing Private __engine_code failed: {e}")

    try:
        vehicle.__display_private_info()
    except AttributeError as e:
        print(f"Accessing Private method __display_private_info failed: {e}")


if __name__ == "__main__":
    main()
