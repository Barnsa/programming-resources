# Functions
Functions are self contained objects that are used to create code that we often want to reuse. The most arbitrary use of a function is in this code:

{{ code_from_file("conditionals/example-1.py", 1, 9, execute=True) }}

As you can see, we have created our first function. To create a function you must first use the def keyword followed by the name for the function. The naming conventions for functions are the same as they are for variables. However, it is good practice to have descriptive names for your functions so that you can recognise what they do at a glance. 

The shape of a user defined function is always of the form:
```python
def name_of_function(passed_variable):
    <contents of the function,>
    <indented even across>
    <multiple lines.>
```
The contents of the function is always indented to show that it belongs to the function definition above it. 

outline user defined
    - abstraction and reusability 
    - modularity 
    - namespace separation
    - how a function is called and how it is defined 
    - passing arguements 
    - keyword arguement rules 
    - mutable default parameteres
    - pass by value and pass by reference
    - return statement
    - side effects 
    - variable length arguement lists
    - tuple packing and unpacking
    - dictionary packing and unpacking
    - docstrings
    - dunders
    - function annotations

outline built-in functions
    - generators 
    - yeild 
    - lambda 
    - map 
    - 