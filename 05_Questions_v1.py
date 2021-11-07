
# Functions

# Select Game Mode
def gamemode():
    # Starts while not loop by defining i as False
    i = False
    while not i:
        # Stores users input on difficulty they would like to select as gamemode and prints options
        gamemode = input("\nWhat difficulty would you like to select? The options are: {} ".format(gamemode_options))
        # This makes it so that any spaces in the code get replaced while also lowering any capitalization.
        gamemode = gamemode.replace(" ", "").lower()

        # Returns users input if they inputted hard
        if gamemode == "hard":
            return gamemode

        # Returns users input if they inputted easy
        elif gamemode == "easy":
            return gamemode

        # Returns users input if they inputted normal
        elif gamemode == "normal":
            return gamemode

        # If user inputs anything other than easy, normal or hard continues loop asking user to input valid inputs
        else:
            print("Please input either {}".format(gamemode_options))

# Hard Questions
hard_questions = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Normal Questions
normal_questions = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Easy Questions
easy_questions = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Hard Answers
hard_answers = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Normal Answers
normal_answers = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Easy Answers
easy_answers = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Defines the difficulty options available
gamemode_options = ["Easy", "Normal", "Hard"]

# Defines the users input as difficulty
difficulty = gamemode()

# Question Selection defines variable dependant on difficulty selected
if difficulty == "hard":
    questions = hard_questions
    answers = hard_answers

elif difficulty == "normal":
    questions = normal_questions
    answers = normal_answers

elif difficulty == "easy":
    questions = easy_questions
    answers = easy_answers

# len defines the amount of questions are left in the list and then this removes each question after being printed
while len(questions) > 0:
    guess = input(questions[0])
    guess = guess.replace(" ", "")
    if guess == answers[0].lower().replace(" ", ""):
        print("Correct")
    else:
        print("Incorrect")
    questions.remove(questions[0])
    answers.remove(answers[0])
