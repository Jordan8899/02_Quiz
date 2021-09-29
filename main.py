import random

question = ["1", "2"]
x = random.randint(0, 1)
while question:
    print(question[x])

    if question[x] == question[0]:
        print("Question 1")
        del question[x]
        x = random.randint(0, 1)

    elif question[x] == question[1]:
        print("Question 2")
        x = random.randint(0, 1)
