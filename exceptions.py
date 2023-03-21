#Error handling

import sys

#Input validation say for example if someone enters a char or string

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print('Error: Invalid input')
    sys.exit(1)

#This code validates and handles errors if trying to divide by 0
try:
    result = x / y
except ZeroDivisionError:
    print('Error: Cannot divide by 0')
    sys.exit(1) #this exits the code

print(f'{x} / {y} = {result}')
