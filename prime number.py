n = int(input("enter any positive number = "))

count = 0

for i in range(n) :
    if n %2 == 0 :
        count = count + 1
        break
        

if count == 0 :
    print("prime number")

else :
    print("not prime number")