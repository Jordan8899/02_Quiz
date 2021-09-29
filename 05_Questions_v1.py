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

    elif question == hard_questions[1]:
        print(hard_answers[1])
        print(hard_answers[1])
        del hard_questions[1]
        del hard_answers[1]
        question = random.choice(hard_questions)

    elif question == hard_questions[2]:
        print(hard_answers[2])
        print(hard_answers[2])
        del hard_questions[2]
        del hard_answers[2]
        question = random.choice(hard_questions)

    elif question == hard_questions[3]:
        print(hard_answers[3])
        print(hard_answers[3])
        del hard_questions[3]
        del hard_answers[3]
        question = random.choice(hard_questions)

    elif question == hard_questions[4]:
        print(hard_answers[4])
        print(hard_answers[4])
        del hard_questions[4]
        del hard_answers[4]
        question = random.choice(hard_questions)

    elif question == hard_questions[5]:
        print(hard_answers[5])
        print(hard_answers[5])
        del hard_questions[5]
        del hard_answers[5]
        question = random.choice(hard_questions)

    elif question == hard_questions[6]:
        print(hard_answers[6])
        print(hard_answers[6])
        del hard_questions[6]
        del hard_answers[6]
        question = random.choice(hard_questions)

    elif question == hard_questions[7]:
        print(hard_answers[7])
        print(hard_answers[7])
        del hard_questions[7]
        del hard_answers[7]
        question = random.choice(hard_questions)

    elif question == hard_questions[8]:
        print(hard_answers[8])
        print(hard_answers[8])
        del hard_questions[8]
        del hard_answers[8]
        question = random.choice(hard_questions)
    else:
        print("Fixed")
        quit()

while gamemode == "easy":
    print(random.choice(easy_questions))
    quit()

while gamemode == "timed":
    print(random.choice(timed_questions))
    quit()
