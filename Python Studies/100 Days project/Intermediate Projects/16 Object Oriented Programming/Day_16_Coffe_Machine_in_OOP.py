# import another_module
# print(another_module.another_variable)

#Constructing Objects 

# from turtle import Turtle,Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("darkgreen")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()






# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name",["Pikachi","Squirtle","Charmander"])
# table.add_column("Type",["Eletric","Water","Fire"])

# table.align = "l"

# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_On = True

while is_On:
    chosen_coffe = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if chosen_coffe == 'off':
        is_On = False
    elif chosen_coffe == "report":
       coffee_maker.report()
       money_machine.report()
    else:
        drink = menu.find_drink(chosen_coffe)
        if coffee_maker.is_resource_sufficient(drink):    
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        