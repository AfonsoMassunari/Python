# def function_1(text):
#     return text + " " + text

# def function_2(text):
#     return text.title()

# output = function_2(function_1("hello"))
# print(output)

# This is a Docstrings

# def format_name(f_name,l_name):
#     """Take a fisrt and last name and format ir to return the title case version of the name"""
#     if f_name == "" or l_name == "":
#         return "You did not provid valid inputs"
#     format_f_name = f_name.title()
#     format_l_name = l_name.title()
#     return f"{format_f_name} {format_l_name}"

# print(format_name(input("What is your first name?"),input("What is your last name?")))

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else: 
#                 return False
#         else:
#             return True
#     else:
#         return False

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_reuse = True
    first_number = float(input("What´s your first number? "))

    while should_reuse is True:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an Operation: ")
        second_number = float(input("What´s the next number? "))
        answer = operations[operation](first_number,second_number)

        print(f"{first_number} {operation} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = answer
        else:
            should_reuse = False
            print("\n" * 20)
            calculator()

calculator()