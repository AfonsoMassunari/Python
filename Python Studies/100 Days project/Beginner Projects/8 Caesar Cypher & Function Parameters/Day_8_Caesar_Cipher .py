# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")
    

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name} ?")
#     print(f"Isn't the weather nice {name}?")


# greet_with_name("afonso")

# def life_in_weeks(age):
#     weeks = (90 - age)*52
#     print(f"You have {weeks} weeks left.")
    
# life_in_weeks(22)

# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with(name = "Afonso Massunari",location = "Japan")

# def calculate_love_score(name1,name2):
#     combined_names = name1+name2
#     lower_combined_names = combined_names.lower()
#     T = lower_combined_names.count("t")
#     R = lower_combined_names.count("r")
#     U = lower_combined_names.count("u")
#     E = lower_combined_names.count("e")
    
#     L = lower_combined_names.count("l")
#     O = lower_combined_names.count("o")
#     V = lower_combined_names.count("v")
#     E = lower_combined_names.count("e")

#     first_digit = T + R + U + E
#     second_digit = L + O + V + E 

#     result = (str(first_digit) + str(second_digit))
#     print(result)

# calculate_love_score("Kanye West", "Kim Kardashian")


# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# direction = input("Type 'encode' to encrypt,type 'decode' to decrypt\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(original_text,shift_amount):
#     cypher = ''
#     for letter in original_text:
#         position = (alphabet.index(letter) + shift_amount) % 27
#         cypher += alphabet[position]
    
#     print(f"Here is the encoded result: {cypher}")


# def decrypt(original_text,shift_amount):
#     output_text = ''
#     for letter in original_text:
#         position = (alphabet.index(letter) + shift_amount) % 27
#         output_text += alphabet[position]

#     print(f"Here is the decoded result: {output_text}")

# if direction == "encode":
#     encrypt(text,shift)
# else:
#     decrypt(text,shift)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:

            shifted_position = (alphabet.index(letter) + shift_amount)%len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the decoded result:{output_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)

    should_restart = input("Type 'yes' if you want to continue ou 'no' if you want to stop\n")

    if(should_restart == "no"):
        should_continue = False


