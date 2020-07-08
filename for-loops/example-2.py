# example-2.py
# iterating iterables, a basic example of a counting loop in python 3 
word = 'banana'
count = 0 
for letter in word:
    if letter is 'a':
        count = count + 1   # count +=1 would also work here
print(count)