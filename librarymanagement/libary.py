# Initialize empty lists and dictionary
students_list = []
students_dict = {}

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    # Add to list
    students_list.append(name)

    # Add to dictionary
    students_dict[name] = {"age": age, "grade": grade}

    print(f"Student {name} added successfully!")

def search_student():
    name = input("Enter student name to search: ")
    if name in students_dict:
        student_info = students_dict[name]
        print(f"Student Name: {name}")
        print(f"Age: {student_info['age']}")
        print(f"Grade: {student_info['grade']}")
    else:
        print(f"Student {name} not found.")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students_dict:
        # Remove from list
        students_list.remove(name)
        # Remove from dictionary
        del students_dict[name]
        print(f"Student {name} removed successfully!")
    else:
        print(f"Student {name} not found.")

# Main loop
while True:
    print("\nStudent Information Management System")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Remove Student")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        remove_student()
    elif choice == 4:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
