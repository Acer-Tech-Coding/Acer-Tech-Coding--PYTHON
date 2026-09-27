class Employee:
    
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called, Employee deleted.")

def CreateEmployee():
    print("Making Employee")
    obj = Employee()
    return obj

print("Calling CreateEmployee() function")
obj = CreateEmployee()
print("Program Ended")

