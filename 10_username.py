# This is a script asking a user for a username and if correct asking for password. This may be used when creating a new account so the username and password must meet certain criteria.
# The script uses nested if statement.

username = input('Enter a username: ')

if username.isalpha() and len(username) > 6: # Username must be letters only and longer than 6 characters
    password = input ('Enter a password: ')
    if len(password) > 5 and len(password) < 12 and password.isalnum(): # Password must be longer than 5 but shorter than 12 and be alphanumeric
        print ('username and password are OK!')
    else:
        print ('password not accepted!')
else:
    print ('username not accepted!')