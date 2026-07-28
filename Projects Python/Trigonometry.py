import math

x = int(input("Enter a number to find its square root: "))
print("The square root of", x, "is:", math.sqrt(x))

y = int(input("Enter a number to find its absolute value: "))
print("The absolute value of", y, "is:", math.fabs(y))

z = int(input("Enter a number to be raised to a power: "))
p = int(input("Enter the power to which the number should be raised: "))

print(z, "raised to the power of", p, "is:", math.pow(z, p))

a = int(input("Enter a number to be copied: "))
b = int(input("Enter the number of times to copy the number: "))

print("The number", a, "copied", b, "times is:", math.copysign(a, b))

