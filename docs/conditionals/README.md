# Conditional Statements
In python many variables that you create, whether they be basic ones or composite variables, need to be compared or evaluated at some point. If you have a variable in your code that isn't, then you probably don't need that variable. 

## Evaluation

## Order of Precedence 
Much like in math, python has an order to when an evaluation gets done. Here is a table:

| Operators             | Meaning                                                            |
| :-------------------- | :----------------------------------------------------------------- |
| ()                    | Parentheses                                                        |
| **                    | Exponent                                                           |
| +x, -x, ~x            | Unary plus, Unary minus, Bitwise NOT                               |
| *, /, //, %           | Multiplication, Division, Floor division, Modulus                  |
| +, -                  | Addition, Subtraction                                              |
| <<, >>                | Bitwise shift operators                                            |
| &                     | Bitwise AND                                                        |
| ^                     | Bitwise XOR                                                        |
| \|                    | Bitwise OR                                                         |
| ==, !=, >, >=, <, <=, | is, is not, in, not in Comparisons, Identity, Membership operators |
| not                   | Logical NOT                                                        |
| and                   | Logical AND                                                        |
| or                    | Logical OR                                                         |

The higher something is on the table the sooner it gets done. Things in parenthesis get done first, mostly so you can force the order of precedence. There are a few gottcha's in this list that tend to get every programmer at least once, but for you guys the biggest one will be that logical AND is performed before logical OR. Consider this code fragment:

{{ code_from_file("conditionals/example-1.py", 1, 10, execute=True) }}

The code as you can see, doesn't respond the way we might like. We would want the code to work out if we can have dinner if we picked a valid dinner option and also had enough money, but as we don't have enough money why is it evaluating as True? It's because the AND evaluates first, evaluating to False, and then the OR evaluates. In the evaluation of True OR False, it always evaluates to True. We can fix this with tht following modification:

{{ code_from_file("conditionals/example-1.py", 13, 22, execute=True) }}

The other order of precedence that you have to watch out for is that some evaluations start from the right, and others start from the left. Consider this code:

{{ code_from_file("conditionals/example-2.py", 1, 18, execute=True) }}





# Literal Values
# Boolean Logic
# Inequalities

# If 
The first control statement you need to learn in Python is the if statement. If statements are used in the construction of conditional execution to create decision making code. 
# Else
# Elif