class Person:
    def __init__(self, name, age, CID):
        self.name = name
        self.age = age
        self.CID = CID 
        
    def walk(self):
        print(f"{self.name} is walking")
        
    def talk(self):
        print(f"{self.name} is talking")
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
        
class Teacher(Person):
    def __init__(self, name, age, CID, subject, salary, department, designation):
        super().__init__(name, age, CID)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
        
    def teach(self):
        print(f"{self.name} is teaching")
        
    def grade_students(self):
        print(f"{self.name} is grading students")
        
    def attend_meeting(self):
        print(f"{self.name} is attending the meeting")
        
    def __str__(self):
        return f"Teacher: {self.name}, Age : {self.age}, CID : {self.CID}, Subject: {self.subject}, Salary: {self.salary}, Department: {self.department}, Designation: {self.designation}"
        
        
class Student(Person):
    def __init__(self, name, age, CID, Student_ID, course, year, GPA):
        super().__init__(name, age, CID)
        self.Student_ID = Student_ID
        self.course = course
        self.year = year
        self.GPA = GPA
        
    def study(self):
        print(f"{self.name} is studying")
        
    def attend_class(self):
        print(f"{self.name} is attending the class")
        
    def write_exam(self):
        print(f"{self.name} is writing the exam")
        
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, CID: {self.CID}, Student ID: {self.Student_ID}, Course: {self.course}, Year: {self.year}, GPA: {self.GPA}"


teacher = Teacher("Dr.Pema", 34, 123456789, "Mathematics", 45000, "Math Department", "HoD")
student = Student("Nima", 20, 123456789, 2230114, "ECE", "First", 75)
print (teacher)
print (student)