#Python Quiz Game

def quiz_game():
    # List of questions
    questions = ("How many elements are in the periodic table?: ",
                 "Which animal lays the largest eggs?: ",
                 "What is the most abundant gas in Earth's atmosphere?: ",
                 "How many bones are in the human body?: ",
                 "Which planet in the solar system is the hottest?: ")

    # Corresponding options for each question
    options = (("A. 116", "B. 117", "C. 118", "D. 119"),
               ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
               ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
               ("A. 206", "B. 207", "C. 208", "D. 209"),
               ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

    # Correct answers corresponding to each question
    answers = ("C", "D", "A", "A", "B")

    guesses = []  # List to store user's guesses
    score = 0  # Variable to store the user's score
    question_num = 0  # Counter for the current question

    # Loop through each question
    for question in questions:
        print("--------------------")
        print(question)  # Display the question

        # Display the options for the current question
        for option in options[question_num]:
            print(option)

        # Input validation to ensure user enters only A, B, C, or D
        while True:
            guess = input("Enter (A, B, C, D): ").upper()  # Get the user's guess and convert it to uppercase
            if guess in ("A", "B", "C", "D"):
                break  # Exit the loop if the input is valid
            else:
                print("Invalid input. Please enter only A, B, C, or D.")

        # Add the valid guess to the list of guesses
        guesses.append(guess)

        # Check if the guess is correct
        if guess == answers[question_num]:
            score += 1  # Increment score if the answer is correct
            print("Correct!")
        else:
            # Display the correct answer if the guess was wrong
            print("Incorrect!")
            print(f"The correct answer is {answers[question_num]}.")

        # Move to the next question
        question_num += 1

    # Display the final results
    print("---------------------")
    print("       RESULTS       ")
    print("---------------------")

    # Show correct answers
    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    # Show user's guesses
    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    # Calculate the final score as a percentage
    score_percentage = int(score / len(questions) * 100)
    print(f"Your final score is {score_percentage}%")


# Call the quiz game function to start the quiz
quiz_game()