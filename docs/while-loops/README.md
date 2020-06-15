# Iteration or Loops 

Anytime you want to do anything more than once in a Python program, you should consider putting it inside a loop.  
There are two types of loops in python, a 'for' loop and a 'while' loop. Generally 'for' loops are used when you know the amount of times you want to repeat something. It doesn't have to be an exact integer value, it can also be anything easily calculable. 'While' loops are used when you aren't sure how many times you need to repeat something or you need to do something recursively.    
In python, all control statements use indentation to define blocks of grouped code.   

# While Loops (indefinite iteration)
In 'while' loops, there is a definite shape to the way every one of them is written. Every 'while' loop is this kind of shape:   
```python
while <condition>:
    <statements>
<additional statements>
```
The condition is to indicate when the loop must stop, the statements must contain something you want to do repetitively, and the additional statements are things such as the 'else' statement that we saw in the 'for' loop examples too. Consider this simple while loop:   
```python
count = 5 
while count > 0:
    print(count)
    count -= 1
    if count == 2:
        break
else: 
    print("Loop finished.")
```
Can you figure out what it does??     
In this example we have a variable called count that stores a value (5), this number has to be on the outside of the loop so that it can be properly modified, if it was inside the loop then it wouldn't change because each iteration of the loop would create it's own version of the variable due to the rules of scope. The check is run for the loop, which determines that the value of count is greater than zero, so runs the loop.   
We first print the value of count, we do this first because if we decrement count first then we would print out the value '4' not '5'. Next we decrement the count by 1, this statement is the same as `count = count - 1`. The 'if' statement looks to see if the value of count is 2, and if it is to break out of the while loop. The 'else statement only activates when the while loop successfully runs and exits naturally, so it never runs here because the break statement gets tripped.    

## Example 'while' loops
Here are a few 'while' loops to give you some ideas of the kinds of ways you might use them:   
```python
# Search and index
pet = ["dog", "cat", "rabbit", "snake", "octopus", ]
search = "buffalo"
i = 0 
while i < len(pet):
    if pet[i] == search:
        # we would have found search in pet
        print(f"We found the search term in index {i}.")
        break
    i += 1
else:
    # We didn't find the search item in the list
    print("We didn't find the search term!")
```
```python
# Simplified executable run loop 
check = True
count = 1
while check:
    if count == 1:
        print("This program will continue to run until you tell it to stop!")
        print("Do you want to stop yet?")
    if count != 1:
        print("How about now? ")
    answer = input().lower()
    stop_commands = ["stop", "exit", "yes", "sure", "get me out of here you filthy mudblood!"]
    count += 1
    if answer in stop_commands:
        answer = input("Are you sure? ").lower()
        if answer in stop_commands:
            break 
```
```python

```