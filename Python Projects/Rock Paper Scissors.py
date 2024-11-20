#Python Rock Paper Scissors Game
import random


def play_rock_paper_scissors():
    # Define the possible choices
    options = ("rock", "paper", "scissors")

    # Game loop to keep running until the player decides to stop
    running = True
    while running:
        # Initialize player's choice as None and get a random choice for the computer
        player = None
        computer = random.choice(options)

        # Loop until player enters a valid choice
        while player not in options:
            player = input("Enter a choice (rock, paper, scissors): ").lower()

        # Display player and computer choices
        print(f"Player: {player}")
        print(f"Computer: {computer}")

        # Determine the outcome of the game
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
                (player == "paper" and computer == "rock") or \
                (player == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")

        # Ask if the player wants to play again
        if not input("Play again? (y/n): ").lower() == "y":
            running = False  # Exit the game loop if the answer is 'n'

    print("Thanks for playing!")


# Call the function to start the game
play_rock_paper_scissors()