#Python Credit Card Validator Program

def validate_credit_card(card_number):
    """
    Validates a credit card number using the Luhn algorithm.

    Parameters:
        card_number (str): The credit card number as a string. Can include spaces or hyphens.

    Returns:
        bool: True if the credit card number is valid, otherwise False.
    """
    # Initialize sums for odd and even-positioned digits
    sum_odd_digits = 0
    sum_even_digits = 0

    # Remove any spaces or hyphens from the input
    card_number = card_number.replace("-", "")
    card_number = card_number.replace(" ", "")

    # Reverse the card number for easier processing of odd/even positions
    card_number = card_number[::-1]

    # Process all digits in odd positions (from the right, i.e., every other digit)
    for x in card_number[::2]:
        sum_odd_digits += int(x)

    # Process all digits in even positions
    for x in card_number[1::2]:
        x = int(x) * 2  # Double the digit
        if x >= 10:
            # If doubling results in a two-digit number, add the digits (equivalent to 1 + (x % 10))
            sum_even_digits += (1 + (x % 10))
        else:
            sum_even_digits += x  # If result is single-digit, add it directly

    # Calculate total sum of processed digits
    total = sum_odd_digits + sum_even_digits

    # Return True if valid, otherwise False
    return total % 10 == 0


# Main loop to prompt the user until a valid card number is entered
while True:
    card_number = input("Enter a credit card #: ")
    if validate_credit_card(card_number):
        print("VALID")
        break  # Exit loop if the card is valid
    else:
        print("INVALID. Please try again.")
