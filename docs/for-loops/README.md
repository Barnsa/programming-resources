# For Loops

Anytime you want to do anything more than once in a Python program, you should consider putting it inside a loop.  
There are two types of loops in python, a 'for' loop and a 'while' loop. Generally 'for' loops are used when you know the amount of times you want to repeat something. It doesn't have to be an exact integer value, it can also be anything easily calculable. 'While' loops are used when you aren't sure how many times you need to repeat something, this could be to repeat something until a condition is reached or until a user tells it to stop. 
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
In this first case, we define a sting of text we poignantly called string. Then we create the 'for' loop by stating that for each index (i) inside the string, we want to print out the value of 'i'. It is common practice in coding to use 'i' as the variable that iterates through something in a loop or for an index location for something iterable. The output of this code is that each letter is looked at by the 'i' in the for loop and then printed out to a new line in the console. 
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
Here are some examples:
```python
list_of_fruit = ['apple', 'banana', 'cherry']
for item in list_of_fruit:
    print(item)
```
```python
dictionary = {'apple':3, 'banana':5, 'cherry':20}
for entry in dictionary.values():   # you can also use .items() or .keys() to get the dictionary pairs or keys
    print(entry)
```

## Iterating Ranges
Using the range function, we can also create 'for' loops that iterate a number of times. Consider these examples:
```python
for count in range(10):   # range(<stop>)
    print(count)
```
```python
for count in range(4, 10):   # range(<start>, <stop>)
    print(count)
```
```python
for count in range(1, 10, 3):   # range(<start>, <stop>, <increment>)
    print(count)
```
In these examples, you can see how the range function is used to set a maximum limit to the number of times the 'for' loop iterates. Notice also that if you run the first example, count never makes it to 10, the numbers 0 all the way up to 9 are printed instead.   
```python 
# how long is the string 
string = 'How long is a piece of string?' 
count = 0
for i in range(len(string)):
    count +=1 
print(count)
```
```python
for i in range(sum(range(4, 10))):
    print(10 * i)
```
In these two examples, it's slightly more complicated to work out the integer after the calculation, but we know it will be a finite number. See if you can work out what these programs will print out without running them.   

## Nested Loops
All loops can also be nested inside each other consider this example:
```python
adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adjective:
  for y in fruits:
    print(x, y) 
```
In this example we iterate over two separate lists and join them together in the print statement. In the outside 'for' loop, x runs through each of the items in the variable 'adjective', then the inner 'for' loop is called and y iterates through the 'fruits' variable. When the outer loop gets to the first index, it runs the inner loop until it completes all it's iterations and then x moves onto the next index. In our example this means that 'x' first has the value 'red', then 'y' iterates through each of the 'fruits' list printing out 'red apple', 'red banana' and 'red cherry' first... Run the code for yourself and see.   
To see how many times an inner loop will run, you can multiply it by all the possible different options of the outer loops and the inner loop to find out. Consider this example:   
```python
number = ["3", "2", "1", "100"]
adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
count = 0
for x in number:
    for y in adjective:
        for z in fruits:
            count += 1
            print(x, y, z) 
total = len(number) * len(adjective) * len(fruits)   # Multiplied as explained
if count == total:
    print("We just proved how to calculate the number of times a loop runs!!")
    print(count)
else:
    print("Epic fail dood!!")
```
If you run this code, you can see that the code runs 36 times and that that's exactly the same number of times as each of list lengths multiplied together. There are some other niche cases you may see in loops, one of which is the 'else' statement.   
```python
number = ["3", "2", "1", "100"]
adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
count = 0
for x in number:
    for y in adjective:
        for z in fruits:
            count += 1
            print(x, y, z) 
        else:
            print("inside loop!")
    else: 
        print("inner loop")
else:
    print("outside loop!")
    print(count)
    print(len(number) * len(adjective) * len(fruits))
```
When the loop finishes, anything in the 'else' statement is executed. If the loop is broken out of or fails to execute, the 'else' statement doesn't execute. Try this for yourself:   
```python
number = ["3", "2", "1", "100"]
adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
count = 0
for x in number:
    for y in adjective:
        for z in fruits:
            break
        else:
            print("inside loop!")
    else: 
        print("inner loop")
else:
    print("outside loop!")
    print(count)
    print(len(number) * len(adjective) * len(fruits))
```

## Test Your Knowledge: Countdown
