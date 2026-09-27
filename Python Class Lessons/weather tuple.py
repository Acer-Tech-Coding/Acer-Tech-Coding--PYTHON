weather = (1, 0, 0, 1, 1, 0, 1)

sunny_days = 0
rainy_days = 0
for i in range (0,7):
    if weather[i] == 1:
        sunny_days += 1
    else:
        rainy_days += 1

if sunny_days > rainy_days:
        print("The week was sunny.")

else:
        print("The week was rainy.")