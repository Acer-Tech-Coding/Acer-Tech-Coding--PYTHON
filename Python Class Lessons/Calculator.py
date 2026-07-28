def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select operation:")
print("1. Add (a)")
print("2. Subtract (b)")
print("3. Multiply (c)")
print("4. Divide (d)")

choice = input("Enter choice (a/b/c/d): ")

print("Enter two numbers:")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 'b':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 'd':
    if num2 != 0:
        print(num1, "/", num2, "=", divide(num1, num2))
    elif num2 == 0:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid input. Please select a valid operation (a/b/c/d).")