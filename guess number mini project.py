import random

print("🎲 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

# Step 1: Generate random number
secret_number = random.randint(1, 100)

# Step 2: Start guessing loop
while True:
    guess = input("Enter your guess: ")
    
    # Input validation
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    
    # Step 3: Compare guess
    if guess < secret_number:
        print("Too low. Try again!")
    elif guess > secret_number:
        print("Too high. Try again!")
    else:
        print(f"🎉 Correct! The number was {secret_number}. You win!")
        break
