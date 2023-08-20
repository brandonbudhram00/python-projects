import random

print("Welcome to Guess The Number!")

# User selects what game they want to play 
which_game = int(input("1.Player Guesses or 2.Computer Guess: ")) 

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


def computer_guess(x): 
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Is {guess} too high (H), too low (L), or correct(C)?')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Computer guessed your number, {guess}, correctly!')

if which_game == 1:
    guess(x)
elif which_game == 2:
    computer_guess(x)
