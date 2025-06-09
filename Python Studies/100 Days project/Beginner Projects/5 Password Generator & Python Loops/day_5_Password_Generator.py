import random
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit +"pie")

# #Input a Python list of student heights
# student_heights = input().split()

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total_height = 0
# for height in student_heights:
#   total_height += height

# print(f"total height = {total_height}")
# print(f"number of students = {len(student_heights)}")
# print(f"average height = {round(total_height/len(student_heights))}")



# target = int(input()) # Enter a number between 0 and 1000
# even_sum = 0
# for number in range(2,target+1,2):
#   even_sum += number
# print(even_sum)

# for number in range(1,101):
#   if number%3==0 and number%5==0:
#     print("FizzBuzz")
#   elif number%3 == 0:
#     print("Fizz")
#   elif number%5 == 0:
#     print("Buzz")
#   else:
#     print(number)
    
    
    
    
    
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols = ['!','@','#','$','%','^','&','*','(',')','-','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']


print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(1,n_letters+1):
  password_list.append(random.choice(letters))

for char in range(1,n_numbers+1):
  password_list.append(random.choice(numbers))

for char in range(1,n_symbols+1):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)
"""password_list = [password_list[i] for i in random.sample(range(len(password_list)),len(password_list))]"""

password = ""
for i in password_list:
  password += i
  
print(f"Here is your password:{password}")