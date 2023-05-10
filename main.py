from data import MENU
from data import resources
import sys


on = True
profit = 0
order = ""
paid = 0
change = 0


def print_report():
    """Prints report of how much of each ingredient, and how much money, are left"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${f'{profit:.2f}'}")


def take_order():
    """Prompt user by asking for order"""
    global order
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print_report()
    elif order == "off":
        sys.exit()
    elif order != "espresso" and order != "latte" and order != "cappuccino":
        print("Sorry, that's not on our menu.")
        take_order()
    check_resources()


def check_resources():
    """Checks if there are sufficient resources"""
    if order == "report":
        take_order()
    elif MENU[order]["ingredients"]["water"] > resources["water"]:
        print("Sorry. There is not enough water.")
        take_order()
    elif order != "espresso":
        if MENU[order]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry. There is not enough milk.")
            take_order()
    elif MENU[order]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry. There is not enough coffee.")
        take_order()


def insert_coins():
    """Processes money given"""
    global paid
    print("Please insert coins.")
    quarters = .25 * (int(input("How many quarters?: ")))
    dimes = .10 * (int(input("How many dimes?: ")))
    nickles = .05 * (int(input("How many nickles?: ")))
    pennies = .01 * (int(input("How many pennies?: ")))
    paid = quarters + dimes + nickles + pennies
    return paid


def transaction():
    """Completes transaction and provides change."""
    global change
    global profit
    if paid >= MENU[order]["cost"]:
        change = paid - MENU[order]["cost"]
        change_formatted = f'{change:.2f}'
        print(f"Your change is ${change_formatted}.")
        profit = profit + (paid - change)
        resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
        if order != "espresso":
            resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
        print_report()
        print(f"Here is your {order} ☕. Enjoy!")

    elif paid < MENU[order]["cost"]:
        print("Sorry. That's not enough money. Money refunded.")


while on:
    take_order()
    check_resources()
    insert_coins()
    transaction()
