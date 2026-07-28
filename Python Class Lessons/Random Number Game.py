import random
playing = True
number = random.randint(1, 10)

while playing:
    guess = input("Guess a number between 1 and 10 (or type 'exit' to quit): ")
    
    if guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    
    try:
        guess = int(guess)
        
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue
        
        if guess == number:
            print("Congratulations! You guessed the correct number!")
            playing = False
        else:
            print("Sorry, that's not the correct number. Try again!")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
