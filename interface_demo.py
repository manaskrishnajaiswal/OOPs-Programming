from abc import ABC, abstractmethod

# 1. Pure Interface: Flyable (no constructors or instance state)
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


# 2. Pure Interface: Swimmable (no constructors or instance state)
class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


# 3. Class Implementing Multiple Interfaces
class Duck(Flyable, Swimmable):
    """
    Duck implements both Flyable and Swimmable interfaces,
    providing concrete implementations for their behaviors.
    """
    def fly(self):
        print("Duck is flying over the water.")

    def swim(self):
        print("Duck is swimming in the pond.")


# 4. Interface Inheritance
class AnimalInterface(ABC):
    @abstractmethod
    def eat(self):
        pass


class MammalInterface(AnimalInterface, ABC):
    """
    MammalInterface extends AnimalInterface and adds the walk() requirement.
    """
    @abstractmethod
    def walk(self):
        pass


class Human(MammalInterface):
    """
    Human class implements MammalInterface, thus must provide
    concrete implementations for both eat() and walk().
    """
    def eat(self):
        print("Human is eating food.")

    def walk(self):
        print("Human is walking on two legs.")


# 5. Loosely Coupled System Example
class PaymentGateway(ABC):
    """
    Acts as a contract for payment processing.
    """
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class PayPalGateway(PaymentGateway):
    def process_payment(self, amount: float):
        print(f"Processing ${amount:.2f} payment via PayPal API.")


class StripeGateway(PaymentGateway):
    def process_payment(self, amount: float):
        print(f"Processing ${amount:.2f} payment via Stripe API.")


# Client code depends on the PaymentGateway interface, not concrete classes
def process_checkout(gateway: PaymentGateway, total: float):
    print("Starting checkout...")
    gateway.process_payment(total)


def main():
    print("--- 1. Multiple Interfaces ---")
    duck = Duck()
    duck.fly()
    duck.swim()
    print()

    print("--- 2. Interface Inheritance ---")
    human = Human()
    human.eat()   # Declared in AnimalInterface
    human.walk()  # Declared in MammalInterface
    print()

    print("--- 3. Loosely Coupled Systems ---")
    paypal = PayPalGateway()
    stripe = StripeGateway()
    
    # We can pass any class that implements the PaymentGateway interface
    process_checkout(paypal, 120.00)
    process_checkout(stripe, 75.50)


if __name__ == "__main__":
    main()
