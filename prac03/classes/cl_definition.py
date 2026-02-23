class Dog:
    """A simple Dog class"""
    
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize dog attributes"""
        self.name = name    # Instance variable
        self.age = age      # Instance variable
    
    def description(self):
        """Return dog description"""
        return f"{self.name} is {self.age} years old"
    
    def bark(self, sound="Woof!"):
        """Make the dog bark"""
        return f"{self.name} says {sound}"

class Car:
    """Car class with basic attributes"""
    
    wheels = 4  # Class variable
    
    def __init__(self, brand, model, year):
        """Initialize car attributes"""
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Default value
        self.is_running = False
    
    def start_engine(self):
        """Start the car engine"""
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} engine started"
        return "Engine is already running"
    
    def stop_engine(self):
        """Stop the car engine"""
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model} engine stopped"
        return "Engine is already off"
    
    def drive(self, distance):
        """Drive the car for a given distance"""
        if self.is_running:
            self.mileage += distance
            return f"Drove {distance} miles. Total mileage: {self.mileage}"
        return "Cannot drive. Start the engine first!"

def main():
    """Demonstrate class usage"""
    
    # Example 1: Creating Dog objects
    print("=== Dog Class Demo ===")
    dog1 = Dog("Rex", 3)
    dog2 = Dog("Buddy", 5)
    
    print(f"Dog1: {dog1.description()}")
    print(f"Dog2: {dog2.description()}")
    
    # Accessing attributes
    print(f"\n{dog1.name} is {dog1.age} years old")
    print(f"Species: {dog1.species}")  # Access class variable
    
    # Calling methods
    print(dog1.bark())
    print(dog2.bark("Woof woof!"))
    
    # Example 2: Car objects
    print("\n=== Car Class Demo ===")
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("Honda", "Civic", 2023)
    
    print(f"Car1: {car1.brand} {car1.model} ({car1.year})")
    print(f"Car2: {car2.brand} {car2.model} ({car2.year})")
    print(f"All cars have {Car.wheels} wheels")
    
    # Using car methods
    print(f"\n{car1.start_engine()}")
    print(car1.drive(50))
    print(car1.drive(30))
    print(car1.stop_engine())
    
    # Example 3: Modifying object properties
    print("\n=== Modifying Properties ===")
    car2.year = 2024  # Modify instance variable
    car2.color = "Red"  # Add new attribute
    print(f"Updated Car2: {car2.brand} {car2.model} ({car2.year}), Color: {car2.color}")
    
    # Example 4: Deleting properties
    print("\n=== Deleting Properties ===")
    print(f"Before deletion: {hasattr(car2, 'color')}")
    del car2.color
    print(f"After deletion: {hasattr(car2, 'color')}")

if __name__ == "__main__":
    main()