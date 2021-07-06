import random

# functions go here


# Choice checker - Check for valid answer
def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item), the
        # full name item is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# statement generator - makes statements look nice
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Instructions if the user has never played the game
def instructions():
    print("**** How to Play ****")
    print()
    print("This game is a little math quiz. Choose your preferred level of questions")
    print("and how many questions you'd like to play, or 'Infinite mode'")
    print("Once all your questions have been played, you have the option to see your score.")
    print("Play more than once to challenge your friends to see who's the best!")


# Round Checker - Checks how many questions player wants or Infinite mode
def check_questions():
    while True:
        response = input("How many questions would you like to play?: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def int_check(question, low=None, high=None, quit=None):

    while True:
        quit = "xxx"
        response = input(question)
        if quit == "xxx" and response.lower() == "xxx":
            return response
        elif quit == "" and response.lower() == "":
            return response

        situation = ""

        if low is not None and high is not None:
            situation = "both"
        elif low is not None and high is None:
            situation = "low only"
        try:
            response = int(response)

            # check input is not too high or
            # too low if a both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("please enter a number between "
                          "{} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more "
                          "than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is a integer

        except ValueError:
            print("Please enter an integer")
            continue


# main routine goes here

statement_generator("Welcome to the Math quiz!!", "*")
print()

# Lists of valid responses
yes_no_list = ["yes", "no"]
difficulty_list = ["easy", "hard"]
mq_list = ["+", "-", "*"]
prize_decoration = ""
operation_error = "Please pick from +, -, *"

# ask user if they have played before
choose_instructions = "Have you played before?? "
choose_error = "Please choose yes or no "

played_before = choice_checker(choose_instructions, yes_no_list, choose_error)
if played_before == "no":
    instructions()
print()

summary_choice = "Would you like to see your stats? "
summary_error = "Please choose yes or no "


# Ask user for difficulty (easy / medium / hard)
diff_instructions = "What difficulty would you like to play with?? "
diff_error = "Please choose 'easy' or 'hard' "

diff_choice = choice_checker(diff_instructions, difficulty_list, diff_error)
print("you chose: {}".format(diff_choice))
print()

# Ask user for # of questions then loop...
game_summary = []

questions_asked = 0
questions_wrong = 0

# Ask user for # of questions, <enter> for infinite mode
questions = check_questions()
operation = choice_checker("Pick your operation(+, -, *)", mq_list, operation_error)
print()

end_game = "no"
while end_game == "no":

    # Start game loop

    # questions heading
    print()
    if questions == "":
        heading = "Continuous Mode: Question {}".format(questions_asked + 1)
    else:
        heading = "Question {} of {}".format(questions_asked + 1, questions)
    statement_generator(heading, "*")
    if questions_asked == questions:
        break

    questions_asked += 1

    # for item in range(0, 5):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(10, 20)
    num_3 = random.randint(5, 10)
    num_4 = random.randint(1, 5)

    if diff_choice == "easy":
        question = "{} {} {}".format(num_3, operation, num_4)
        answer = eval(question)

    else:
        question = "{} {} {}".format(num_1, operation, num_2)
        answer = eval(question)

    print("What is: ", question, "?")
    result = int_check("Your answer?: ")

    if result == answer:
        feedback = "Correct!"
        prize_decoration = "W"

    else:
        feedback = "WRONG"
        prize_decoration = "L"
        questions_wrong += 1

    if result == "xxx":
        break

    # output results
    statement_generator(feedback, prize_decoration)

    round_result = "Question {}: {} = {}".format(questions_asked, question, result)

    game_summary.append(round_result)

    if questions_asked == questions:
            break

# Quick Calculations (stats)
questions_right = questions_asked - questions_wrong

# Ask user if they want to see their game history.
show_stats = choice_checker(summary_choice, yes_no_list, summary_error)
# If 'yes', show game history
# **** calculate game stats ******
percent_win = questions_right / questions_asked * 100
percent_lose = questions_wrong / questions_asked * 100

print()
print("***** Game History *******")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print("******** Game Stats *********")
print("Win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%))".format(questions_right, percent_win,
                          questions_wrong, percent_lose))

# Show game
# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {}".format(questions_right, questions_wrong))
print()
print("Thank you for playing !!!")
