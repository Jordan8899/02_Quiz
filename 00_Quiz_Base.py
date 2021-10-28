import random
score = 0
round_number = 1
# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response

    # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please enter either \"Yes\" or \"No\"")

def instructions():
    print("\n***** How to play *****")
    print("")
    print("This quiz is based on the world of Harry Potter. \n"
          "it involves parts of the Harry Potter books and movies as well as fantastic beasts and where to find them.\n"
          "After these instructions you will be asked to select a gamemode, you may type 'easy', 'normal', or 'hard'.\n"
          "After choosing one of the gamemodes you will be given random questions based on the difficulty you selected.\n"
          "You must type all answers correctly spelled.\n"
          "Good luck and have fun")
    print("")
    print("***********************")
    return ""

def randomizer():
    questions_amount = len(questions) - 1
    randomized_number = random.randint(0, questions_amount)
    return[questions[randomized_number], answers[randomized_number], printed_answer[randomized_number]]

def statement_decoration(statement, decoration):

    # How much decoration is on either side of the statement
    sides = decoration * 3

    # Defines where the sides and statement are
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    # Prints the decoration as well as the statement
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

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

# Main routine
print("*** Welcome to the world of magic *** \n")

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

gamemode_options = ["Easy", "Normal", "Hard"]

i = False
while not i:
    gamemode = input("\nWhat difficulty would you like to select? The options are: {}".format(gamemode_options))
    gamemode = gamemode.strip().lower()
    if gamemode == "hard":
        i = True
    elif gamemode == "easy":
        i = True
    elif gamemode == "normal":
        i = True
    else:
        print("Please input either 'easy', 'normal', or 'hard'")
        i = False

# Question Selection
if gamemode == "hard":
    questions = hard_questions
    answers = hard_answers
    printed_answer = hard_answers

elif gamemode == "normal":
    questions = normal_questions
    answers = normal_answers
    printed_answer = normal_answers

elif gamemode == "easy":
    questions = easy_questions
    answers = easy_answers
    printed_answer = easy_answers

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
if gamemode == "easy":
    true_wizard = "You have been accepted to join Hogwarts school for witchcraft and wizardry"
elif gamemode == "normal":
    true_wizard = "You are as legendary as the Harry Potter"
elif gamemode == "hard":
    true_wizard = "You are a true legendary master of magic"

# Score and gamemode based response to how well the user performed in the quiz
if score == 8:
    statement_decoration("Congratulations you got a perfect score {} out of 8 on {} mode. {}".format(score, gamemode, true_wizard), "*")

else:
    statement_decoration("You got {} out of 8 on the {} difficulty. You did okay for a Muggle".format(score, gamemode), "#")
