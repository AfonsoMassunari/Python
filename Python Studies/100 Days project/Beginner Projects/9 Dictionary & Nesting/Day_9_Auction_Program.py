# programming_dictionary = {
#     "Bug":"An error in a program",
#     "Function":"A piece of code that you can easely call"
# }

# print(programming_dictionary["Function"])

# programming_dictionary["Loop"] = "The action of doing something over and over again"

# print(programming_dictionary)


# empty_dictionary  = {}

# programming_dictionary["Bug"] = "A moth in your computer."

# print(programming_dictionary)

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])



# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])



# travel_log = {
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"],
# }

# print(travel_log["France"][1])



# travel_log = {
#     "France":{
#         "cities_visited":["Paris","Lille","Dijon"],
#         "total_visits":12,
#         },

#     "Germany": {
#         "cities_visited": ["Stuttgart","Hamburg","Berlin"],
#         "total_visits":8
#     },
# }

# print(travel_log["Germany"]["cities_visited"][2])


# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for student in student_scores:
#     if student_scores[student] > 90:
#         grade = "Outstanding"
#     elif student_scores[student] > 80:
#         grade = "Exceeds Expectations" 
#     elif student_scores[student] > 70:
#         grade = "Acceptable"  
#     elif student_scores[student] <= 70:
#         grade = "Fail" 
    
#     student_grades[student] = grade

# Nested List in Dictionary

from art import logo

print(logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    
    # max(bidding_dictionary,key=bidding_dictionary.get)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

should_continue = True

bidders_list = {}

while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders_list[name] = bid;
    restart = input("Are there any other bidders? Type 'yes or 'no'.")

    if restart == "no":
        should_continue = False
        find_highest_bidder(bidders_list)
    elif restart == "yes":
        print("\n"*20)
    
    


