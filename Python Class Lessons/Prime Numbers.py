Starting = int(input("Enter the starting number: "))
Ending = int(input("Enter the ending number: "))

print("The prime numbers between " + str(Starting) + " and " + str(Ending) + " are:")

for num in range(Starting, Ending + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)