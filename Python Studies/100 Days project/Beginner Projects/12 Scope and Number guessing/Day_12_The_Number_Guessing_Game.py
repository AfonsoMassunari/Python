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

import random

def guess_number():
    print("Welcome to the Guessing Game!\nI'm thinking of a number between 1 and 100")
    difficulty = input("Type 'easy' or 'hard': ")
    
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    game_over = True

    number = random.randint(1,100)

    while game_over:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a Guess: "))

        if number == guess:
            print(f"You got it! The answer was {number}")
            game_over = False
        elif number > guess:
            print("Too low.")
            print("Guess again.")
        else:
            print("Too High.")
            print("Guess again.")

        attempts -= 1

        if attempts == 0:
            game_over = False

guess_number()