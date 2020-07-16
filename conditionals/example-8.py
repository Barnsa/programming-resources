# example-8.py first example 
# Showing the difference between the is keyword and the equality operator
list_1 = [10] 
list_2 = list_1        
list_3 = list(list_1)

# test all of the equalities
print(list_1 == list_2)
print(list_1 == list_3)
print(list_2 == list_3)

# test all of the is comparisons
print(list_1 is list_2)
print(list_1 is list_3)
print(list_2 is list_3)