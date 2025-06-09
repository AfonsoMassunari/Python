from Coffe_Machine_data import MENU
from Coffe_Machine_data import resources

profit = 0
is_On = True

def is_resource_sufficient(order_ingridient):
    """Return True when are enought ingredients, False if ingredients are insufficient"""
    for item in order_ingridient:
        if order_ingridient[item] > resources[item]:
            print(f"Sorry there is not enought {item}.")
            return False
    return True

def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters? "))*0.25
    total += int(input("how many dimes? "))*0.10
    total += int(input("how many nickles? "))*0.05
    total += int(input("how many pennies? "))*0.01
    return total

def is_transaction_sucessful(money_received,drink_cost):
    """Returen Trye when the payment is acccepted, or False if money is insfficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        return True
    else:
        print(f"Sorry that's not enought money. Money refunded {money_received}.")
        return False
    
def make_coffee(drink_name,order_ingridients):
    """Deduct the required ingridients from the resources."""
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"Here is your {drink_name} ☕")


while is_On:
    chosen_coffe = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if chosen_coffe == 'off':
        is_On = False
    elif chosen_coffe == "report":
       print(f"Water: {resources['water']} ml")   
       print(f"Milk: {resources['milk']} ml")
       print(f"Coffee: {resources['coffee']} ml")
       print(f"Money: ${profit}")
    else:
        drink = MENU[chosen_coffe]
        if is_resource_sufficient(drink['ingredients']):    
            payment = process_coins()
            if is_transaction_sucessful(payment,drink['cost']):
                make_coffee(chosen_coffe,drink["ingredients"])
        