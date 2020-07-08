# Iterating Ranges, these are all of the examples that involve ranges

# example-4.py first example
for count in range(10):   # range(<stop>)
    print(count)

# example-4.py second example
for count in range(4, 10):   # range(<start>, <stop>)
    print(count)

# example-4.py third example
for count in range(1, 10, 3):   # range(<start>, <stop>, <increment>)
    print(count)

# example-4.py fourth example
string = 'How long is a piece of string?' 
count = 0    
for i in range(len(string)):
    count +=1 
print(count)

# example-4.py fifth example
for i in range(sum(range(4, 10))):
    print(10 * i)