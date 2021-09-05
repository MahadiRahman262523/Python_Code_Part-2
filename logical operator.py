'''
num1 = int (input("enter num1 value = "))
num2 = int (input("enter num2 value = "))
num3 = int (input("enter num3 value = "))
'''
'''
if num1 > num2 and num1 > num3 :
    print (num1)
elif num2 > num1 and num2 >num3 :
    print(num2)
else :
    print(num3)
'''
'''
if num1 > num2 or num1 > num3 :
    print (num1)
elif num2 > num1 or num2 >num3 :
    print(num2)
else :
    print(num3)
'''

ch = input("enter any character = ")

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
    print ("vowel")
else :
    print("consonant")