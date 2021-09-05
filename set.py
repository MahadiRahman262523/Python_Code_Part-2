num1 = {1,2,3,4,5}
#print(num1)

num2 = set([4,5,6,7])
#print(num2)
"""
num2.add(9)
print(num2)

num2.remove(8)
print(num2)

num2.remove(9)
print(num2)

print(4 in num1)
print(7 not in num1)
"""
print(num1 | num2) # | -> union
print(num1 & num2) # & -> intersection
print(num1 - num2) # - ->difference