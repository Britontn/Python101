#Decorators
#A decorator is a design pattern in Python that allows a user to add new functionality to an existing
# object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
def announce(f):
    def wrapper():
        print('About to run the function...')
        f()
        print('Done with the function.')
    return wrapper

@announce
def hello():
    print('Hello, world!')

hello()