"""Encryption and Decryption program."""

### Read Text File Function ###
# it opens a file in read mode, and then returns the contents as a lower case string.
def read_text_file(filename:str) -> str:

    file = open(filename, "r")
    contents = str((file.read()).lower())

    return contents


### Encryption Function ###
# This function iterates over the string.
# It then converts the string to its ASCII value, and applies a shift.
# This is then appended to the list, and then returned.
def encryption_function(plain_text:str,shift:int) -> list:

    encrypted_list = []

    for i in plain_text:
        msg = ord(i) + shift
        encrypted_list.append(msg)

    return encrypted_list


### Write Encrypted File Function ###
# The function converts the list into a string.
# Then it adds 'ENCRYPTED_ to the filename.
# It then opens the file and writes the cypher text to it.
def encrypted_file(encrypted_text:list, filename):

    encrypted_str = " ".join(map(str, encrypted_text))
    encryption = (open(f"ENCRYPTED_{filename}", "w")).write(encrypted_str)

    return encryption


### Decryption Function ###
# This function converts the string into a list.
# The list is iterated over, and with each character, apply the reverse shift, and print it.
def decryption_function(encrypted_text:str, shift:int):

    message = ""
    encrypted_list = encrypted_text.split()

    for i in encrypted_list:
            i = int(i) - shift
            msg = chr(i)
            message += msg
    return message


### Driver function ###
# This function first opens the file ready for use.
# Then if in encrypt mode:
    # Pass the contents to the encrypt function
    # then pass them to the file write function
# then if in decrypt mode:
    # pass the contents to the decrypt function
def driver_function(filename:str, shift:int, encrypt:bool):

    file = read_text_file(filename)

    if encrypt == False:

        return print(f"Decrypted message is: {decryption_function(file, shift)}.")

    elif encrypt == True:
        plain_text = encryption_function(file, shift)
        encrypted_file(plain_text, "my_message.txt")

        return print(f"Message was safely encrypted in 'ENCRYPTED_my_message.txt' file.")


# To encrypt: provide file name to the function, set shift number and set encryption to True.
# To decrypt: provide file name to the function, set shift number and set encryption to False.

driver_function("13_ENCRYPTED_my_message.txt",4, False)