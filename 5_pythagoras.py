# This is a script counting hypotenuse from pythagoras equation.

a = float(input('Please input first lenght: ')) #Inverting to float when inputing as a number may be non-integer.
b = float(input('Please input second lenght: '))

print ('Hypotenuse lenght is', ((a**2) + (b**2)) ** 0.5)