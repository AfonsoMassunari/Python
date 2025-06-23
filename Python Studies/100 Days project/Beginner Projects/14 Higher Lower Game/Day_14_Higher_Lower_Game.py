# def is_prime(num):
#     half_num = int(num/2)
    
#     if(num != 2 and num%2==0):
#         return False
    
#     for n in range(3,half_num + 1, 2):
#         if(num%n==0):
#             return False
        
#     return  True

# if is_prime(2):
#     print("Prime")
# else:
#     print("Is_not_Prime")


# def increase_enemies(enemy):
#     enemy += 1
#     print(f"enemies inside function:{enemies}")
#     return enemy + 1

# enemies = 1

# enemies = increase_enemies(enemies)
# print(f"enemies outside function:{enemies}")

# try:
#     age = int(input("How old are you"))
# except ValueError:
#     print("You have typed in a an invalid number. Please try again with a numerical")
#     age = int(input("How old are you"))

# if age > 18:
#     print(f"You can drive at age {age}.")

# import random
# import maths

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item*2
#         new_item += random.randint(1,3)
#         new_item = maths.add(new_item,item)
#         b_list.append(new_item)
#     print(b_list)


# mutate([1,2,3,5,8,13])

from art import logo
from art import vs
from game_data import data
import random


def Higher_Lower_Game():
    
    game_over = False
    score = 0
    print(logo)

    while not game_over:

        id1 = random.randint(0,len(data)-1)

        while True:   
            id2 = random.randint(0,len(data)-1)

            if id2 != id1:
                break
    
        print(f"Compare A: {data[id1]['name']}, a {data[id1]['description']},from {data[id1]['country']}.")
        print(vs)
        print(f"Against B: {data[id2]['name']}, a {data[id2]['description']},from {data[id2]['country']}.")
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n"*30)
        print(logo)

        if player_choice == "a" and data[id1]["follower_count"] > data[id2]["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
        elif player_choice == "b" and data[id2]["follower_count"] > data[id1]["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
        else: 
            print(f"Sorry, that's wrong! Final score: {score}")
            game_over = True

Higher_Lower_Game()