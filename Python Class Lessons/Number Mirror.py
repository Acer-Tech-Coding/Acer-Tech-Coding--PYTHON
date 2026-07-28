try:
    number = int(input("Please Enter A Number."))
    print("The number you gave was:", number)
    
except ValueError as ex:
    print("Exeption:", ex)