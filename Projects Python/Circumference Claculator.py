def calculate_circumference(radius):

    pi = 22/7
    circumference = 2 * pi * radius
    return circumference

print("Circumference Calculator")
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print("The circumference of the circle with radius", radius, "is:", circumference)
