"""
Multiple Inheritance - Inheriting from Multiple Parent Classes
"""

class Person:
    """First parent class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

class Teacher:
    """Second parent class"""
    def __init__(self, subject, experience):
        self.subject = subject
        self.experience = experience
    
    def teach(self):
        return f"Teaching {self.subject}"
    
    def get_qualification(self):
        return f"Qualified to teach {self.subject}"

class Student:
    """Third parent class"""
    def __init__(self, student_id, grade):
        self.student_id = student_id
        self.grade = grade
    
    def study(self):
        return f"Studying in grade {self.grade}"
    
    def get_student_info(self):
        return f"Student ID: {self.student_id}"

class TeachingAssistant(Person, Teacher, Student):
    """Class inheriting from multiple parents"""
    def __init__(self, name, age, subject, experience, student_id, grade, supervisor):
        # Initialize all parent classes
        Person.__init__(self, name, age)
        Teacher.__init__(self, subject, experience)
        Student.__init__(self, student_id, grade)
        self.supervisor = supervisor
        self.duties = []
    
    def add_duty(self, duty):
        self.duties.append(duty)
    
    def perform_duties(self):
        if self.duties:
            return f"Performing: {', '.join(self.duties)}"
        return "No duties assigned"
    
    def get_all_info(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Subject: {self.subject}
        Experience: {self.experience} years
        Student ID: {self.student_id}
        Grade: {self.grade}
        Supervisor: {self.supervisor}
        Duties: {', '.join(self.duties) if self.duties else 'None'}
        """

# Testing
print("=== MULTIPLE INHERITANCE ===\n")

ta = TeachingAssistant(
    name="Alex Chen",
    age=24,
    subject="Python Programming",
    experience=2,
    student_id="STU2024001",
    grade=12,
    supervisor="Dr. Smith"
)

# Using methods from all parent classes
print(ta.introduce())           # From Person
print(ta.teach())                # From Teacher
print(ta.study())                 # From Student
print(ta.get_student_info())     # From Student
print(ta.get_qualification())    # From Teacher

# Using TeachingAssistant specific methods
ta.add_duty("Grade assignments")
ta.add_duty("Help students")
print(ta.perform_duties())

print(ta.get_all_info())

# Method Resolution Order (MRO)
print(f"\nMethod Resolution Order:")
for i, cls in enumerate(TeachingAssistant.__mro__):
    print(f"  {i}: {cls.__name__}")