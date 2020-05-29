# Iteration or Loops 

Anytime you want to do anything more than once in a Python program, you should consider putting it inside a loop.  
There are two types of loops in python, a 'for' loop and a 'while' loop. Generally for loops are used when you know the amount of times you want to repeat something. It doesn't have to be an exact integer value, it can also be anything easily calculable. 'While' loops are used when you aren't sure how many times you need to repeat something. 
In python, all control statements use indentation to define blocks of grouped code.   

# For Loops (definite iteration)
## Iterating iterables
For loops always start with the keyword 'for' and then an iterator followed by some condition. 
Here are a few examples:  
```python
string = 'hello world!' 
for i in string:
    print(i)
```
In this first case, we define a sting of text we poignantly called string. Then we create the for loop by stating that for each index (i) inside the string, we want to print out the value of 'i'. It is common practice in coding to use 'i' as the variable that iterates through something in a loop. The output of this code is that each letter is looked at by the 'i' in the for loop and then printed out to a new line in the console. 
```python
word = 'banana'
count = 0 
for letter in word:
    if letter is 'a':
        count = count + 1   # count +=1 would also work here
print(count)
```
In this example, we have a more pythonic idea. The word 'letter' works the same way as the 'i' in the previous example, it's just more descriptive which helps with clarity when rereading later. See if you can work out what this program does without running it.   
Other than strings you can also iterate through any type of iterable including: dictionaries, lists, tuples and sets. 
some examples:
```python
list_of_fruit = ['apple', 'banana', 'cherry']
for item in list_of_fruit:
    print(item)
```
```python
dictionary = {'apple':3, 'banana':5, 'cherry':20}
for entry in dictionary.value():   # you can also use .items() to get the dictionary keys
    print(entry)
```
## Iterating Ranges
Using the range function, we can also create 'for' loops that iterate a number of times. Consider these examples:
```python
for count in range(10):
    print(count)
```
```python 
# how long is the string 
string = 'How long is a piece of string?' 
count = 0
for i in range(len(string)):
    count +=1 
print(count)
```
