# Setting score and round number up so they work, importing random to allow the creation of randomization
import random
score = 0
round_number = 1

# Hard Questions
hard_questions = ["1\n",
                  "2\n",
                  "3\n",
                  "4\n",
                  "5\n",
                  "6\n",
                  "7\n",
                  "8\n"]

# Easy Questions
easy_questions = ["What is the name of the spell that gave Harry Potter the scar on his forehead?\n",
                  "2\n",
                  "3\n",
                  "4\n",
                  "5\n",
                  "6\n",
                  "7\n",
                  "8\n"]

# Hard Answers
hard_answers = ["1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8"]

# Easy Answers
easy_answers = ["Avada Kedavra",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8"]

# Gamemode selection
i = False
while not i:
    gamemode = input("Gamemode? ")
    gamemode = gamemode.strip().lower()
    if gamemode == "hard":
        gamemode = "hard"
        i = True
    elif gamemode == "easy":
        i = True
    else:
        print("Please input")
        i = False

# Question Selection
if gamemode == "hard":
    questions = hard_questions
    answers = hard_answers

elif gamemode == "easy":
    questions = easy_questions
    answers = easy_answers

# Randomized question function
def randomizer():
    questions_amount = len(questions) - 1
    randomized_number = random.randint(0, questions_amount)
    return[questions[randomized_number], answers[randomized_number]]

# Prints said randomized question which is linked to the answer
while len(questions) > 0:
    print("Question {}".format(round_number))
    randomized = randomizer()
    guess = input(randomized[0])
    if guess == randomized[1]:
        print("Correct\n")
        score += 1
    elif guess != randomized[1]:
        print("Incorrect\n")
    round_number += 1
    questions.remove(randomized[0])
    answers.remove(randomized[1])

# Score and gamemode based response to how well the user performed in the quiz
if score == 8:
    print("\nCongratulations you got a perfect score {} out of 8 on the {} difficulty".format(score, gamemode))

else:
    print("\nYou got {} out of 8 on the {} difficulty. You did well".format(score, gamemode))
