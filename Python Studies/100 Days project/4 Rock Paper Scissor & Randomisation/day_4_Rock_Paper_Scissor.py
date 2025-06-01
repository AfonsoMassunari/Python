import random

# random_float = random.random()*5
# print(random_float)

coin_side = random.randint(0,1)

# if coin_side == 1:
#   print("Heads")
# else:
#   print("Tails")

# fruits = ["apple","pineapple","banana"]
# vegetables = ["tomato","potato","onion"]
# print(fruits[-1])
# print(fruits)
# fruits.extend(["orange","grapes"])
# print(fruits)
# disty_dozen = [fruits,vegetables]
# print(disty_dozen)

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# sorted_name = random.randint(0,len(names)-1)

# print(f"{names[sorted_name]} is going to buy the meal today!")

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?

# letter = position[0].lower();
# number = position[1];
# abc = ["a","b","c"]
# letter_index = abc.index(letter)
# number_index = int(position[1])-1
# map[number_index][letter_index] = "x"
# print(f"{line1}\n{line2}\n{line3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("\nUser choice:")
print(hand[user_choice])

computer_choice = random.randint(0,2)

print(f"Computer chose:\n{hand[computer_choice]}")

if(user_choice == computer_choice):
  print("it's a draw")

if user_choice>=3 or user_choice<0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif user_choice == 2 and computer_choice == 0:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif user_choice < computer_choice:
  print("You lose")