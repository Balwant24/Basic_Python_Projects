import random

easy_words = ["apple", "banana", "mango", "orange", "grapes", "papaya", "pineapple"]
medium_words = ["tiger", "lion", "elephant", "monkey", "dog", "cat", "horse"]
hard_words = ["computer", "laptop", "keyboard", "internet", "software", "hardware"]

print("Welcome to the password guessing game!!")
print("Choose a difficulty level : easy, medium or hard")
level = input("Difficulty level : ").lower()
if level == "easy":
    print("You have chosen easy level. Your 1st hint is the word is a fruit.")
    secret = random.choice(easy_words)
elif level=="medium":
    print("You have chosen medium level. Your 1st hint is the word is an animal.")
    secret = random.choice(medium_words)
elif level=="hard":
    print("You have chosen hard level. Your 1st hint is the word is related to computers.")
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts+=1

    if guess == secret:
        print(f'Congratulations! You guessed it in {attempts} attempts.')
        break

    hint = ""


    for i in range(len(secret)):
        if i<len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        
        else:
            hint+="_"
    print("Hint:" + hint)
print("Game Over!!")

