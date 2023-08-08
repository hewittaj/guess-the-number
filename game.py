import random

DIFFICULTIES = ['easy', 'medium', 'hard']
EASY_GUESSES = 15
MEDIUM_GUESSES = 10
HARD_GUESSES = 5


def get_and_check_guess(number_to_guess, guesses_left):
    """
    Checks if the user guess is the number to guess
    """
    number_guessed = int(input("Make a guess: "))

    if number_guessed == number_to_guess:
        print(f"You got it, the answer was {number_to_guess}")
        return True, guesses_left
    elif number_guessed < number_to_guess:
        print("Too low.")
        guesses_left -= 1
        return False, guesses_left
    else:
        print("Too high.")
        guesses_left -= 1
        return False, guesses_left


def get_difficulty():
    """
    Prompts the user to enter a difficulty
    """
    difficulty = input(
        "Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
    number_of_guesses = 0
    while difficulty not in DIFFICULTIES:
        difficulty = input(
            "Choose a difficulty. Type 'easy', 'medium' or 'hard': ")

    match difficulty:
        case "easy":
            number_of_guesses = EASY_GUESSES
        case "medium":
            number_of_guesses = MEDIUM_GUESSES
        case "hard":
            number_of_guesses = HARD_GUESSES
    return difficulty, number_of_guesses


def run_game():
    """
    Runs the guessing game
    """
    # Variable declarations
    correct_guess = False
    difficulty = ""
    number_to_guess = random.randint(1, 101)

    # Start game
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")

    difficulty, number_of_guesses = get_difficulty()
    print(
        f"You have {number_of_guesses} attempts remaining to guess the number."
    )

    # User guesses number
    while not correct_guess and number_of_guesses > 0:
        correct_guess, number_of_guesses = get_and_check_guess(
            number_to_guess, number_of_guesses)
        if number_of_guesses > 0:
            print(
                f"You have {number_of_guesses} attempts remaining to guess the number."
            )
        if number_of_guesses == 0:
            print("You lose!")
