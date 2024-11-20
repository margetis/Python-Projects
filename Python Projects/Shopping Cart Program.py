#Python Shopping Cart Program

def shopping_cart():
    # Initialize empty lists to store foods and their corresponding prices
    foods = []
    prices = []
    total = 0  # Variable to keep track of the total price

    # Infinite loop to continuously ask for food items and prices
    while True:
        # Ask the user to input a food item (q to quit)
        food = input("Enter a food to buy (q to quit): ")

        # Check if the user wants to quit
        if food.lower() == "q":
            break  # Exit the loop if the user enters 'q'
        else:
            # Ask the user to input the price of the food item
            try:
                price = float(input(f"Enter the price of a {food}: $"))  # Convert the input to float
            except ValueError:
                # Handle the case where the input for price isn't a valid float
                print("Invalid price, please enter a valid number.")
                continue  # Skip to the next iteration of the loop to ask again

            # Add the food item and its price to their respective lists
            foods.append(food)
            prices.append(price)

    # After exiting the loop, print the shopping cart summary
    print("\n----YOUR CART----")  # Display the header for the cart summary

    # Iterate over both the foods and prices lists to print each item and its price
    for i in range(len(foods)):
        print(f"{foods[i]}: ${prices[i]:.2f}")  # Display food and its price, formatted to 2 decimal places

    # Calculate the total price by summing the prices list
    total = sum(prices)

    # Print the total price, formatted to 2 decimal places
    print(f"\nYour total is: ${total:.2f}")


# Call the function to run the shopping cart program
shopping_cart()
