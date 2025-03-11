# This is a script counting 10 numbers from Fibonacci sequence.

fib = [0,1] # Adding first two numbers to the list as a start for counting.

for i in range(8): # Iterating through eight (because list needs to consista of 10 numbers from fibonnacci's sequence)
    new_number = fib[i] + fib[i + 1] # Creating new number as number i + next number (i + 1)
    fib.append(new_number) # Appending created number

print(fib)

# Alternatively, not defining a list but variables and adding them
# a, b = 0, 1
#
# for i in range(10):
#     print(a)
#     a, b = b, a + b