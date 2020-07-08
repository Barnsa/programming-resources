# example-7.py
# code to illustrate complex if statement evaluations
variable_1 = 17 
variable_2 = 17 
variable_3 = 8
variable_4 = True 
variable_5 = False

if (variable_1 > variable_2 or variable_4) and (variable_1 == variable_2) \
    or not variable_4: 
        print("evaluation 1 is true!")
else:
    print("evaluation 1 is False!")
        
if (variable_3 is variable_2 or variable_4) and (variable_3 is not variable_2) \
    and not variable_5: 
        print("evaluation 2 is true!")
else:
    print("evaluation 2 is False!")
    
if (variable_2 is not variable_3 and not variable_5) and \
    (variable_1 is not variable_2) and variable_4: 
        print("evaluation 2 is true!")
else:
    print("evaluation 2 is False!")