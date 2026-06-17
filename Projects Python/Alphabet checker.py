Input = input("Enter your value: ")

if Input == "a" or Input == "b" or Input == "c" or Input == "d" or Input == "e" or Input == "f" or Input == "g" or Input == "h" or Input == "i" or Input == "j" or Input == "k" or Input == "l" or Input == "m" or Input == "n" or Input == "o" or Input == "p" or Input == "q" or Input == "r" or Input == "s" or Input == "t" or Input == "u" or Input == "v" or Input == "w" or Input == "x" or Input == "y" or Input == "z":
    print("The value is an alphabet.")

elif Input == "A" or Input == "B" or Input == "C" or Input == "D" or Input == "E" or Input == "F" or Input == "G" or Input == "H" or Input == "I" or Input == "J" or Input == "K" or Input == "L" or Input == "M" or Input == "N" or Input == "O" or Input == "P" or Input == "Q" or Input == "R" or Input == "S" or Input == "T" or Input == "U" or Input == "V" or Input == "W" or Input == "X" or Input == "Y" or Input == "Z":
    print("The value is an alphabet.")

elif Input == "0" or Input == "1" or Input == "2" or Input == "3" or Input == "4" or Input == "5" or Input == "6" or Input == "7" or Input == "8" or Input == "9":
    print("The value is a digit, not an alphabet.")

elif Input == " ":
    print("The value is a space, not an alphabet.")

else:
    print("The value is neither an alphabet, nor a digit, nor a space.")
