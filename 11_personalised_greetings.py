"""Personalised Greeting Creator."""
import random as ra

# A dictionary with greetings
greetings1 = 'Hello there!'
greetings2 = 'Hi there!'
greetings3 = 'Oh, hello!'

greetings_dict = {1 : greetings1,
                  2 : greetings2,
                  3 : greetings3}

### Choose random template function ###
# This function accepts: Nothing.
# Uses the random module to select a random key from the greetings dict
# and then returning its value (a random template greeting)
def random_num():
    return ra.randint(1,3)


### Choose greeting template function ###
# This function accepts: Nothing.
# Use user input to prompt the user to select a random greeting from the dict.
# This is then returned. We can choose a random one if they fail to choose correctly.
def rand_greet():
    chosen_num = input('Please pick a random greeting from 1-3. ')
    if chosen_num in greetings_dict:
        return greetings_dict[chosen_num]
    else:
        return greetings_dict[ra.randint(1,3)]

### Main 'run all' function ###
# This function accepts: Nothing.
# This first prompts the user for a name
# The it asks the user to choose between a fixed or random greeting.
# based on their choice we then call either the random or normal greeting
# function, and add their name to the template.
def run_all():

    name = input('What is your name? ')
    fixed_rand = input('Do you want your greetings to be fixed or random?').title()

    if fixed_rand == 'Fixed':
       return print(f"{rand_greet()} {name}")
    else:
       return print(f"{greetings_dict[ra.randint(1,3)]} {name}")



run_all()
