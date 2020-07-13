# example-9.py 
# Common evaluations and their outcomes
variable_1 = 4
variable_2 = 2
variable_3 = 3
variable_4 = 5

# Simple math functionality
print(variable_1 + variable_2)
print(variable_1 - variable_2)
print(variable_1 * variable_2)
print(variable_1 / variable_2) # / always becomes a floating number
print(variable_1 % variable_2)
print(variable_1 // variable_2)

# Let's do some type checking to prove it
print(type(variable_1 + variable_2))
print(type(variable_1 - variable_2))
print(type(variable_1 * variable_2))
print(type(variable_1 / variable_2))
print(type(variable_1 % variable_2))
print(type(variable_1 // variable_2))

# String concatination 
# this uses the + in an interesting way
string_1 = "hey"
string_2 = "you"
print(string_1 + " " + string_2 + "!")
print(type(string_1 + " " + string_2 + "!"))

# interesting evaluations that still happen from left to right
# mostly... 
print(variable_1 + variable_2 * variable_3 + variable_4)
print(variable_4 + variable_1 * variable_2 - variable_3)
