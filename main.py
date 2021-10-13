import random

# Hard Questions
hard_questions = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Easy Questions
easy_questions = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Hard Answers
hard_answers = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Easy Answers
easy_answers = ["1", "2", "3", "4", "5", "6", "7", "8"]

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


def randomizer():
    questions_amount = len(questions) - 1
    randomized_number = random.randint(0, questions_amount)
    return[questions[randomized_number], answers[randomized_number]]

while len(questions) > 0:
    randomized = randomizer()
    print(randomized[0])
    print(randomized[1])
    questions.remove(randomized[0])
    answers.remove(randomized[1])