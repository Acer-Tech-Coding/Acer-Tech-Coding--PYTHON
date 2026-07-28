import math

print(
    "The Floor and Ceiling of 3.7 is: ", math.floor(3.7), "and", math.ceil(3.7)

    
)

x = int(input("Enter a number to find its square root: "))



print("The square root of", x, "is:", math.sqrt(x))

a = int(input("Enter a number to find its absolute value: "))
print("The absolute value of", a, "is:", math.fabs(a))




y = int(input("Enter a number to be raised to a power: "))
z = int(input("Enter the power to which the number should be raised: "))
print(y, "raised to the power of", z, "is:", math.pow(y, z))




m = int(input("Enter a number to be copied."))
n = int(input("Enter the number of times to copy the number."))
print("The number", m, "copied", n, "times is:", math.copysign(m, n))    



