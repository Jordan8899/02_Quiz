import random

# Hard Questions
hard_questions = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Easy Questions
easy_questions = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Timed Questions
timed_questions = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Hard Answers
hard_answers = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Easy Answers
easy_answers = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Timed Answers
timed_answers = ["1", "2", "3", "4", "5", "6", "7", "8"]

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
    elif gamemode == "timed":
        i = True
    else:
        print("Please input")
        i = False


# Print Questions based on gamemode
while gamemode == "hard":
    question = random.choice(hard_questions)
    if question == hard_questions[0]:
        print(hard_answers[0])
        print(hard_answers[0])
        del hard_questions[0]
        del hard_answers[0]
        question = random.choice(hard_questions)


while gamemode == "easy":
    print(random.choice(easy_questions))
    quit()

while gamemode == "timed":
    print(random.choice(timed_questions))
    quit()
