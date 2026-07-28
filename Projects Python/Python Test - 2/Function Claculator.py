def add(num1, num2):

    return num1 + num2

def subtract(num1, num2):

    return num1 - num2

def multiply(num1, num2):

    return num1 * num2

def divide(num1, num2):

    return num1 / num2

print("Welcome to the Function Calculator!")
print("Here, you can perform basic arithmetic operations using python functions.")

try:
    Operation = float(input("Enter the desired operation: (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): "))

    if  Operation == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of addition is: {add(num1, num2)}")
    elif Operation == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif Operation == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif Operation == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of division is: {divide(num1, num2)}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")  

finally:
    print("Thank you for using the calculator!") 