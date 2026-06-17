Age = int(input("Enter your age: "))

if Age < 0:
    print("Invalid age. Age cannot be negative.")

elif Age >= 10 and Age <= 20:
    print("You are eligible!")