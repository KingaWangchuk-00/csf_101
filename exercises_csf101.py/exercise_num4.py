students_list = []
students_dict = {}

def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    print("Student information added successfully!")




def search_student():
    name = input("Enter student's name to search: ")
    if name in students_dict:
        print("Student found!")
        print("Name:", name,"Age:", students_dict[name]['age'],"Grade:", students_dict[name]['grade'])
        print("Age:", students_dict[name]['age'])
        print("Grade:", students_dict[name]['grade'])
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student's name to remove: ")
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully!")
    else:
        print("Student not found.")


option = int(input("'1.add_student\n 2.search_student\n 3.remove_student\n enter your choice:"))
def goto_function(option):
    if option == 1:
        add_student()
    elif option == 2:
        search_student()
    elif option == 3:
        remove_student()
    else:
        print("Invalid option")
       


goto_function(option)

