#Python Countdown Timer
import time

def countdown_timer():
    # Input validation for time in seconds
    while True:
        try:
            my_time = int(input("Enter a time in seconds: "))
            if my_time < 0:
                print("Time cannot be negative. Please enter a valid positive number.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    # Countdown logic
    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = (x // 60) % 60
        hours = x // 3600
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    print("TIMES UP!")

# Call the function to start the timer
countdown_timer()