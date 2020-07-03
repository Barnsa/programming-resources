# example-1.py first example
# Precedence of or & and
meal = "Spaghetti Carbonara"

money = 0

if meal == "Spaghetti Carbonara" or meal == "Lasagne" and money >= 2:
    print("Dinner is served!!")
else:
    print("Can't deliver dinner :( ")
    
    
# example-1.py second example
# Fixed the order of precedents 
meal = "Spaghetti Carbonara"

money = 0

if (meal == "Spaghetti Carbonara" or meal == "Lasagne") and money >= 2:
    print("Dinner is served!!")
else:
    print("Can't deliver dinner :( ")