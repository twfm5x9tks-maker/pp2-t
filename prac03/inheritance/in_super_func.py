"""
Super() Function - Calling Parent Methods
"""

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print(f"Vehicle __init__ called for {brand}")
    
    def start(self):
        return f"{self.brand} {self.model} engine started"
    
    def info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)  # Call parent __init__
        self.doors = doors
        print(f"Car __init__ called for {brand}")
    
    def start(self):
        # Call parent method and extend it
        parent_start = super().start()
        return f"{parent_start} - Ready to drive with {self.doors} doors"
    
    def honk(self):
        return "Beep beep!"

class ElectricCar(Car):
    def __init__(self, brand, model, year, doors, battery_size):
        super().__init__(brand, model, year, doors)
        self.battery_size = battery_size
    
    def start(self):
        return f"🔋 {super().start()} (Electric mode)"
    
    def charge(self):
        return f"Charging {self.battery_size}kWh battery"

# Testing
print("=== SUPER() FUNCTION ===\n")
car = Car("Toyota", "Camry", 2023, 4)
print(car.start())
print(car.info())
print(car.honk())

print("\n" + "="*30 + "\n")
tesla = ElectricCar("Tesla", "Model 3", 2024, 4, 75)
print(tesla.start())
print(tesla.charge())