string = input("Enter a string: ")

character = input("Enter a character to be checked from your string - " + string + ": ")

i = 0

count = 0

while i < len(string):

    if string[i] == character:
        count += 1
    i += 1

print("The character " + character + " appears " + str(count) + " times in the string " + string)


