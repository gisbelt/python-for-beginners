print('Hello, World!')
# print() 
print("show this in the console")

# variables 
sum = 1 + 2 # 3
product = sum * 2
print(product)

# type() 
distance_to_alpha_centauri = 4.367 # looks like a float
print(type(distance_to_alpha_centauri)) ## <class 'float'>

# operator: <left side> <operator> <right side>
left_side = 10
right_side = 5
result = left_side / right_side # 2
print(result)

# date, import datetime, ex: date.today()
from datetime import date
print(date.today())
print("Today's date is: " + str(date.today())) ## convert date to string

# exercise: Build a unit converter
parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

# input(): capture user data
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)
## calculator program 
print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print("The sum is: ", int(first_number) + int(second_number)) ## The input() function stores a result as a string, change these strings to numbers using the int() function

# exercise: Build a unit converter accepting user input
parsecs_input = input("Enter the number of parsecs: ")
parsecs = int(parsecs_input)
lightyears = parsecs * 3.26
print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")


# run: python hello.py 