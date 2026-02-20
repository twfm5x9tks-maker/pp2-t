"""
Method Overriding - Redefining Parent Methods
"""

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_pay(self):
        """Base method - to be overridden"""
        return self.base_salary
    
    def work(self):
        return f"{self.name} is working"
    
    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
    
    def calculate_pay(self):  # Override
        return self.base_salary + self.bonus
    
    def work(self):  # Override
        return f"{self.name} is managing the team"
    
    def get_role(self):  # Override
        return "Manager"

class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
    
    def calculate_pay(self):  # Override
        overtime_pay = self.overtime_hours * 50
        return self.base_salary + overtime_pay
    
    def work(self):  # Override
        return f"{self.name} is writing code"
    
    def get_role(self):  # Override
        return "Developer"

class Intern(Employee):
    def __init__(self, name, base_salary, supervisor):
        super().__init__(name, base_salary)
        self.supervisor = supervisor
    
    def calculate_pay(self):  # Override
        return self.base_salary / 2  # Half pay for interns
    
    def work(self):  # Override
        return f"{self.name} is learning from {self.supervisor}"
    
    def get_role(self):  # Override
        return "Intern"

# Testing
print("=== METHOD OVERRIDING ===\n")

employees = [
    Manager("Alice", 80000, 10000),
    Developer("Bob", 60000, 20),
    Intern("Charlie", 30000, "Alice")
]

for emp in employees:
    print(f"Role: {emp.get_role()}")
    print(f"  {emp.work()}")
    print(f"  Pay: ${emp.calculate_pay()}")
    print()