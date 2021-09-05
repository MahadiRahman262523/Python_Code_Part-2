from random import randint

for i in range(1,6) :
    guessNumber = int(input("enter guessing number between 1 to 5 = "))
    randomNumber = randint(1,5)

    if guessNumber == randomNumber :
        print("You Have Won")
    else :
        print("You Have Lost")
        print("random number was = ",randomNumber)