#Python Concession Stand Program

def shopping_menu():
    # Menu with items and their respective prices
    menu = {
        "pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25
    }

    cart = []  # List to store selected items
    total = 0  # Variable to store the total cost of the order

    # Display the menu
    print("--------MENU--------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")  # Prints each item with its price
    print("--------------------")

    # Main loop to allow the user to select items
    while True:
        # Ask the user to select an item or quit by entering 'q'
        food = input("Select an item (q to quit): ").lower()

        # If the user enters 'q', break the loop and stop adding items
        if food == "q":
            break
        # Check if the selected food is in the menu
        elif menu.get(food) is not None:
            cart.append(food)  # Add the selected item to the cart
        else:
            # Inform the user if the item is not found in the menu
            print("Item not found in the menu. Please choose a valid option.")

    # Display the order summary
    print("\n----- YOUR ORDER -----")
    for food in cart:
        # Add the price of each food item to the total
        total += menu.get(food)
        # Print the selected food items
        print(food, end=" ")

    # Print a blank line for better formatting
    print()

    # Display the final total, formatted to two decimal places
    print(f"Total is: ${total:.2f}")

# Call the function to execute the menu selection process
shopping_menu()