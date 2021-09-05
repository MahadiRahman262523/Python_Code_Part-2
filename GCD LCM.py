num1 = int(input("enter number 1 = "))
num2 = int(input("enter number 2 = "))

n1 = num1
n2 = num2

while n2 != 0 :
    rem = n1%n2
    n1 = n2
    n2 = rem


gcd = n1
lcm = (num1 * num2)/gcd

print("GCD = ",gcd)
print("LCM = ",lcm)
