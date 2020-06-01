# Iterating Ranges, these are all of the examples that involve ranges

print("First Example")
for count in range(10):   # range(<stop>)
    print(count)

print("\n")
print("Second Example")
for count in range(4, 10):   # range(<start>, <stop>)
    print(count)

print("\n")
print("Third Example")
for count in range(1, 10, 3):   # range(<start>, <stop>, <increment>)
    print(count)

print("\n")
print("Fourth Example")
string = 'How long is a piece of string?' 
count = 0    
for i in range(len(string)):
    count +=1 
print(count)

print("\n")
print("Fifth Example")
for i in range(sum(range(4, 10))):
    print(10 * i)