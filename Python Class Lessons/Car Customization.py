print("Select your ride:")
print("1. Car")
print("2. Bike")
print("3. Truck")

vehicle_choice = input("Enter the number corresponding to your choice: ")

if vehicle_choice == "1":
    print("You have selected a Car.")
elif vehicle_choice == "2":
    print("You have selected a Bike.")
elif vehicle_choice == "3":
    print("You have selected a Truck.")
else:
    print("Invalid choice.")

print("\nCustomize your ride:")
color = input("Choose a color: ")
engine_type = input("Choose an engine type (e.g., V6, Electric): ")
print(f"\nYou have customized your ride with the following options:")
print(f"Color: {color}")
print(f"Engine Type: {engine_type}")

print("\nThank you for customizing your ride!")

print("\n See a summary of your choices!")
print("\nSummary of your choices:")
print(f"Vehicle Type: {vehicle_choice}")
print(f"Color: {color}")
print(f"Engine Type: {engine_type}")

print("\nGoodbye!")

