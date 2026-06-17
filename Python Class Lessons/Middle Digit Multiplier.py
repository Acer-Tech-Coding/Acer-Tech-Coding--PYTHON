num = int(input("Enter a number: "))
t=num
numLen = 0

while t > 0:
    numLen = numLen + 1
    t = int(t / 10)


if numLen>=4:
    numLen = int(numLen/2)
    check = 0
    while num>0:
        rem

