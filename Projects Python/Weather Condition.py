Current_Temperature = int(input("Enter the current temperature in Celsius: "))

if Current_Temperature < 0:
    print("The weather is freezing.")
    print("Make sure to wear warm clothes and stay safe.")
elif Current_Temperature > 30:
    print("The weather is hot.")
    print("Make sure to stay hydrated and wear light clothing.")
else:
    print("The weather is moderate.")
    print("Enjoy your day!")