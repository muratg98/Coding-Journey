import random
print("Welcome to the best game of Rock, Paper, Scissors!")

#0 = rock
#1 = paper
#2 = scissors

RPS = ('rock', 'paper', 'scissors')
compnum = random.randint(0, 2)

while True:
    usernum = input("What do you choose?\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n")
    try:
        usernum = int(usernum)
    except:
        print("please enter a valid number between 0 and 2")
        continue
    if usernum == 0:
        print("you have chosen Rock")
        if compnum == 2:
            print("computer chose scissors\nYou Win!")
            continue
        elif compnum == 1:
            print("computer chose paper\nYou Lose!")
            continue
        else:
            print("computer chose rock\nIt's a Draw!")
            continue
    elif usernum == 1:
        print("you have chosen Paper")
        if compnum == 2:
            print("computer chose scissors\nYou Lose!")
            continue
        elif compnum == 1:
            print("computer chose paper\nIt's a Draw!")
            continue
        else:
            print("computer chose rock\nYou Win!")
            continue
    elif usernum == 2:
        print("you have chosen Scissors")
        if compnum == 2:
            print("computer chose scissors\nIt's a Draw!")
            continue
        elif compnum == 1:
            print("computer chose paper\nYou Win!")
            continue
        else:
            print("computer chose rock\nYou Lose!")
            continue
    else:
        print("please enter a integer between 0 and 2")
        continue
