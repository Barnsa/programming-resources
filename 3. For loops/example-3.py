# Iterating iterables, examples using dictionaries and lists in python 3

print("First example")
list_of_fruit = ['apple', 'banana', 'cherry']
for item in list_of_fruit:
    print(item)

print("\n")    
print("\nSecond Example")
dictionary = {'apple':3, 'banana':5, 'cherry':20}
for entry in dictionary.values():   # you can also use .items() or .keys() to get the dictionary pairs or keys
    print(entry)

print("\n")    
print("Third Example")
dictionary = {'apple':3, 'banana':5, 'cherry':20}
for entry in dictionary.items():   # See!!
    print(entry)
for entry in dictionary.keys():
    print(entry)