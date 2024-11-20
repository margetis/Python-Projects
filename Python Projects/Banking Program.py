#Python Banking Program

def show_balance(balance):
    """
    Displays the current balance.

    Parameters:
        balance (float): The user's current balance.
    """
    print("*******************")
    print(f"Your balance is ${balance:.2f}")
    print("*******************")


def deposit():
    """
    Prompts the user to enter a deposit amount. Keeps asking until a valid amount is entered.

    Returns:
        float: The valid deposit amount.
    """
    while True:
        print("*******************")
        try:
            amount = float(input("Enter the amount to deposit: "))
            print("*******************")

            # Check if the deposit amount is valid
            if amount < 0:
                print("*******************")
                print("That's not a valid amount! Please enter a positive number.")
                print("*******************")
            else:
                return amount  # Return valid deposit amount
        except ValueError:
            print("*******************")
            print("Invalid input! Please enter a number.")
            print("*******************")


def withdraw(balance):
    """
    Prompts the user to enter an amount to withdraw. Keeps asking until a valid amount is entered.

    Parameters:
        balance (float): The user's current balance.

    Returns:
        float: The valid withdrawal amount.
    """
    while True:
        print("*******************")
        try:
            amount = float(input("Enter the amount to withdraw: "))

            # Check if the withdrawal amount is valid and within balance
            if amount > balance:
                print("*******************")
                print("Insufficient funds. Please enter an amount within your balance.")
                print("*******************")
            elif amount < 0:
                print("*******************")
                print("Amount must be greater than 0.")
                print("*******************")
            else:
                return amount  # Return valid withdrawal amount
        except ValueError:
            print("*******************")
            print("Invalid input! Please enter a number.")
            print("*******************")


def banking_program():
    """
    Main function that runs the banking program.
    Handles showing balance, depositing, withdrawing, and exiting.
    """
    balance = 0  # Initial balance
    is_running = True  # Controls the program loop

    while is_running:
        # Display menu options
        print("*******************")
        print("  Banking Program  ")
        print("*******************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*******************")
        choice = input("Enter your choice (1-4): ")

        # Perform action based on user choice
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()  # Add deposit amount to balance
        elif choice == "3":
            balance -= withdraw(balance)  # Subtract withdrawal amount from balance
        elif choice == "4":
            is_running = False  # Exit the loop to end the program
        else:
            print("*******************")
            print("Invalid choice")
            print("*******************")

    # Program end message
    print("*******************")
    print("Thank you! Have a nice day!")
    print("*******************")


# Run the banking program if this file is executed
if __name__ == "__main__":
    banking_program()