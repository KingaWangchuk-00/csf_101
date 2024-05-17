# Define the parent class Person
class Person:
    #Represents a person with common attributes and behaviors.
    
    def __init__(self, name, age, cid_number):
        #Initializes a Person object with name, age, and CID number.
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        #for walking behavior.
        print(f"{self.name} is walking.")

    def talk(self):
        #for talking behavior.
        print(f"{self.name} is talking.")

    def eat(self):
        #For eating behavior.
        print(f"{self.name} is eating.")

    def sleep(self):
        #For sleeping behavior.
        print(f"{self.name} is sleeping.")


# Define the Student class that inherits from Person
class Student(Person):
    #Represents a student with specific attributes and behaviors.
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        #Initializes a Student object with name, age, CID number, student ID, course, year, and GPA.
        super().__init__(name, age, cid_number) # super()__init__() for inheriting
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        #For studying behavior.
        print(f"{self.name} is studying.")

    def attend_class(self):
        #for attending class behavior.
        print(f"{self.name} is attending class.")

    def write_exam(self):
        #for writing an exam behavior.
        print(f"{self.name} is writing an exam.")


# Define the Teacher class that inherits from Person
class Teacher(Person):
    #Represents a teacher with specific attributes and behaviors.
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        #Initializes a Teacher object with name, age, CID number, subject, salary, department, and designation.
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        #for teaching behavior
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        #for grading students behavior.
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        #for attending a meeting behavior.
        print(f"{self.name} is attending a meeting.")


# Create objects
student1 = Student("kinga", 20, "CID:10304001462", "02230265", "Mechanical Engineering", 1, 3.5)
teacher1 = Teacher("ALU", 35, "CID:10405001645", "Math", 50000, "IT Department", "Professor")

# Test the objects
print("Student:")
student1.walk()
student1.talk()
student1.eat()
student1.sleep()
student1.study()
student1.attend_class()
student1.write_exam()

print("\nTeacher:")
teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()
teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()