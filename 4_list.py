# This is a script asking a user for a number and creating a list from it to zero

number = int(input('What is your number? ')) #Converting to integer because we focus on that numbers only

number_list = [number] #Creating a list and adding inputted number


for i in number_list: #Iterating through every item in the list if greater than zero.
        if i > 0:
            number_list.append(i - 1)

# Alternatively, it can be done by range() command but we need to remove [number] from number_list first.
# for i in range(number, -1, -1): 
#     number_list.append(i)


print(number_list)