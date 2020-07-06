# example-5.py 
# else statements
# Remember an if or elif statement only triggers if it evaluates to True,
# if all of them evaluate to false then the else statement runs.

variable_1 = 10 
variable_2 = 5 
variable_3 = "trigonometry"
variable_4 = 5.5 
variable_5 = False 

if variable_1 > variable_2:
    print(f"{variable_1} is greater than {variable_2}")        
elif variable_1 < variable_2:
    print(f"{variable_1} is less than {variable_2}")        
elif variable_1 == variable_2:
    print(f"variable_1:{variable_1} and variable_2:{variable_2} are equal")
else:
    print(f"Something went very wrong!! Variable 1 or 2 are broken.")


if type(variable_3) == int:
    print(f"variable_3 is an integer not a string, see: {variable_3}")
else:
    print(f"variable_3 is not an integer, see: {variable_3}")


if type(variable_4) == float:
    print(f"variable_4 is a float type with a value of {variable_4}")
else: 
    print(f"variable_4 is the wrong type.")    


if variable_5 is True:
    print(f"variable_5 is {variable_5}")
elif variable_5 is not True:
    print(f"variable_5 is {variable_5}")
else:
    print(f"variable_5 is not a Boolean for some reason.")    

## This file has some dependencies in the README.md file, check line 50. If you change this file you might have to change it there too. 