marks = int(input("enter a marks = "))

if 80 <= marks <= 100 :
    print("A+")

elif 70 <= marks <= 79 :
    print("A")

elif 60 <= marks <= 69 :
    print("A-")

elif 50 <= marks <= 59 :
    print("B")

elif 40 <= marks <= 49 :
    print("D")

elif 33 <= marks <= 39 :
    print("pass")

else :
    print("fail")
