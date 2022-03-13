# |              |   espresso   |    latte     |  cappuccino  |
# | water (ml)   |      50      |     200      |     250      |
# | coffee (g)   |      18      |      24      |      24      |
# | milk  (ml)   |      --      |     150      |     100      |
# | price ($)    |     1.50     |     2.50     |     3.00     | 
# -------------------------------------------------------------

# coins: 
# penny - 1 ($0.01)
# nickel - 5 ($0.05)
# dime - 10 ($0.10)
# quarter - 25 ($0.25)


# machines has:
# water 300 ml
# milk 200 ml
# coffee 100 g 
# money 0 $


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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

import json

# print 'report'
menu_json = json.loads(json.dumps(MENU))
resources_json = json.loads(json.dumps(resources))


def print_report():
    print("water" + resources_json["water"])
    print("milk" + resources_json["milk"])
    print("coffee" + resources_json["coffee"])

def espresso(resources_json):
    resources_json["coffee"] = resources_json["coffee"] - menu_json["espresso"]["ingredients"]["coffee"]

while True:

    print("espresso coffee:" + str(menu_json["espresso"]["ingredients"]))

    # input = input("choose coffee (espresso,latte,cappuccino): ")
    if (input == "report"):
        print_report()
    elif (input == "espresso"):
        espresso(resources_json)


    break
