# Values and Types
There are 4 basic types in python; Boolean, integer, floating point number and string. Booleans or "bools" are either true or false, a one or a zero, they are representative of the binary calculations that make computers work. Integers are any whole number and can be both positive and negative numbers, where as floating point numbers are anything with a decimal point in. A string is an interesting type as it also works like an iterable which we'll see more of later, but it stores a string of characters together. Every time we make a value that a computer needs to be able to reuse, we call that type a "variable". Let's look at some examples of how we use types and make variables:
 
## Basic Types: Creating your first variable
To create your first variable it's pretty easy, you just name it and then use the assignment operator to assign it to that name. This will create a sort of pet name, pseudonym, or alias for a location in memory where the object that contains the value is then stored. Anytime you use that pseudonym it'll refer to whatever is stored in that object again. It's easier to show you then it is to explain it, so make sure you feel comfortable with everything here before you move on. 

### Naming Conventions
Variable names can start with a number, letter, or underscore, but not any other special character. [PEP8](https://www.python.org/dev/peps/pep-0008/) Python programming conventions say that variables should be named with all lower case letters, for longer variable names each word should be separated by underscores: 

{{ code_from_file("values-and-types/example-1.py") }}

As code is read many more times than its written, so generally speaking, longer variable names help others understand your code better. It's also good practice when you start to be very descriptive, so when you look back over your code to prompt you and study your programming, you'll remember what it was you were doing and how it works at a glance.

### Assignment 
Python is a dynamically typed language, what this means is that you don't have to know what type of data you want to label with a variable name to be able to create it. In statically typed languages such as the 'C' family of languages, you must declare the type of data you are going to store in memory before you store it. In python, variables dynamically change behind the scenes to accommodate different basic types, here's an example:

{{ code_from_file("values-and-types/example-2.py") }}

In this example, our variable ambiguously called "variable" is a single location in memory. Each time we use the assignment operator (the equals sign), we force the variable to reference a different type of data and then ask it to print out to the screen. We're printing out the contents of the same alias every time, we're just overwriting the data in that location. We can also check the types of data with the next example:

{{ code_from_file("values-and-types/example-3.py", execute = True) }}

This does exactly the same as example 2 but it also prints out the basic type or object of the variable at each stage. Now you can see each of the types printed out too... see for yourself!

## Test Your Knowledge: Making your own variables
For this knowledge test, using appropriate naming conventions try making your own variables to describe numbers and strings you might use in your own programs. Make variables to contain a happy birthday wish, the value of pi to 5 decimal places, your favourite integer under 100, a variable containing the meaning of life, and the true or false logic of whether a mouse is larger than a Giraffe. Try to make at least one variable of every basic type. 

## Composite Types
There are also types that store or arrange basic types to make it easier to work with them, the three composite types are; lists, dictionaries, and tuples. Lists store a malleable group of variables that are easy to work with because the values can be referred to by index. An index is the numerical location of the position that a variable is in a list. Consider this list:
```python
name_of_a_list = ["variables", "are", "contained", "in", "here", 12, True, 33.33334]

```
As all indexes start at the number zero as a general rule in programming, we could also represent this data in a table like this:

| index number  |      0      |   1   |      2      |   3   |   4    |   5   |   6   |    7     |
| :------------ | :---------: | :---: | :---------: | :---: | :----: | :---: | :---: | :------: |
| variable data | "variables" | "are" | "contained" | "in"  | "here" |  12   | True  | 33.33334 |

We can write code to interact with an index value like this:   

{{ code_from_file("values-and-types/example-4.py", 1, 5) }}    

Which one of the variables do you think gets printed?? If you guessed "contained" then you just got caught out by the one thing that catches out every programmer at least once. As we said, all indexes start at the number 0 as a general rule. So "variables" is at index 0, "are" at index 1, and so on. The astute among you may have noticed that the only difference between interacting with a list and making a list is the use of the assignment operator. That's true of all variables, assigning requires the assignment operator and using the data doesn't. Tuples are similar to lists in that they have an index number for the location of the data, but they are not mutable, which is to say they cannot change their data once they are created. 



## Test Your Knowledge: 
