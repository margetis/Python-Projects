#Python Alarm Clock

import time
import datetime


def set_alarm(alarm_time):
    """
    Sets a countdown timer to the specified alarm time.
    Continuously displays the remaining time until the alarm goes off.
    """
    # Parse the target alarm time into a datetime object
    target_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()

    print(f"Alarm set for {alarm_time}")
    is_running = True

    while is_running:
        # Get the current datetime
        now = datetime.datetime.now()

        # Combine today's date with the target time for countdown calculation
        alarm_datetime = datetime.datetime.combine(now.date(), target_time)

        # If the alarm time is earlier than the current time, set it for the next day
        if alarm_datetime < now:
            alarm_datetime += datetime.timedelta(days=1)

        # Calculate the remaining time as a timedelta
        remaining_time = alarm_datetime - now

        # Extract hours, minutes, and seconds from the timedelta
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Display the countdown
        print(f"Time left: {hours:02}:{minutes:02}:{seconds:02}")

        # Check if the remaining time has hit zero
        if remaining_time.total_seconds() <= 0:
            print("WAKE UP!")
            is_running = False  # Stop the loop once the alarm rings

        # Wait for 1 second before updating the countdown
        time.sleep(1)


def get_valid_alarm_time():
    """
    Prompts the user to input a valid alarm time in HH:MM:SS format.
    If the input is invalid, the user is asked to try again.
    """
    while True:
        alarm_time = input("Enter the alarm time (HH:MM:SS): ")
        try:
            # Try to parse the input to ensure it's in the correct format
            datetime.datetime.strptime(alarm_time, "%H:%M:%S")
            return alarm_time  # Return valid alarm time
        except ValueError:
            print("Invalid time format. Please enter time in HH:MM:SS format.")


if __name__ == "__main__":
    # Get a valid alarm time from the user
    alarm_time = get_valid_alarm_time()
    # Set the alarm with the validated time
    set_alarm(alarm_time)