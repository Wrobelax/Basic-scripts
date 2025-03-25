"""Customisable Maths quiz."""
import random as ra
from datetime import datetime


def choose_question_type() ->str:
    """Ask user for preferred type of maths question.

       The user is prompted to make a choice from the options available.
       The loop will continue to ask whilst their choice is not one of the
       available options from the list.

       Returns:
           The type of question to be used in the quiz.
       """

    random_types = ["Adding", "Subtracting", "Multiplying", "Dividing", "Modulus", "Exponentiation", "Mixed"]
    attempts = 0

    while attempts < 3:
        attempts += 1
        type = input("Please choose questions set: Adding, Subtracting, Multiplying, Dividing, Modulus, Exponentiation or Mixed: ").title()

        if (type == "Adding" or
                type == "Subtracting" or
                type == "Multiplying" or
                type == "Mixed" or
                type == "Dividing" or
                type == "Modulus" or
                type == "Exponentiation"):
            print(f"You are going to respond for a set of {type} questions.")
            return type
        else:
            print("Incorrect choice.")
            continue

    else:
        rand_choice = ra.choice(random_types)
        print(f"Provided incorrect choice too many times, picking radomly. Your set is: {rand_choice}. ")
        return rand_choice


def choose_number_of_questions() -> int:
    """Ask user for number of questions they'd like to answer.

    Returns:
        the number of questions, which will determine loop size.
    """
    rand_questions = range(1,10)

    try:
        numb_questions = int(input(f"Please pick a number of questions that you would like to respond on: "))
        return numb_questions
    except ValueError:
        numb_questions = ra.choice(rand_questions)
        print(f"Incorrect number of questions, choosing randomly. You are going to respond on {numb_questions} questions.")
        return numb_questions


def choose_dificulty_level() ->int:
    """Ask user for desired difficulty level.

    In the quiz we have 5 difficulty levels (1-5), where 1 is
    the easiest and 5 is the hardest. The difficulty level will
    be used later when generating questions. The higher the
    difficulty, the larger the numbers that are used.

    Returns:
        and integer from 1-5 representing difficulty level.
    """
    diff_random = range(1,5)

    try:
        diff_lvl = int(input(f"Please choose difficulty level from 1-5: "))
        if diff_lvl <= 5:
            return diff_lvl
        else:
            diff_lvl = ra.choice(diff_random)
            print(f"Incorrect difficulty level, choosing randomly. Your difficulty level is {diff_lvl}.")
            return diff_lvl
    except ValueError:
        diff_lvl = ra.choice(diff_random)
        print(f"Incorrect difficulty level, choosing randomly. Your difficulty level is {diff_lvl}.")
        return diff_lvl


def generate_numbers_for_questions(difficulty_lvl: int) -> tuple:
    """Generate the numbers needed for the questions.

        Difficulty level 1: numbers 2 - 20
        Difficulty level 2: numbers 4 - 40
        Difficulty level 3: numbers 6 - 60
        Difficulty level 4: numbers 8 - 80
        Difficulty level 5: numbers 10 - 100

        Args:
            difficulty_lvl: A number from 1-5 relating to the difficulty of the question.

        Returns:
            A tuple of 2 numbers to be used in the question.
        """
    difficulty_lvl_1 = range(2,20)
    difficulty_lvl_2 = range(4,40)
    difficulty_lvl_3 = range(6,60)
    difficulty_lvl_4 = range(8,80)
    difficulty_lvl_5 = range(10,100)

    if difficulty_lvl == 1:
        rand_number_1 = ra.choice(difficulty_lvl_1)
        rand_number_2 = ra.choice(difficulty_lvl_1)
        return rand_number_1,rand_number_2

    elif difficulty_lvl == 2:
        rand_number_1 = ra.choice(difficulty_lvl_2)
        rand_number_2 = ra.choice(difficulty_lvl_2)
        return rand_number_1,rand_number_2

    elif difficulty_lvl == 3:
        rand_number_1 = ra.choice(difficulty_lvl_3)
        rand_number_2 = ra.choice(difficulty_lvl_3)
        return rand_number_1,rand_number_2

    elif difficulty_lvl == 4:
        rand_number_1 = ra.choice(difficulty_lvl_4)
        rand_number_2 = ra.choice(difficulty_lvl_4)
        return rand_number_1,rand_number_2

    elif difficulty_lvl == 5:
        rand_number_1 = ra.choice(difficulty_lvl_5)
        rand_number_2 = ra.choice(difficulty_lvl_5)
        return rand_number_1,rand_number_2


def addition_question(operand_a: int, operand_b: int) -> bool:
    """Ask addition question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """

    try:
        question = int(input(f"What is the sum of numbers {operand_a} and {operand_b}: "))
        if question == (operand_a + operand_b):
            print("That's correct! One point to Gryffindor!")
            return True
        else:
            print(f"That's not the correct answer. It should be {operand_a + operand_b}.")
            return False
    except ValueError:
        print(f"That's not a number. Correct answer is {operand_a + operand_b}.")
        return False


def subtraction_question(operand_a: int, operand_b: int) -> bool:
    """Ask subtraction question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """

    try:
        question = int(input(f"What is the subtraction of numbers {operand_a} and {operand_b}: "))
        if question == (operand_a - operand_b):
            print("That's correct! One point to Gryffindor!")
            return True
        else:
            print(f"That's not the correct answer. It should be {operand_a - operand_b}.")
            return False
    except ValueError:
        print(f"That's not a number. Correct answer is {operand_a - operand_b}.")
        return False


