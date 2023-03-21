#Function that calles another function (from functions.py)
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")

#Another way is tp import the entire module
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")