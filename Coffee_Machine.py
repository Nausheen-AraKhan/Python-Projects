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
}
def is_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry, {item} is insufficient")
            is_enough = False
    return is_enough
def process_coins():
    total = 0
    print("Please insert coins: ")
    total+=int(input("How many quarters?"))*0.25
    total+=int(input("How many dimes?"))*0.10
    total+=int(input("How many nickles?"))*0.05
    total+=int(input("How many pennies?"))*0.01
    return total
def transaction(money,cost):
    if money>=cost:
        change=round(money-cost,2)
        global profit
        profit+=money
        print(f"Here is your change: {change}")
        return True
    else:
        print("Sorry, you don't have enough money")
        return False
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your coffee: {drink_name}☕️. Enjoy!")
profit=0
is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        print(drink)
        if is_sufficient(drink["ingredients"]):
            payment=process_coins()
            if transaction(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])


