#Python Email Slicer Program
import re

def email_slicer():
    # Regex pattern to validate email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        email = input("Enter Your Email Address: ")
        if re.match(email_pattern, email):  # Check if email matches the pattern
            break
        else:
            print("Invalid email format! Please enter a valid email address.")

    # Slicing the email into username and domain
    index = email.index("@")
    username = email[:index]
    domain = email[index + 1:]  # Skip the '@' symbol

    print(f"Your username is '{username}' and your domain is '{domain}'")


email_slicer()