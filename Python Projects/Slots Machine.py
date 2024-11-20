#Python Slots Machine
import random


def spin_now():
    """
    Spins the slot machine and returns a row of three random symbols.

    Returns:
        list: A list of three symbols chosen randomly from the predefined set.
    """
    symbols = ['🍒', '🍉', '🍋', '⭐', '💰']
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    """
    Prints the row of symbols in a formatted way.

    Parameters:
        row (list): A list containing three symbols to display as the result of a spin.
    """
    print("*************")
    print(" | ".join(row))
    print("*************")


def get_payout(row, bet):
    """
    Calculates the payout based on the symbols in the row and the bet amount.

    Parameters:
        row (list): A list containing three symbols.
        bet (int): The amount bet by the player.

    Returns:
        int: The payout amount if there is a win, otherwise 0.
    """
    if row[0] == row[1] == row[2]:  # Check if all three symbols match
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
        elif row[0] == '💰':
            return bet * 20
    return 0


def place_bet(balance):
    """
    Prompts the player to enter a valid bet amount.

    Parameters:
        balance (int): The player's current balance.

    Returns:
        int: The valid bet amount.
    """
    while True:
        bet = input("Place your bet amount: ")

        # Check if input is a valid integer
        if not bet.isdigit():
            print("Please enter a valid bet amount.")
            continue

        bet = int(bet)

        # Check if bet is within balance and greater than zero
        if bet > balance:
            print("Insufficient funds. Please enter a bet within your balance.")
        elif bet <= 0:
            print("Bet must be greater than 0.")
        else:
            return bet  # Return valid bet amount


def play_round(balance):
    """
    Executes a single round of the slot game.

    Parameters:
        balance (int): The player's current balance.

    Returns:
        int: The updated balance after the round.
    """
    print(f"Current balance is ${balance}")

    # Place a valid bet
    bet = place_bet(balance)

    # Deduct bet from balance
    balance -= bet

    # Spin the slot machine and print the result
    row = spin_now()
    print("Spinning...\n")
    print_row(row)

    # Calculate payout and update balance
    payout = get_payout(row, bet)
    if payout > 0:
        print(f"You won ${payout}!")
    else:
        print("Sorry, you lost this round.")

    # Add payout to balance
    return balance + payout


def slot_machine_game():
    """
    Main function to run the slot machine game.
    Handles game setup, rounds, and game termination.
    """
    balance = 100  # Starting balance

    print("*************************")
    print(" Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 ⭐ 💰")
    print("*************************")

    # Main game loop
    while balance > 0:
        balance = play_round(balance)  # Play a single round and update balance

        # Ask if player wants to play again
        while True:
            play_again = input("Would you like to play again? (y/n): ").lower()
            if play_again in ("y", "n"):
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if play_again == "n":
            break

    # Game over message
    print("********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")


# Run the game if this file is executed
if __name__ == "__main__":
    slot_machine_game()