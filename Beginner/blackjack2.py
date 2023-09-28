import random

import os

def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
comp_hand = []

def score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        11 == 1
        score = sum(hand)
    return score
def userdraw():
    while score(user_hand) < 21:
        draw = input("Type 'y' to get another card\nType 'n' to stick to your current hand\n ")
        if draw == 'y':
            user_hand.append(random.choice(cards))
            score(user_hand)
            if score(user_hand) == 21:
                print(f"Your hand is {user_hand}")
                print("Congratulations, you got 21!")
                break
            elif score(user_hand) > 21:
                print(f"Your score is: {score(user_hand)}")
                print("You Bust!")
                ##ideally code something here to skip the computers drawing turn and just ask if they wanna play again
                break
            print(f"Your hand is: {user_hand}, current score: {score(user_hand)}")
        elif draw == 'n':
            print(f"Your final hand is {user_hand}: final score: {score(user_hand)}")
            break
def compdraw():
    if score(user_hand) > 21:
        return
    while score(comp_hand) < 17:
        comp_hand.append(random.choice(cards))
        if score(comp_hand) > 21:
            print(comp_hand)
            print(f"The computer BUST with a score of {score(comp_hand)}")
            print("You Win!")
            return
    print(f"The computers final hand is {comp_hand}, final score: {score(comp_hand)}")

def check_scores():
    if score(user_hand) > 21 or score(comp_hand) > 21:
        return
    if score(user_hand) > score(comp_hand):
        print("You Win!")
    elif score(user_hand) < score(comp_hand):
        print("You Lose!")
    else:
        print("It's a Draw!")

def game():
    user_hand.append(random.choice(cards))
    user_hand.append(random.choice(cards))
    comp_hand.append(random.choice(cards))
    print(f"Your Cards {user_hand}, current score {score(user_hand)}")
    print(f"Computer Cards {comp_hand}, current score {score(comp_hand)}")
    userdraw()
    compdraw()
    check_scores()

playing = True
game()
while playing:
    is_play = input("Would you like to play again? Type 'y' for YES, or 'n' for NO: ")
    if is_play == 'y':
        user_hand.clear()
        comp_hand.clear()
        game()
    elif is_play == 'n':
        print("Thank You For Playing! ")
        playing = False