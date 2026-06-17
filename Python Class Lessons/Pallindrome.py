string = input("Enter a string: ")

string2 = ('')

for i in string:
    string2 = i + string2
print("The reverse of the string is: " , string2)

if string == string2:
    print("The string is a palindrome! The reverse of " + string + " is: " , string2)
         