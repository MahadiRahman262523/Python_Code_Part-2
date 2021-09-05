'''
n = input("enter a text of number = ")

list = n.split()

sum = 0
for num in list :
    sum = sum + int(num)

print(sum)
'''

numOfLetter = 0
numOfWord = 0
numOfDigit = 0

text = input("enter your text = ")

for x in text :
    x = x.lower()
    if x >= 'a' and x <= 'z' :
        numOfLetter = numOfLetter + 1

    elif x >= '0' and x <= '9':
            numOfDigit = numOfDigit + 1

    elif x == ' ':
                numOfWord = numOfWord + 1


print("number of letter = ",numOfLetter)
print("number of digit = ",numOfDigit)
print("number of word = ",numOfWord+1)