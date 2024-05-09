# import libary 

from queue import LifoQueue
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

# registration of the patient according to their problem 
name=input(str("enter your name:"))
cid_card=input("enter your citizens identity num:")
ap=input("enter your issue:")
import inquirer
questions = [
  inquirer.List('med_issue',
                message="which department do you want to visit?",
                choices=['Dentist', 'Dermatology', 'Orthopaedic', 'cardiology', 'Psychiatrists', 'Pediatricians','Other'],
            ),
]
answers = inquirer.prompt(questions)
print (answers["med_issue"])

if answers["med_issue"] == "Dentist":
    print("your appointment has been approve ")
elif answers["med_issue"] == "Dermatology":
    print("your appointment has been approve.")
elif answers["med_issue"] == "Orthopaedic":
    print("your appointment has been approve")
elif answers["med_issue"]=="cardiology":
    print("your appointment has been approve")
elif  answers["med_issue"]=="Psychiatrists":
    print("your appointment has been approve")
elif answers["med_issue"]=="Pediatricians":
    print("your appointment has been approve")

    
else:
    print("is there anything we can help with")

from queue import LifoQueue
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

NoOfVisists = int(input("Enter the number of url history: "))
print("Enter URLs to visit:")
for i in range(NoOfVisists):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url
#display the current page 
print(f"current page:{current_page}")
# Go back
while input("Do you want to go back? (yes/no): ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")
    # Go forward
while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")