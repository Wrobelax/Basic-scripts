# This is a script using loop for asking a user for three favourite movies, adding them to the list and printing them.

# Creating empty list
movie_list = []

# Looping question in range 3 and appending responses to the list
for i in range(3):
    movie = input(f"What's your #{i+1} favourite movie? ")
    movie_list.append(movie)


# printing each movie separately to avoid brackets and separating last two by "and".
print(f'Your favourite movies are {movie_list[0]}, {movie_list[1]}, and {movie_list[2]}.')