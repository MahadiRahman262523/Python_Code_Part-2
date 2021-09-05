'''
def student(*details) :
    print(details)
    print(details[0])

student(177,"mahadi",3.46)
'''

def add(*num) :
    sum = 0
    for x in num :
        sum = sum + x
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)
add(10,20,30,40,50)

