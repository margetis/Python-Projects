#Python Weight Converter

def weight_converter():
    while True: #Checks if the user gives a valid number
        weight = float(input("Enter your weight: "))
        if weight > 0:
            break
        else:
            print("This number is not valid! Please enter your weight: ")

    while True: #Cheks if the user chooses a valid unit
        unit = input("Kilograms or Pounds? (K or L)")
        if unit in ["K","L"]:
            break
        else:
            print("This unit is not valid! Please enter a valid unit: ")

    if unit == "L": #Converts the weight in Kgs if the user chose "L" as a unit
        weight = weight * 2.205
        print(f"Your weight in Kilograms is: {round(weight, 1)} Kgs")
    else: ##Converts the weight in pounds if the user chose "K" as a unit
        weight = weight / 2.205
        print(f"Your weight in Pounds is: {round(weight, 1)} Lbs")

weight_converter()



