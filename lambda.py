people =[{'name': "Harry", "House": "Gryffindor"},
        {'name': "Cho", "House": "Ravenclaw"},
        {'name': "Draco", "House": "Slytherin"}
        ]
# This method will result in error, as the sort function does not know how to sort a list of dictionary

# people.sort()
# print(people)

# Defining a function for sorting, this will take the name and sort it in alphetibical way

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

# lambda function for simple function

people.sort(key= lambda person: person["name"])