# Iterating iterables, examples using dictionaries and lists in python 3

# example-3.py first example
list_of_fruit = ['apple', 'banana', 'cherry']
for item in list_of_fruit:
    print(item)

# example-3.py second example
dictionary = {'apple':3, 'banana':5, 'cherry':20}
for entry in dictionary.values():   # you can also use .items() or .keys() to get the dictionary pairs or keys
    print(entry)

# example-3.py third example
dictionary = {'apple':3, 'banana':5, 'cherry':20}
for entry in dictionary.items():   # See!!
    print(entry)
for entry in dictionary.keys():
    print(entry)