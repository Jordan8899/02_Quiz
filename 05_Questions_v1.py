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
gamemode = input("Gamemode? ")
gamemode = gamemode.strip().lower()

# Print Questions based on gamemode
if gamemode == "hard":
    print(random.choice(hard_questions))


elif gamemode == "easy":
    print(random.choice(easy_questions))


elif gamemode == "timed":
    print(random.choice(timed_questions))

else:
    print("Error please input 'hard', 'easy', 'timed'")
