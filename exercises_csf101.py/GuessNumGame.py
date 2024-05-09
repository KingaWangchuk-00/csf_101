import random 

secret_number = random.randint(1,10)

max_attempts = 3 

def welcome_message():
    print("\nWelcome to the NUmber guessing game! ")
    print(f"You have {max_attempts} attempts to guess the correct number.")

def guess_recursive(attempts_left):
    guess = int(input("\nGuess the number (between 1 and 10): "))

    if guess == secret_number:
        print("Congratulations! You have guessed the correct number! ")

    else:
        print(f"Wrong guess. Attempts left {attempts_left -1}")
        if attempts_left > 1:
            guess_recursive(attempts_left - 1)
        else:
            print(f"\nSorry, you couldn't guess the number. The correct number is {secret_number}. ")

welcome_message()
guess_recursive(max_attempts)

print(f"Memory address of the secret number {secret_number} is: {id(secret_number)}")
    