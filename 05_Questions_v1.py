import random
# Hard Questions
hard_questions = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Easy Questions
easy_questions = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Timed Questions
timed_questions = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Hard Answers
hard_answers = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Easy Answers
easy_answers = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Timed Answers
timed_answers = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Gamemode selection
gamemode = False
while not gamemode:
    gamemode = input("Gamemode? ")
    gamemode = gamemode.strip().lower()
    if gamemode == "hard":
        mode = "hard"
        gamemode = True
    elif gamemode == "easy":
        gamemode = True
        mode = "easy"
    elif gamemode == "timed":
        gamemode = True
        mode = "timed"
    else:
        print("Please input")
        gamemode = False


# Print Questions based on gamemode
if mode == "hard":
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

elif mode == "easy":
    print(random.choice(easy_questions))
    quit()

elif mode == "timed":
    print(random.choice(timed_questions))
    quit()
