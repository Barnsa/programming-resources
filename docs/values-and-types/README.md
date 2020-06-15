# Values and Types
There are 4 basic types in python; Boolean, integer, floating point number and string. Boolean's or "bools" are either true or false, a one or a zero, they are representative of the binary calculations that make computers work. Integers are any whole number and can be both positive and negative numbers, where as floating point numbers are anything with a decimal point in. A string is an interesting type as it also works like an iterable which we'll see more of later, but it stores a string of characters together. Every time we make a value that a computer needs to be able to reuse, we call that type a "variable". Let's look at some examples of how we use types and make variables:
 
## Creating your first variable
To create your first variable it's pretty easy, you just name it and then use the assignment operator to assign it to that name. This will create a sort of pet name, or pseudonym, for a location in memory where that value is then stored. Anytime you use that pseudonym you'll use whatever is stored in that memory location again. It's easier to show you then it is to explain it, so make sure you feel comfortable with everything here before you move on. 

### Naming Conventions
Variable names can start with a number, letter, or underscore, but not any other special character. PEP8 Python programming conventions say that variables should be named with all lower case letters, for longer variable names each word should be separated by underscores: 
```python
# a simple variable followed by the equals sign, we can make it any type of variable but we will make it an integer 
variable = 10

# This is the same thing but with a more descriptive and longer variable name
the_number_of_vowels_in_banana = 3
```
As code is read many more times than its written, so generally speaking longer variable names help others understand your code better. It's also good practice when you start to be very descriptive, so when you look back over your code to prompt you and study your programming, you'll remember what it was you were doing and how it works at a glance.

### Assignment 
Python is a dynamically typed language, what this means is that you don't have to know what type of data you want to store in a variable to be able to create it. In statically typed languages such as the 'C' family of languages, you must declare the type of data you are going to store in memory before you store it. In python, the size can dynamically change to 
```python
variable = 10 
print(variable)

variable = True
print(variable)

variable = "hello"
print(variable)

variable = 3.14
print(variable)
```


## Test Your Knowledge: 
