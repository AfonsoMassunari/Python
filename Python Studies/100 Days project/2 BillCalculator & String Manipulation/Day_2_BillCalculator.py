# print("Hello"[4])

# num_char = len(input("What is your name?"))
# print(type(num_char))
# new_num_char = str(num_char)

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(70)+str(100))

# two_digit_number = input()
# type(two_digit_number) 
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# height = input()
# weight = input()

# weight_as_int = int(weight)
# height_as_float = float(height)

# bmi = weight_as_int/height_as_float**2

# bmi_as_int = int(bmi)

# print(bmi_as_int)

# print(round(8/3,2))
# print(round(2.5555555,2))
# print(int(8/3))
# print(8//3)

# score = 0
# height = 0
# print(f"your score is{score},your height{height}")

# age = input("age: ")
# age_left = (90-int(age))*(52)
# print(f"You have {age_left} weeks left.")

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
total_people = int(input("How many people to split the bill? "))
value_for_each_person = round((total_bill + total_bill*(tip/100))/total_people,2)
print(f"Each person should pay: ${value_for_each_person}")
