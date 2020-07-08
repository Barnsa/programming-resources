# example-2.py
# Showing order of precedence through examples
# As all of these have the same precedence, 
# they get evaluated starting from left-right:
print(3 // 2 * 3)  
print(3 * 2 // 3)
print(3 * 2 % 6)
print(2 % 6 * 3)
print(6 + 3 - 7)
print(6 - 7 + 3)

# Right to left precedence happens with **
# Output: 512, since 2**(3**2) = 2**9
print(2 ** 3 ** 2)

# If 2 needs to be the first exponent evaluated, we need to use ()
# Output: 64, since (2**3)**2 = 8**2 
print((2 ** 3) ** 2)