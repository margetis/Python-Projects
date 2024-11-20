def temperature_converter():
    # Ask for temperature input and validate it
    while True:
        try:
            temperature = float(input("Enter a temperature: "))
            break  # Valid temperature entered, exit loop
        except ValueError:
            print("This was not a valid temperature! Please enter a valid number.")

    # Ask for the unit and validate it
    while True:
        unit = input("Is the temperature in Celsius or Fahrenheit? (C or F): ").upper()
        if unit in ["C", "F"]:
            break  # Valid unit entered, exit loop
        else:
            print("This unit is not valid! Please enter a valid unit (C or F).")

    # Perform the conversion
    if unit == "C":
        result = round((9 * temperature / 5) + 32, 1)  # Celsius to Fahrenheit
        print(f"The temperature in Fahrenheit is: {result} °F")
    elif unit == "F":
        result = round((temperature - 32) * 5 / 9, 1)  # Fahrenheit to Celsius
        print(f"The temperature in Celsius is: {result} °C")

# Call the function to run the converter
temperature_converter()