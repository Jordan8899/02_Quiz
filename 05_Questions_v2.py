# Setting score and round number up so they work, importing random to allow the creation of randomization
import random
score = 0
round_number = 1
gamemode_options = ["Hard", "Normal", "Easy"]
# Functions

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
hard_questions = ["What is the motto of Hogwarts school for witchcraft and wizarding (in English)?\n",
                  "What ghost is missing from the movies that appears in the books?\n",
                  "What character does JK Rowling share the same birthday with?\n",
                  "Where did JK Rowling get Heromione’s name from?\n",
                  "What character mentioned in the first book / movie was taken from a real person?\n",
                  "What language do spells come from?\n",
                  "What secret character is in the films including fantastic beasts?\n",
                  "What material were the brooms made out of in real life (3 words)?\n"]

# Normal Questions
normal_questions = ["What creatures (plural) forged the Gryffindor sword?\n",
                    "What horcrux is related to the Ravenclaw house?\n",
                    "What did they change Philosopher to in the American version of Harry Potter and the Philosopher’s stone?\n",
                    "What is the name of the main character in Fantastic Beasts and where to find them?\n",
                    "What does Lord Voldermort want to rid the world of?\n",
                    "What position did Harry Potter play in Quidditch?\n",
                    "What position does Ginny Weasley play in Quidditch?\n",
                    "How many times did Gryffindor win the House Cup throughout the books?\n"]

# Easy Questions
easy_questions = ["What is the name of the spell that gave Harry Potter the scar on his forehead?\n",
                  "What house did Harry Potter get sorted into?\n",
                  "What is the REAL name of the Dark Lord?\n",
                  "What teacher at Hogwarts was a werewolf (full name)?\n",
                  "What is the name of the wizardring town outside of Hogwarts?\n",
                  "What character was in love with Lily Potter (full name)?\n",
                  "What subject did Albus Dumbledoor teach before becoming headmaster?\n",
                  "What book number has the highest word count?\n"]

# Hard Answers
hard_answers = ["Never tickle a sleeping dragon",
                "Peeves",
                "Harry Potter",
                "Shakespeare",
                "Nicholas Flamel",
                "Latin",
                "Ginger Witch",
                "Airplane grade titanium"]

# Normal Answers
normal_answers = ["Goblins",
                  "Diadem",
                  "Sorcerer",
                  "Newt Scamander",
                  "Muggles",
                  "Seeker",
                  "Chaser",
                  "1"]
# Easy Answers
easy_answers = ["Avada Kedavra",
                "Gryffindor",
                "Tom Riddle",
                "Remus Lupin",
                "Hogsmeade",
                "Severous Snape",
                "Transfiguration",
                "5"]

# Difficulty selection
difficulty = gamemode()

# Question Selection
if difficulty == "hard":
    questions = hard_questions
    answers = hard_answers
    printed_answer = hard_answers

elif difficulty == "normal":
    questions = normal_questions
    answers = normal_answers
    printed_answer = normal_answers

elif difficulty == "easy":
    questions = easy_questions
    answers = easy_answers
    printed_answer = easy_answers


# Randomized question function
def randomizer():
    questions_amount = len(questions) - 1
    randomized_number = random.randint(0, questions_amount)
    return[questions[randomized_number], answers[randomized_number], printed_answer[randomized_number]]

# Prints said randomized question which is linked to the answer while also adding to the score if correct and adding round number
while len(questions) > 0:
    print("Question {}".format(round_number))
    randomized = randomizer()
    guess = input(randomized[0])
    guess = guess.replace(" ", "").lower()
    if guess == randomized[1].lower().replace(" ", ""):
        print("Correct\n")
        score += 1
    elif guess != randomized[1]:
        print("Incorrect, the correct answer is {}\n".format((randomized[2])))
    round_number += 1
    questions.remove(randomized[0])
    answers.remove(randomized[1])

# Based Response depending on gamemode
if difficulty == "easy":
    true_wizard = "You have been accepted to join Hogwarts school for witchcraft and wizardry"
elif difficulty == "normal":
    true_wizard = "You are as legendary as Harry Potter"
elif difficulty == "hard":
    true_wizard = "You are a true legendary master of magic"

# Score and gamemode based response to how well the user performed in the quiz
if score == 8:
    print("\nCongratulations you got a perfect score {} out of 8 on {} mode. {}".format(score, difficulty, true_wizard))

else:
    print("\nYou got {} out of 8 on the {} difficulty. You did magical".format(score, difficulty))
