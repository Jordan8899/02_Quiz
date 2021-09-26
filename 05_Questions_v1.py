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
while mode == "hard":
    random.choice(hard_questions)

    quit()

while mode == "easy":
    print(random.choice(easy_questions))
    quit()

while mode == "timed":
    print(random.choice(timed_questions))
    quit()
