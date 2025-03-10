# This is a script asking a user for age and returning whether can vote basing on age. If below 18 returns also a time to wait.

age = int(input('How old are you? ')) # Inverting to integers.

# Counting years to wait.
to_wait = 18- age

# Checking the age and printing appropriate message
if age >= 18:
    print('You are allowed to vote!')

else:
    print('You are not allowed to vote!', 'Please wait', to_wait, 'years. ')