def multiplication_question(operand_a: int, operand_b: int) -> bool:
    """Ask multiplication question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """

    try:
        question = int(input(f"What is the multiplication of numbers {operand_a} and {operand_b}: "))
        if question == (operand_a * operand_b):
            print("That's correct! One point to Gryffindor!")
            return True
        else:
            print(f"That's not the correct answer. It should be {operand_a * operand_b}.")
            return False

    except ValueError:
        print(f"That's not a number. Correct answer is {operand_a * operand_b}.")
        return False


def division_question(operand_a: int, operand_b: int) -> bool:
    """Ask division question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """

    try:
        question = int(input(f"What is the division of numbers {operand_a} and {operand_b}: "))
        if question == (operand_a / operand_b):
            print("That's correct! One point to Gryffindor!")
            return True
        else:
            print(f"That's not the correct answer. It should be {operand_a / operand_b}.")
            return False

    except ValueError:
        print(f"That's not a number. Correct answer is {operand_a / operand_b}.")
        return False


def modulus_question(operand_a: int, operand_b: int) -> bool:
    """Ask modulus question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """

    try:
        question = int(input(f"What is the modulus of numbers {operand_a} and {operand_b}: "))
        if question == (operand_a % operand_b):
            print("That's correct! One point to Gryffindor!")
            return True
        else:
            print(f"That's not the correct answer. It should be {operand_a % operand_b}.")
            return False

    except ValueError:
        print(f"That's not a number. Correct answer is {operand_a % operand_b}.")
        return False


def exponentiation_question(operand_a: int, operand_b: int) -> bool:
    """Ask exponentiation question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """

    try:
        question = int(input(f"What is the exponentiation of numbers {operand_a} and {operand_b}: "))
        if question == (operand_a ** operand_b):
            print("That's correct! One point to Gryffindor!")
            return True
        else:
            print(f"That's not the correct answer. It should be {operand_a ** operand_b}.")
            return False

    except ValueError:
        print(f"That's not a number. Correct answer is {operand_a ** operand_b}.")
        return False


def main_game_loop(question_type: str, num_of_questions: int, difficulty_level: int) -> int:
    """Orchestrate the question loop and score keeping.

    This function consists of a for loop which loops for as many times as 'difficulty_level'
    For each cycle of the loop, the question type is examined which either picks a 'fixed' question
    or in the case when 'Mixed' is selected a random question is chosen from the list. The score is kept
    during the quiz and incremented for each correct answer.

    Args:
        question_type: The type of questions to select (which function to call).
        num_of_question: Number of questions to answer (How long the loop runs for).
        difficulty_level: Determines the numbers to come from 'generate_numbers_for_question'.

    Returns:
        The number of correctly answered questions.
    """
    correct_answers = 0
    random_set = ["Adding", "Subtracting", "Multiplying", "Dividing", "Modulus", "Exponentiation"]

    for i in range(1, num_of_questions+1):
        print(f"Question {i}:")
        if question_type == "Mixed":
            random_choice = ra.choice(random_set)
        else:
            random_choice = question_type

        if random_choice == "Adding":
            answer = addition_question(generate_numbers_for_questions(difficulty_level)[0],
                                       (generate_numbers_for_questions(difficulty_level)[1]))
            if answer == True:
                correct_answers += 1

        elif random_choice == "Subtracting":
            answer = subtraction_question(generate_numbers_for_questions(difficulty_level)[0],
                                          (generate_numbers_for_questions(difficulty_level)[1]))
            if answer == True:
                correct_answers += 1

        elif random_choice == "Multiplying":
            answer = multiplication_question(generate_numbers_for_questions(difficulty_level)[0],
                                             (generate_numbers_for_questions(difficulty_level)[1]))
            if answer == True:
                correct_answers += 1

        elif random_choice == "Dividing":
            answer = division_question(generate_numbers_for_questions(difficulty_level)[0],
                                       (generate_numbers_for_questions(difficulty_level)[1]))
            if answer == True:
                correct_answers += 1

        elif random_choice == "Modulus":
            answer = modulus_question(generate_numbers_for_questions(difficulty_level)[0],
                                       (generate_numbers_for_questions(difficulty_level)[1]))
            if answer == True:
                correct_answers += 1

        elif random_choice == "Exponentiation":
                answer = exponentiation_question(generate_numbers_for_questions(difficulty_level)[0],
                                          (generate_numbers_for_questions(difficulty_level)[1]))
                if answer == True:
                    correct_answers += 1

    return correct_answers


def main() -> None:
    """Driver function to orchestrate maths quiz."""

    name = input(f"What is your name? ").title()
    question_type = choose_question_type()
    question_numbers = choose_number_of_questions()
    difficulty = choose_dificulty_level()
    score = main_game_loop(question_type,question_numbers,difficulty)
    time_now = datetime.strptime('2022-05-10 16:30:22', "%Y-%m-%d %H:%M:%S")
    text = f"{name}, you scored with {score} correct answers in {question_type} set at difficulty level {difficulty}-{question_numbers} questions on {time_now}.\n"
    with open("15_math_game_score.txt", mode="a") as game_log:
        game_log.write(text)
    print (text)

    pass

if __name__ == "__main__":
    main()