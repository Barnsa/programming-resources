# Nested Loops, some examples of nested loops for 

number = ["3", "2", "1", "100"]
adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
count = 0

print("First Example")
for x in adjective:
  for y in fruits:
    print(x, y) 
    
    
print("\n")
print("Second Example")
for x in number:
    for y in adjective:
        for z in fruits:
            count += 1
            print(x, y, z) 
total = len(number) * len(adjective) * len(fruits)   # Multiplied as explained in the README.md
if count == total:
    print("We just proved how to calculate the number of times a loop runs!!")
    print(count)
else:
    print("Epic fail dood!!")