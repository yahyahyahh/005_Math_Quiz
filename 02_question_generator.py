import random


for item in range(0, 5):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    operation = "-"
    question = "{} {} {}".format(num_1, operation, num_2)
    answer = eval(question)
    evaluation = answer

    print("question: ", question)
    print("answer", answer)

    if answer == evaluation:
        result = "won"
    else:
        result = "lost"
