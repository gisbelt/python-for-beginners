# math stuff: operators behave the same when using literal numbers (such as 42) or variables. 
# sum 
answer = 30 + 12
print(answer) # output: 42

# subtract 
difference = 30 - 12
print(difference) # output: 18

# multiply
product = 30 * 12
print(product) # output: 360

# divide 
quotient = 30 / 12
print(quotient) # output: 2.5
# Imagine converting a number of seconds into minutes and seconds for display purposes 
# determine the number of minutes in 1042 seconds. 
# With 60 seconds in a minute, you can divide by 60 and get an answer of 17.3666667. 
# The number you are interested in is simply 17. 
# It is recommended that you round down, using what is known as lower multiple division. 
# To perform such a division in Python, you must use // 
# The next step is to determine the number of seconds. 
# This number is the remainder of 1042 if you divide by 60.
# To find the remainder, use the modulus operator, which in Python is %. 
# The remainder of 1042 / 60 is 22, which is the value that the modulus operator will provide.
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60
print(display_minutes) # output: 17
print(display_seconds) # output: 22

# int(), float()
# int is used to perform the conversion to an integer number and float is used to convert to a floating point number.
# The key difference between the two is the existence of a decimal separator
demo_int = int('215')
print(demo_int) # output: 215
demo_float = float('215.3')
print(demo_float) # output: 215.3

# abs()
# Absolute values: an absolute value is a non-negative number without its sign.
# Use abs para convertir el valor negativo en su valor absoluto. 
# Si hace la misma operación mediante abs (e imprime las respuestas), verá que muestra 23 para ambas ecuaciones
print(abs(39 - 16)) # output: 23
print(abs(16 - 39)) # output: 23

# round()
# Use it to round up to the nearest integer if the decimal value is greater than .5, or down if it is less than .5. 
# If the decimal value is equal to .5, the function rounds up or down to the nearest even integer. 
print(round(1.4)) # output: 1
print(round(1.5)) # output: 2
print(round(2.5)) # output: 2
print(round(2.6)) # output: 3

# math 
# math library 
# math allows rounding with floor and ceil, providing the value of pi and many other operations. 
# You can choose to always round up to the nearest whole number if you use ceil, or down if you use floor 
from math import ceil, floor
round_up = ceil(12.5)
print(round_up) # output: 13
round_down = floor(12.5)
print(round_down) # output: 12



# *********************************************************************************************************


# Python respects the order of operations in mathematics. 
# The order of operations determines that expressions must be evaluated in this order:
# 1. parentheses
# 2. Exponents
# 3. Multiplication and division
# 4. Addition and subtraction
# Using parentheses allows you to ensure that the code executes in a predictable manner and the code is easier to read and maintain. 
result_1 = 1032 + 26 * 2
print(result_1)
result_2 = 1032 + (26 * 2)
print(result_2)
# The output is the same in both cases: 1084. 

# run: python math-operations.py 