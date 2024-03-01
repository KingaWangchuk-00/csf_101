#force
#promt the user to enter the two value
#learning how to use the condition 

print("select the missing value:")
print("1.Mass(m)")
print("2.Acceleration(a)")
print("3.Force(f)")
missing_value_choice= input("enter the num:")

if missing_value_choice =="1":
    a=float(input("enter acceleration(a):"))
    F=float(input("enter force (f):"))
    m= F/a
    print(f"mass(m)={m}")   # f is the formated string or f_string (f-string, expression specified by {} will be replaced with it's value)
    
elif missing_value_choice == "2":
    m=float(input("enter mass(m):"))
    F=float(input("enter force(F):"))
    a=F/m
    print(f"Acceleration(a)={a}")

elif missing_value_choice =="3":
    m=float(input("enter mass(m):"))
    a=float(input("enter acceleration(a):"))
    F=m*a
    print(f"Force(F)={F}")

else:
    print("invail option selected for the missing value.")

