try:
    age = int(input("Please enter your age: "))
    if age %2 == 0:
        print("You are even-aged!")
        
    elif age %2 != 0:
        print("You are odd-aged!")


except ValueError as ex:
    print("Exception: Invalid input. Please enter a valid number.", ex)

except SyntaxError as ex:
    print("Exception: Invalid input format. Please enter a valid number.", ex)

except:
    print("An unexpected error occurred. Please try again.")

finally:
    print("Execution of the age verification operation is complete. The code executed.")
    print("Thank you for using the Age Verifier program. Goodbye!")