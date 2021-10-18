import random
score = 0

# Hard Questions
hard_questions = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n"]

# Easy Questions
easy_questions = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n"]

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

# Randomized question function
def randomizer():
    questions_amount = len(questions) - 1
    randomized_number = random.randint(0, questions_amount)
    return[questions[randomized_number], answers[randomized_number]]

# Prints said randomized question which is linked to the answer
while len(questions) > 0:
    randomized = randomizer()
    guess = input(randomized[0])
    if guess == randomized[1]:
        print("Correct\n")
        score += 1
    elif guess != randomized[1]:
        print("Incorrect\n")
    questions.remove(randomized[0])
    answers.remove(randomized[1])

print("\nYou got {} out of 8".format(score))
