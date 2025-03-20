"""Word Frequency Counter."""

### Read Text File Function ###
# This function opens a text file in read mode, and then returns the contents of the file as a string.
def read_text_file(file_name:str) -> str:
    with open (file_name, "r") as file:
        read_file = file.read()
    return read_file


### File Contents Parser Function ###
# This function iterates over the raw text and for each character:
# if the character is alphanumeric, or a space character we add it to a variable local to the function. This is then split and returned as a list.
def file_contents_parser(raw_text:str) -> list:
    desired_characters = ""
    for i in raw_text:
        if i.isalnum() == True or i.isspace() == True:
            desired_characters += i.lower()

    return desired_characters.split()


### Frequency Dictionary Builder Function ###
# This function creates a blank dictionary, and then iterates over the list of parsed words. For each word in the list:
# if not in the dictionary, add it with a value of 1.
# If in the dictionary, increase its value by 1.
# Sort the dictionary according to their values, and return it.
def freq_dict_builder(parsed:list) -> dict:
    new_dict = {}

    for i in parsed:
        if i in new_dict.keys():
            new_dict[i] += 1
        elif not i in new_dict.keys():
            new_dict[i] = 1
    sorted_dict = dict(sorted(list(new_dict.items()), key = lambda x:x[1]))

    return sorted_dict


### Then set up variables and call functions.

file_name = "python_zen.txt"

file_reader = read_text_file(file_name)

file_parser = file_contents_parser(file_reader)

for keys, values in freq_dict_builder(file_parser).items():
    print(f"'{keys}': {values}")




