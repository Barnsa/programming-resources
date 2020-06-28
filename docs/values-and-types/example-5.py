# example-5.py 
# showing that tuples are immutable by breaking things

# odds of being struck by lightning
tuple_as_a_record = ("Lightning strike", 1, 700000)   
accident, number_of_people, in_population = tuple_as_a_record   # tuple unpacking

print(
    f"""The chance of being the victim of a {accident}, is {number_of_people} in {in_population}"""
)