#Python Dice Roller Program
import random

def roll_dice(num_of_dice):
    """
    Simulates rolling a specified number of dice and prints their art representation
    along with the total score.
    """
    # Dice art dictionary for each side of the die (1 to 6)
    dice_art = {
        1: ("┌───────────┐",
            "│           │",
            "│     ●     │",
            "│           │",
            "└───────────┘"),

        2: ("┌───────────┐",
            "│ ●         │",
            "│           │",
            "│         ● │",
            "└───────────┘"),

        3: ("┌───────────┐",
            "│ ●         │",
            "│     ●     │",
            "│         ● │",
            "└───────────┘"),

        4: ("┌───────────┐",
            "│ ●       ● │",
            "│           │",
            "│ ●       ● │",
            "└───────────┘"),

        5: ("┌───────────┐",
            "│ ●       ● │",
            "│     ●     │",
            "│ ●       ● │",
            "└───────────┘"),

        6: ("┌───────────┐",
            "│  ●     ●  │",
            "│  ●     ●  │",
            "│  ●     ●  │",
            "└───────────┘")
    }

    # List to store dice rolls and a variable to keep track of the total score
    dice = []
    total = 0

    # Roll each die and store the result in the dice list
    for _ in range(num_of_dice):
        dice.append(random.randint(1, 6))

    # Display the art for each rolled die
    for die in dice:
        for line in dice_art.get(die):
            print(line)
        print()  # Print a blank line between dice for readability

    # Calculate and display the total score
    total = sum(dice)
    print(f"Total: {total}")


# Get the number of dice from the user and call the function
num_of_dice = int(input("How many dice?: "))
roll_dice(num_of_dice)