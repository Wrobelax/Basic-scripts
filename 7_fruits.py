# This is a script asking a user for a favourite fruit and comparing it to a static list of my favourite fruits.

fav_fruits = ['apple', 'banana', 'kaki', 'mango', 'blueberry'] # Static list of fruits.

user_fruit = input("What's your favourite fruit? ") # Asking a user for a favourite fruit.


if user_fruit.lower() in fav_fruits: # Checking if user's favourite fruit is on the list with ignoring first caps letter.
    print(f'We both like {user_fruit}!')

else:
    print(f"I haven't tried {user_fruit} yet. I'll have to give it a go!")