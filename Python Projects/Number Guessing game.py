#Python Guessing Game
import random

def number_guessing_game():
    # Set the range for the number to guess
    lowest_num = 1
    highest_num = 100

    # Generate a random number between the lowest and highest numbers
    answer = random.randint(lowest_num, highest_num)

    guesses = 0  # Counter for the number of guesses
    is_running = True  # Flag to keep the game running

    # Introduction to the game
    print("Python Number Guessing Game")
    print(f"Select a number between {lowest_num} and {highest_num}")

    # Main game loop
    while is_running:
        # Prompt the user for their guess
        guess = input("Guess a number: ")

        # Check if the input is a valid digit
        if guess.isdigit():
            guess = int(guess)  # Convert the input to an integer
            guesses += 1  # Increment the number of guesses

            # Check if the guess is out of the defined range
            if guess < lowest_num or guess > highest_num:
                print("That number is out of range")
                print(f"Please select a number between {lowest_num} and {highest_num}")
            # If the guess is too low
            elif guess < answer:
                print("Too low! Try again!")
            # If the guess is too high
            elif guess > answer:
                print("Too high! Try again!")
            # If the guess is correct
            else:
                print(f"CORRECT! The answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False  # Stop the game when the correct answer is guessed
        else:
            # If the input is not a valid number
            print("Invalid guess")
            print(f"Please select a number between {lowest_num} and {highest_num}")


# Call the function to run the game
number_guessing_game()