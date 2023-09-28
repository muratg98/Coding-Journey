import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1, 100)
attempts = 0

def easy():
    global attempts
    attempts = 10
    print(f"You chose Easy Mode! You have {attempts} attempts to guess the number.")
    return attempts

def hard():
    global attempts
    attempts = 5
    print(f"You chose Hard Mode! You have {attempts} attempts to guess the number.")
    return attempts

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        easy()
        break
    elif difficulty == 'hard':
        hard()
        break
    else:
        print("That is not a valid input.")

while attempts != 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer is {number}.")
        break
    elif guess > number:
        print("Too High.")
        attempts -= 1
        print(f"You have {attempts} remaining to guess the number.")
    elif guess < number:
        print("Too Low.")
        attempts -= 1
        print(f"You have {attempts} remaining to guess the number.")
if attempts == 0:
    print(f"You failed to find the number! It was {number}")

