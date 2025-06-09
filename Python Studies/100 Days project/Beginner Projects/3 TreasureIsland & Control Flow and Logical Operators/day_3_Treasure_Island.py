'''
print("Welcome to the rollercoaster!")
height = input("What is your height in cm?")

if int(height) > 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 7
        print("Child tickets pay $5.")
    elif age <= 18:
        bill = 7
        print("Youthtickets pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry,you have to grow taller before you can ride.")
'''

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# combined_names = name1+name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")

# first_digit = t + r + u + e
# second_digit = l + o + v + e

# score = int(str(first_digit)+str(second_digit))

# if(score<10) or(score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif(score<50) and (score>40):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
******************************************************************************* ''')

print("Welcome to Treasure Island.")
print("You mission is to find the treasure.")
choice1 = input('You\'re at a crossroad,where do you want to go? Type "left" or "right".').lower()

if choice1 == "right":
    print("You felll into a hole. Game Over")
else:
    print("You\'ve come to a lake. There is an island in the middle of the lake")
    choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2=="swim":
         print("You get attacked by an angry trout. Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.\n")
        choice3 = input("One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3 == "red":
            print("Game Over")
        if choice3 == "blue":
            print("Game Over")
        else:
            print("You found the treasure! You Win!")