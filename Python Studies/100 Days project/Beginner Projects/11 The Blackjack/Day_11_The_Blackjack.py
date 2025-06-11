import random

def deal_card():
    cards = [11,2,3,4,5,7,8,9,10,10,10,10]
    player_card = random.choice(cards)
    return player_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards) #sum all elements of the list

def compare(p_score,c_score):
    if p_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose, opponent has a Blackjack"
    elif p_score == 0:
        return "You win, you have a Blackjack"
    elif p_score > 21:
        return "You lose, You went over"
    elif c_score > 21:
        return "You win, Oponnent went over" 
    elif p_score > c_score:
        return "You win"
    else:
        return "You lose"

def BlackJack():
    player_cards = []
    computer_cards = []
    computer_score = -1
    player_score = -1
    is_game_over = False

    for _ in range (2): 
        player_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards:{player_cards}, current score:{player_score}")
        print(f"Computer's  first card:{computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score >= 21 :
            is_game_over = True
        else:
            player_get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_get_another_card == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n"*20)
    print(f"Your final hand:{player_cards}, final score:{player_score}")
    print(f"Computer's final hand:{computer_cards}, final score:{computer_score}")
    print(compare(player_score,computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*20)
    BlackJack()

