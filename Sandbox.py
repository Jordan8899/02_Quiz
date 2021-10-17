import random

# sets the questions and answers for the quiz
questions = ["question 1", "question 2", "question 3", "question 4"]
answers = ["answer 1", "answer 2", "answer 3", "answer 4"]


# randomizer function that returns a random question and its answer from the questions and answers lists.
def randomizer():
    # sets a variable (num_of_questions) as the amount of questions in the variable questions - 1
    num_of_questions = len(questions) - 1
    # sets the question number randomly from 0 to the amount of question's in questions - 1
    question_num = random.randint(0, num_of_questions)

    # returns the random question and answer that as picked
    return [questions[question_num], answers[question_num]]


while len(questions) > 0:
    # calls the randomizer function
    random_question_answer = randomizer()
    print(random_question_answer[0])
    print(random_question_answer[1])
    questions.remove(random_question_answer[0])
    answers.remove(random_question_answer[1])

print("out of questions")
