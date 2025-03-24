import random as ra
from datetime import datetime
import time

def establish_random_number(user_number_low:int, user_number_high:int) ->int:
    """Return a random integer given the low and high points.

     Args:
         lowest: the lowest possible random number.
         highest: the highest possible random number.

     Returns:
         A random number between lowest and highest (inclusive of both).
     """

    rand_number = int(ra.randint(user_number_low, user_number_high))

    return rand_number


def create_save_file_text(name: str, guess: int, user_number_low: int, user_number_high: int) -> str:
    """Create the text to be appended to the save game file.

    Args:
        name: The name of the player.
        guess: The number of guesses taken to guess the correct number.
        user_number_low: The lowest possible number, as defined by the player.
        user_number_high: The highest possible number, as defined by the player.

    Returns:
        A string which details the game, to then be written to file.
    """
    time_now = datetime.strptime('2022-05-10 16:30:22', "%Y-%m-%d %H:%M:%S")
    written_log = f"Player {name} guessed after {guess} try. Given a choice of {user_number_high} numbers. Dated: {time_now}.\n"

    return written_log


def write_text_to_file(filename: str, text: str, mode='a') -> None:
    """Write the text to file.

    Args:
        filename: The name of the file to be opened for appending.
        text: The text to be written to file.
        mode='a': Mode has been set to append, but can be changed if needed.
    """
    with open(filename, mode="a") as game_log:
        game_log.write(text)

    pass


def main_gameplay(random_number:int, lowest:int, highest:int) -> int:
    """Gameplay loop.

    Args:
        random_number: this is the number the player is trying to guess.
        lowest: this is the lowest number from the range provided by the player.
        highest: this is the highest number from the range provided by the player.

    Returns:
        The number of attempts taken to guess correctly.
    """
    guess = 1
    guess_list = []

    while random_number:

        try:
            guess_numb = int(input('Guess a number:'))
        except ValueError:
            print("That's not a valid number, try again!")
            continue

        if guess_numb != random_number:

            for number in guess_list:
                if guess_numb == number:
                    guess -= 1
                    print(f'You already tried {guess_numb}.')

            if guess_numb > random_number:
                if guess_numb > highest:
                    print(f"You provided a number outside of range! Pick a number between {lowest} and {highest}.")
                else:
                    guess += 1
                    guess_list.append(guess_numb)
                    print('Try again but lower...')
            elif guess_numb < random_number:
                if guess_numb < lowest:
                    print( f"You provided a number outside of range! Pick a number between {lowest} and {highest}.")
                else:
                    guess += 1
                    guess_list.append(guess_numb)
                    print('Try again but higher...')


        elif guess_numb == random_number:
            print(f"That's correct! You guessed after {guess} try!")
            break

    return guess


def retrieve_lower_upper_numbers() -> tuple:
    """Retrieve the low/high numbers from the user.

    The user is prompted to enter the low/high numbers, and
    gets 3 attempts to do so. The try/except is to catch a situation
    where the integers are incorrectly entered. If the user exceeds the
    number of attempt then they are given 1 & 10 by default.

    Returns:
        A tuple of the low and high numbers, used in random number generation.
    """
    attempts = 1

    while attempts <= 3:
        try:
            user_number_low = int(input('Please pick the lowest number: '))
            user_number_high = int(input('Please pick the highest number: '))
            rand_number = int(ra.randint(user_number_low, user_number_high))
            return (user_number_low, user_number_high)


        except ValueError:
            attempts += 1
            if attempts <= 3:
                print('You provided incorrect numbers. Try again.')

    else:
        user_number_low = 1
        user_number_high = 10
        print('You provided too many wrong numbers. You are going to guess a number between 1 and 10.')
        return (user_number_low, user_number_high)


def score_reader(filename:str) -> str:
    """Read the current score board to the player.

    Args:
        filename: File to be read.

    Returns:
         String of current score.
    """
    with open(filename, mode="r") as file:
        read_score = file.read()

        return read_score


def main(filename: str) -> None:
    """Driver function to orchestrate gameplay.

    Args:
        filename: the name of the text file to be written to.
    """
    print(f"Current leaderboard is as follows: \n{score_reader(filename)}.")
    time.sleep(5)

    name = input('Please enter your name: ')

    while name.isalpha() == False:
        name = input("You provided incorrect name. Please use letters only: ")
    else:
        pass

    name = name.title()

    numbers = retrieve_lower_upper_numbers()
    rand_numb = establish_random_number(numbers[0],numbers[1])
    guesses = main_gameplay(rand_numb,numbers[0],numbers[1])
    msg = create_save_file_text(name, guesses, numbers[0],numbers[1])
    write_text_to_file(filename,msg)

main('14_game_log.txt')
