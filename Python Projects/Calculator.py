def calculator():
    # Loop until a valid operator is entered
    while True:
        operator = input("Enter an operator (+, -, *, /): ")  # Asks the user to choose an operator
        if operator in ["+", "-", "*", "/"]:
            break  # Exit loop if a valid operator is entered
        else:
            print("Invalid operator! Please enter one of (+, -, *, /).")

    a = float(input("Enter the 1st number: "))  # Asks the user to choose the 1st number
    b = float(input("Enter the 2nd number: "))  # Asks the user to choose the 2nd number

    if operator == "+":
        result = a + b
        print("Result:", round(result, 3))
    elif operator == "-":
        result = a - b
        print("Result:", round(result, 3))
    elif operator == "*":
        result = a * b
        print("Result:", round(result, 3))
    elif operator == "/":
        if b == 0:  # Checking if the divisor is zero
            while b == 0:
                b = float(input("Error: Division by zero is not allowed! Choose a valid number: "))
            result = a / b
            print("Result:", round(result, 3))
        else:
            result = a / b
            print("Result:", round(result, 3))

# Call the function without needing to pass parameters since they are being asked within the function
calculator()