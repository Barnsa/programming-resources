# example-6.py first example
# Showing complex nested loops with else statements
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


# example-6.py second example
# Showing broken complex nested loops with else statements
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