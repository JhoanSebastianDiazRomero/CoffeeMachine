MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def enough_resources():
    for ingredient in drink_ingredients:
        if resources[ingredient] - drink_ingredients[ingredient] < 0:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def calculate_coin_total():
    total = 0
    print("Please insert coins.")
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def process_successful_transaction():
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    resources['money'] += drink['cost']

    if coin_total > drink['cost']:
        print(f"“Here is ${round(coin_total - drink['cost'], 2)} dollars in change.” ")

    print(f"Here is your {order}☕️. Enjoy!")


machine_on = True

while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        drink = MENU[order]
        drink_ingredients = drink['ingredients']
        if enough_resources():
            coin_total = calculate_coin_total()
            if coin_total < drink['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                process_successful_transaction()
    elif order == 'report':
        print_report()
    elif order == "off":
        machine_on = False
