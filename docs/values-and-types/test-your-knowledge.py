# test-your-knowledge.py
# Broken code to illustrate composite type manipulation in python 3.5
# . . . 
## First create an empty dictionary called "dictionary_of_things", 
## a tuple called "tuple_of_stuff" and a list called "list_of_bits".
tuple_of_stuff = ()
list_of_bits = []
dictionary_of_things = {}


## Next make <key>:<value> entries in the dictionary that adds 
## "thing1":"Bonobo" and "thing2": ["monkey", "sushi"]
## Extra: add a dictionary value of every basic and composite type
## then print out the keys and values
dictionary_of_things["thing1"] = "Bonobo"
dictionary_of_things["thing2"] = ["monkey", "sushi"]
print(dictionary_of_things.keys())
print(dictionary_of_things.values())


## Next make the tuple_of_stuff contain the numbers 10 and 7,
## concatenate it together with "tuple2", and make sure the 
## final label is tuple_of_stuff. Make sure you print out the 
## completed tuple.
## Extra: sort "tuple_of_stuff" without breaking the type test
tuple_of_stuff = (10, 7)
tuple2 = (100, 27, 35, 53, 72, 19, 84, 9)
tuple_of_stuff = tuple_of_stuff + tuple2
tuple_of_stuff = tuple(sorted(tuple_of_stuff))
print(tuple_of_stuff)


## Next create data for the list_of_things of every basic type,
## concatenate it together with the "list2", and make sure the
## combined list is sorted and called "uber_list". 
## Extra: slice your sting you made in uber_list, and print out
## only the middle character, or middle two if it's an even 
## number of characters.  
list_of_bits = ["Monkey", 12, True, 3.4]
list2 = ["This ", "is ", "for ", "an ", "uber_", "list!"]
uber_list = list_of_bits + list2
print(uber_list)










### Test code to make sure that your code works and passes inspection
if __name__ == "__main__":
    import os
    path = os.getcwd()
    os.system("pytest " + os.getcwd())
