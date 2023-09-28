from CoffeeMachinehold import *


def check_resources(coffee):
    for ingredient, value in MENU[coffee]["ingredients"].items():
        if resources[ingredient] - value < 0:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    else:
        return True


def get_coins():
    coffee_cost = MENU[coffee_request]["cost"]
    print(f"That will be ${coffee_cost}.")
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    pay = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) +(0.01 * pennies)
    if pay == coffee_cost:
        print(f"Here is your {coffee_request}. Enjoy! ")
        global money
        money += pay
        return True
    elif pay > coffee_cost:
        change = float(pay - coffee_cost)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_request}. Enjoy! ")
        money += pay
        return True
    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False


def calc_resources():
    for ingredient, value in MENU[coffee_request]["ingredients"].items():
        resources[ingredient] -= value
    return resources


money = 0

on = True
while on:
    coffee_request = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_request in MENU:
        if check_resources(coffee_request) is True:
            if get_coins() is True:
                calc_resources()
            else:
                continue
        else:
            continue
    elif coffee_request == 'report':
        for resource, amount in resources.items():
            print(f"{resource}: {amount}")
        print(f"money: ${money}")
    elif coffee_request == 'off':
        print("Switching Off")
        on = False
        break
    else:
        print("Please enter a valid input")
        continue














