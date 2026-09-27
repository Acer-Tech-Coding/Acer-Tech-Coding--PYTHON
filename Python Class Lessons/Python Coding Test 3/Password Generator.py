import random
import string

length = int(input("Enter password length (minimum 3): "))

if length < 3:
    print("Password length must be at least 3.")
else:
    password_characters = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]

    all_characters = string.ascii_letters + string.digits

    for _ in range(length - 3):
        password_characters.append(random.choice(all_characters))

    random.shuffle(password_characters)
    password = "".join(password_characters)

    print("Generated password:", password)
