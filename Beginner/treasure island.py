print("Welcome to Treasure Island\nYour mission is to find the treasure.")

def crossroads():
    while True:
        cr = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
        if cr == 'left' or cr == 'right':
            return cr
        else:
            print("please enter either 'left' or 'right'\n")
            continue

def lake():
    while True:
        l = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' for a boat. Type 'swim' to swim across.\n")
        if l == 'wait' or l == 'swim':
            return l
        else:
            print("please enter either 'wait' or 'swim'\n")
            continue

def doors():
    while True:
        drs = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you choose?\n")
        if drs == 'red' or drs == 'yellow' or drs == 'blue':
            return drs
        else:
            print("please enter either 'red', 'yellow', or 'blue'\n")
            continue

def main():
    direction = crossroads()
    if direction == 'right':
        print("you fall into a hole bruh")
        return
    action = lake()
    if action == 'swim':
        print("you drowned... wa wah wahhh")
        return
    house = doors()
    if house == 'red':
        print("you enter fire and die")
        return
    elif house == 'blue':
        print("eaten by beasts. game over")
        return
    print("you found the treasure! you win!")

main()




