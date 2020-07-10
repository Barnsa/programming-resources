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

The code as you can see, doesn't respond the way we might like. We would want the code to work out if we can have dinner firstly if we picked a valid dinner option and also had enough money, but as we don't have enough money why is it evaluating as True? It's because the AND evaluates first, evaluating to False, and then the OR evaluates. In the evaluation of True OR False, it always evaluates to True. We can fix this with the following modification:

{{ code_from_file("conditionals/example-1.py", 13, 22, execute=True) }}

The other order of precedence that you have to watch out for is that some evaluations start from the right, and others start from the left. Consider this code:

{{ code_from_file("conditionals/example-2.py", 1, 18, execute=True) }}

You can see that depending on the type of evaluation used it will depend on whether it is evaluated from left to right. When in doubt you should test your code thoroughly and use parenthesis. 

## Literal Values
We've covered all of the basic types in python; the string, Boolean, integer, and floating point number. However, python also supports a lot of other literal values that aren't commonly used. Below is a more comprehensive list of literal values:

| literal type        | sample                       |
| :------------------ | :--------------------------- |
| String literal      | "hello",'hey'                |
| int literal         | 5                            |
| Long int literal    | 879564L (Only in python 2.x) |
| Floating point      | 3.1459                       |
| Complex Literals    | 12j                          |
| Boolean Literals    | True, False                  |
| Special Literals    | None                         |
| Unicode Literals    | u"Hello"                     |
| Byte Literals       | b"Hello"                     |
| Hex Literals        | 0x +hexValue                 |
| Octal Literals      | 0o +octValue                 |
| List Literals       | [] , [1, 2, 4, 5]            |
| Tuple Literals      | () , (9, ) , (1, 2, "happy") |
| Dictionary Literals | {} , {'x':7}                 |
| Set Literals        | {8, 9, 10}                   |

For those interested in coding literals and some of the abstract ideas surrounding literal testing, you can find more reading on python 3 conventions [here](https://www.python.org/dev/peps/pep-0586/) (WARNING: very advanced stuff!!). Here are some examples of the literals being used:

{{ code_from_file("conditionals/example-6.py", start=1, execute=True) }}

Generally though, you will only use basic types unless you are purposely trying to obfuscate your code, or doing type conversion specifically. It's just a good idea to be familiar with the other literals so that you aren't confused if you encounter them in other peoples code. The long integer isn't in python 3.x anymore as all integers are now treated as if they are long integers in python, to learn more about how it gets converted and how python is interpreted you can find it in the documentation [here](https://docs.python.org/3/c-api/long.html). 


## Inequalities
To talk about inequalities, we must first need to talk about what an equality is. In python, equality is the symbol == and will directly check if one object is equal to another object. This is not the same as the 'is' keyword. Consider this code:

{{ code_from_file("conditionals/example-8.py", start=1, stop=15, execute=True) }}

Here you can see that the difference between the equality operator and the is statement quite apparent. The equality operator looks to see if the values inside the lists are the same, whereas the is operator looks to see if the labels point to the same object. Understanding this key difference will help you to write good evaluation statements that behave the way you intend them to. 



## If 
The first control statement you need to learn in Python is the if statement. If statements are used in the construction of conditional execution to create decision making code. The 'if' part will execute if the statement evaluates as true. Consider this example:

{{ code_from_file("conditionals/example-3.py", 1, 30, execute=True) }}

Looking through this code you can see that some of the statements aren't printed. For instance, variable_3 is not of a type integer, you can also see that there are some statements that are there to catch different values of variable_1 and variable_2, and a statement to catch if variable_5 is True or False. This way of writing code isn't very readable however, because there are no logical connections between one statement and the others. This is where the elif statement comes in.

## Elif
We use the 'else if' or 'elif' statement to logically join statements together and run multiple checks on the same objects. If we take the code above and turn it into a more complex set of if statements then we get something a little clearer: 

{{ code_from_file("conditionals/example-4.py", 1, 30, execute=True) }}

As you can see the code is a little more logically grouped and it helps with processing cycles too. Once an if statement is executed, if it evaluates to true in the first part of the statement then it doesn't have to run any of the elif statements. As soon as one of the steps evaluates to true then the evaluation can exit there. In our previous example, each if statement has to be evaluated independently, increasing the amount of processing that needs to be done and making your code less readable. But what happens if you evaluate something and you don't trigger any condition, well there is the 'else' statement that handles that.   

## Else 
The else statement is designed to run after everything in the if/elif statement evaluates to False. Consider it a piece of code that runs 'if all else fails'. Else statements can also be used in loops which you will see later. Let's take the code we had in example 3 and 4 and improve it further to incorporate else statements:

{{ code_from_file("conditionals/example-5.py", 1, 40, execute=True) }}

## Boolean Logic
All logic inside a computer boils down to True or False logic. True is either represented by its name or by the number 1, False is represented by its name or 0. All modern classical (Von Neumann architecture) computers are based off of Boolean logic and Boolean algebra, this means that all the components inside the machine have been developed to take 1's and 0's and represent them in every way we need to create useful data with. For the purposes of programming however, you need to understand how truth tables refer to AND, OR, NAND (not AND) and NOR (not OR) logic. Here are the truth tables for each of the logical comparisons

|  AND  | True  | False |
| :---: | :---: | :---: |
| True  | True  | False |
| False | False | False |

|  OR   | True  | False |
| :---: | :---: | :---: |
| True  | True  | True  |
| False | True  | False |

| NAND  | True  | False |
| :---: | :---: | :---: |
| True  | False | True  |
| False | True  | True  |

|  NOR  | True  | False |
| :---: | :---: | :---: |
| True  | False | False |
| False | False | True  |

When considering your if statements, you need to consider how they will be evaluated. Consider this code fragment:

{{ code_from_file("conditionals/example-5.py", 1, 40, execute=True) }}
