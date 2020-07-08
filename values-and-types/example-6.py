# example-6.py first example
# how to create a dictionary and how to fill it
our_dict = {
    "Boston":"Bruins",
    "Buffalo":"Sabres",
    "Detroit":"Redwings",
    "Florida":"Panthers",
    "Montreal":"Canadiens",
    "Ottawa": "Senators",
    "Tampa":"Lightning",
    "Toronto":"Maple Leafs"
}
print(type(our_dict))

our_dict["New Jersey"] = "Devils"

print(our_dict) 

print(our_dict.items())     ## prints out all the pairs of <keys>:<values>
print(our_dict.keys())      ## prints out all the <keys>
print(our_dict.values())    ## prints out all the <values>