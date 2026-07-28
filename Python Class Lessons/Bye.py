valid = False
while not valid:
    try:
        user_input = int(input("Please enter a number: "))
        while user_input % 2 == 0:
            
        
            print("Bye")
    except ValueError:
        print("Invalid input. Please enter a valid number.")  

    