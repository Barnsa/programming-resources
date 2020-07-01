# example-5.py first example
# showing that tuples are immutable by breaking things

# odds of being struck by lightning
tuple_as_a_record = ("lightning strike", (1, 700000))   
accident, (number_of_people, in_population) = tuple_as_a_record   # tuple unpacking

print(
    f"""The chance of being the victim of a {accident}, is {number_of_people} in {in_population}"""
)

# example-5.py second example
# showing that tuples are immutable by breaking things

tuple_as_a_record = ("meteor shower", (1, 20000))   
accident, (number_of_people, in_population) = tuple_as_a_record   # tuple unpacking

accident = "shark attack"
print(accident)
print(tuple_as_a_record)