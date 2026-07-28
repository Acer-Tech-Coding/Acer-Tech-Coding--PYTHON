try:
    num1,num2 = eval(input("Enter two numbers separated by a commma: "))

    result = num1 / num2
    print("The result of the division is:", result)

except ZeroDivisionError as ex:
    print("Exception: Cannot divide by zero.", ex)

except ValueError as ex:
    print("Exception: Invalid input. Please enter two numbers separated by a comma.", ex)

except SyntaxError as ex:
    print("Exception: Invalid input format. Please enter two numbers separated by a comma.", ex)

except:
    (print("An unexpected error occurred. Please try again."))

else:
    print("No Exeptions occurred. The division was successful.")

finally:
    print("Execution of the division operation is complete. The code executed.")



