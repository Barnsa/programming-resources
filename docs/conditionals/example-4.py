# example-4.py 
# elif statements and evaluations
# Remember an if or elif statement only triggers if it evaluates to True

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

if type(variable_3) == int:
    print(f"variable_3 is an integer not a string, see: {variable_3}")

if type(variable_4) == float:
    print(f"variable_4 is a float type with a value of {variable_4}")
    
if variable_5 is True:
    print(f"variable_5 is {variable_5}")
    
elif variable_5 is not True:
    print(f"variable_5 is {variable_5}")
    

## This file has some dependencies in the README.md file, check line 50. If you change this file you might have to change it there too. 