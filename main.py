import random

def question():
    questions = ["1", "2"]
    asked = []
    x = random.randint(0, 1)
    if questions[x] not in asked:
        print(questions[x])
    else:
        return

question()
