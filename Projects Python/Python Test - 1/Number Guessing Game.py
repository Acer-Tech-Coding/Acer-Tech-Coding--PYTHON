import random

secret = random.randint(1, 50)

attempts = 0 

lives = 5

hints = 5

print("Welcome to the Number Guessing Game!")
print("You have 5 lives to guess the number I am thinking of.")
print("If you guess the number correctly, you win!")
print("If you run out of lives, you lose!")
print("For every wrong guess, you lose a life.")
print("But don't worry, I will give you hints to help you guess the number.")
print("\nI am thinking of a number between 1 and 50.")

while attempts < lives:

    guess = int(input("Guess a number between 1 and 50: "))

    if guess == secret:
        print("You win! The secret number was", secret)
    else:
        diff = abs(guess - secret)

        if diff >= 20:
            print("ice cold 🧊")
        elif diff >= 10:
            print("cold ❄️")
        elif diff >= 5:
            print("warm ♨️")
        else:
            print("hot 🔥🔥")

        attempts = attempts + 1

        for _ in range(5 - attempts):
            print("❤️", end=" ")
        print()

if guess != secret:
    print("You lost! The secret number was", secret)


