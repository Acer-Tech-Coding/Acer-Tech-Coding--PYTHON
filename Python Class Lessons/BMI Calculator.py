height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

if BMI < 18.4:
    print("You are underweight")
    
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are normal weight") 

elif BMI >= 25 and BMI <= 29.9:
    print("You are overweight")

elif BMI >= 30 and BMI <= 34.9:
    print("You are severely overweight")

elif BMI >= 35 and BMI <= 39.9:
    print("You are obese")