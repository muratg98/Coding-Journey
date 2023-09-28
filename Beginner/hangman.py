import random
import hangmanart
import hangmanwords

from hangmanart import stages
from hangmanart import logo
print(logo)
end_of_game = False
from hangmanwords import word_list
chosen_word = random.choice(word_list)
lives = 6
word_length = len(chosen_word)
display = []
#display = display.extend([' _ '] * len(chosen_word))
for _ in range(word_length):
    display += "_"

#print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            print(f"Well done! {guess} is in the word")
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word! You lose a life")
        lives -= 1
        print(f"you have {lives} lives remaining")
        if lives == 0:
            end_of_game == True
            print("You Lose! ")
            break
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
