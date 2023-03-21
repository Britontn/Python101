

people = [
    {"name": "Harry", "house": "Gryffindor" },
    {"name": "Cho", "house": "Ravenclaw" },
    {"name": "Draco", "house": "Slytherin" }
]

#Sort by default will not know how to sort dictionary
#so we will need to tell it how to sort by defining a function to
# return only the name and then we sort by the returned values
def f(person):
    return person['name']

people.sort(key=f)
print(people)


#Another way to achieve this is to use the LAMBDA function

people.sort(key=lambda person: person['name'])
print(people)
