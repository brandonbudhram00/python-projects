import random

print("Welcome to Guess The Number!")

# User will be asked to enter a number that will be used in the function
x = int(input("Please enter a number. The higher the number, the more difficult: "))

def guess(x):
    # A random number will be generated and stored a variable
    random_number = random.randint(1, x) 

    # Initializing the guess as 0
    guess = 0

    while guess != random_number: 
        guess = int(input(f'Guess a number between 1 and {x}: '))

        # If statements to provide feedback for users
        if guess < random_number:
            print('Sorry, guess again. Too low.')

        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Congrats, you have guessed the random number {random_number}')

# running the function using the user-inputed value
guess(x)