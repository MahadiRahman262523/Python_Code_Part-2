#list comprehension for map function
#def square(x) :
 #   return x*x

num = [1,2,3,4,5]

#result = list(map(square,num))

result = [x*x for x in num]
print(result)