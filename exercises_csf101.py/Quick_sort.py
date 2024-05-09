def factorial(n):
    if n == 1:
        return 1 
    else:
        return(n * factorial(n - 1))
n = 3
print(f"the factorial of {n} is {factorial(n)} ")


    