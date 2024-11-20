#Python Hangman Game
import random
from Wordlist import words  # Ensure you have a file named 'Wordlist.py' with a list variable `words`

# Dictionary holding the stages of hangman art based on incorrect guesses
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}


def display_man(wrong_guesses):
    """
    Displays the current state of the hangman based on wrong guesses.

    Parameters:
        wrong_guesses (int): The current count of wrong guesses.
    """
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("************")


def display_hint(hint):
    """
    Displays the hint with correctly guessed letters and underscores for remaining letters.

    Parameters:
        hint (list): The list of guessed letters and underscores.
    """
    print(" ".join(hint))


def display_answer(answer):
    """
    Displays the answer in a spaced format.

    Parameters:
        answer (str): The word being guessed.
    """
    print(" ".join(answer))


def get_valid_guess(guessed_letters):
    """
    Prompts the user for a valid single alphabetical character guess.

    Parameters:
        guessed_letters (set): The set of letters already guessed.

    Returns:
        str: A valid guess from the player.
    """
    while True:
        guess = input("Guess a letter: ").lower()

        # Ensure the input is a single alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
        else:
            return guess  # Return the valid guess


def play_game():
    """
    Main function to run the hangman game. Handles the game flow, player guesses, and win/loss conditions.
    """
    answer = random.choice(words)  # Randomly select a word from the list
    hint = ["_"] * len(answer)  # Initialize the hint with underscores
    wrong_guesses = 0  # Track the number of wrong guesses
    guessed_letters = set()  # Track guessed letters
    is_running = True  # Control the game loop

    while is_running:
        display_man(wrong_guesses)  # Display the current hangman
        display_hint(hint)  # Display the current hint

        # Get a valid guess from the player
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)  # Add the guess to guessed letters set

        # Check if the guess is in the answer
        if guess in answer:
            # Reveal the correctly guessed letters in the hint
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1  # Increment wrong guesses if the guess is incorrect

        # Check win condition (all letters guessed)
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        # Check loss condition (maximum wrong guesses reached)
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


# Run the game if this file is executed
if __name__ == '__main__':
    play_game()
