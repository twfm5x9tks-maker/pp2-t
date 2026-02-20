"""
Class Variables Examples
"""

print("=== CLASS VARIABLES ===\n")

# Example 1: Employee Counter
class Employee:
    company = "TechCorp"
    total_employees = 0
    
    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

print("Example 1:")
e1 = Employee("John")
e2 = Employee("Alice")
print(f"Company: {Employee.company}")
print(f"Total employees: {Employee.total_employees}")

# Example 2: Bank Account
print("\nExample 2:")
class BankAccount:
    bank_name = "Central Bank"
    total_money = 0
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_money += balance

a1 = BankAccount("John", 1000)
a2 = BankAccount("Alice", 2500)
print(f"Bank: {BankAccount.bank_name}")
print(f"Total money in bank: ${BankAccount.total_money}")

# Example 3: Student Grades
print("\nExample 3:")
class Student:
    school = "High School"
    total_students = 0
    
    def __init__(self, name):
        self.name = name
        self.grade = 0
        Student.total_students += 1

s1 = Student("Emma")
s2 = Student("Mike")
print(f"School: {Student.school}")
print(f"Total students: {Student.total_students}")