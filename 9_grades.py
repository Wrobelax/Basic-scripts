# This is a script for asking a user about name and a score and returning a grade with a message basing on a score.


score = int(input("What's your score? ")) # Converting to integer.
name = input("What's your name?")


#using if, elif, else to return a proper grade with a message.
if score >= 80:
    print(f'{name}, you got an A grade with a score of {score}')

elif score <= 79 and score >= 70:
    print(f'{name}, you got a B grade with a score of {score}')

elif score <= 69 and score >= 60:
    print(f'{name}, you got a C grade with a score of {score}')

elif score <= 59 and score >= 50:
    print(f'{name}, you got a D grade with a score of {score}')

else:
    print(f'{name}, you Failed with a score of {score}')