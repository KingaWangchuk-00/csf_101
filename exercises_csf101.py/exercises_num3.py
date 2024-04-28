#a py code to check wheather the person is eligible for the discount for the movie ticket based on their age 

name=input("enter your name:") #asking the person's infomation 
age=int(input("Enter your age:")) #asking the age so that we can figure out wheather the person is eligible for getting a discount 

import inquirer #imported a libary 
stud=[
    inquirer.List('student',
                  message='Are you a student?',
                  choices=['YES','NO'],
                  ),
 ]
answer=inquirer.prompt(stud)
print(answer["student"])

if age <= 12:
        print(f"{name},You are eligible for a discount!")

elif 13 <= age <= 18 and answer == "yes":
    print(f"{name},You are eligible for a discount!")
else:
    print(f"{name},You are not eligible for a discount.")
