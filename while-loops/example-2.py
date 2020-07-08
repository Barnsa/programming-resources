# example-2.py
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
