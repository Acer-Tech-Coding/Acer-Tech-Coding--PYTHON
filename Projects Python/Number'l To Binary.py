# Decimal to Binary Converter

decimal = int(input("Enter a number number: "))

if decimal == 0:
    binary = "0"
else:
    binary = ""
    number = decimal

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

print("Binary value:", binary)
