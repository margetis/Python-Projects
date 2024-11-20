#Python Compound Interest Calculator

def compound_interest_calculator():
    # Get the principle amount
    while True:
        principle = float(input("Enter your principle amount: "))
        if principle < 0:
            print("Principle can't be less than zero")
        else:
            break

    # Get the interest rate
    while True:
        rate = float(input("Enter the interest rate (as a percentage): "))
        if rate < 0:
            print("Interest rate can't be less than zero")
        else:
            break

    # Get the time period in years
    while True:
        time = float(input("Enter the time in years: "))
        if time <= 0:
            print("Time can't be less than or equal to zero")
        else:
            break

    # Compound interest formula
    total = principle * pow((1 + rate / 100), time)

    # Output the result
    print(f"Balance after {time} year/s: ${total:.2f}")

# Call the function to execute the calculator
compound_interest_calculator()