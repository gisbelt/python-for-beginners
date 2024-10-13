# methods
# .title(): 
# returns the string in uppercase and can be used directly with a string 
print("temperatures and facts about the moon".title())
heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

# .split()
# Without arguments, the method will separate the string into each space. 
# This would create a list of all the words or numbers separated by a space 
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)
# output: ['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F'] 
# In this example, it works with multiple lines, so the (implicit) newline character 
# can be used to split the string at the end of each line, and create unique lines: 
temperatures2 = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures2.split('\n')
print(temperatures_list)
# output: ['Daylight: 260 F', 'Nighttime: -280 F'] 

# .find() 
# An approach to search for the position of a specific word in a string
# The .find() method returns -1 when the word is not found, or returns the index (the number representing the position in the string). 
temperatures3 = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures3.find("Moon"))
# output: -1 
temperatures4 = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures4.find("Mars"))
# output: 64 

# .count()
# returns the total number of repetitions of a given word in a string: 
temperatures5 = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures5.count("Mars"))
print(temperatures5.count("Moon"))
# output:
# 1
# 0

# .lower() 
# Strings in Python are case-sensitive. To perform a case-insensitive comparison, you can convert a string to lowercase letters 
print("The Moon And The Earth".lower())
# output: the moon and the earth

# .upper() 
# converts all characters to uppercase 
print("The Moon And The Earth".upper())
# output: THE MOON AND THE EARTH 

# .isnumeric() 
# Python has methods that help to check the type of string. 
# It should loop through the elements and check if the values are of a given type.
# You may be surprised to learn that “-70”.isnumeric() will return False. 
# This is because all characters in the string would have to be numeric and the hyphen (-) is not. 
# If you have to check for negative numbers in a string, the .isnumeric() method will not work.
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
# output: 30

# .isdecimal() 
# can search for strings that look like decimals 

# .startswith()
# There are additional validations that you can apply on strings to check for values. 
# In the case of negative numbers, the hyphen is added as a prefix to the number and can be detected with the method
print("-60".startswith('-'))
# output: True

# .endswith() 
# helps to check the last character of a string 
if "30 C".endswith("C"):
	print("This temperature is in Celsius")
# output: This temperature is in Celsius 

# .replace()
# You can use the .replace() method to find and replace repetitions of a character or group of characters: 
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
# output: Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.

# .join() 
# Just as the .split() method can split characters, the .join() method can group them together again. 
# The .join() method needs an iterable element (such as a Python list) as an argument, 
# so its use is different from other string methods:
# In this example, ' ' is used to join all the elements of the list. 
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
# output: The Moon is drifting away from the Earth. On average, the Moon is moving about 4cm every year.


# *************************************************************************


# Search for a string 
# in
# The easiest way to detect whether there is a particular word, character or group of characters in a string 
print("Moon" in "This text will describe facts and challenges with space travel")
# output: False 
print("Moon" in "This text will describe facts about the Moon")
# output: True


# *************************************************************************


# String formatting
# %
# The placeholder for the string variable is %s. 
# After the string, use another % character followed by the variable name. 
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
# output: On the Moon, you would weigh about 1/6 of your weight on Earth.
# The use of multiple values changes the syntax, since parentheses are needed to surround the variables being passed: 
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# output: Both sides of the Moon get the same amount of sunlight, but only one side is seen from Earth because the Moon rotates around its own axis when it orbits Earth.

# .format() method
# The .format() method uses curly braces ({}) as placeholders within a string and uses variable assignment to replace text 
mass_percentage2 = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage2))
# output: On the Moon, you would weigh about 1/6 of your weight on Earth.
mass_percentage3 = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage3))
# output: You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth.
mass_percentage4 = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage4))
# output: You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth. 

# f-strings
# It is possible to use f-strings. 
# Variables are enclosed in braces and the string must use the prefix f 
# These strings look like templates and use the variable names from the code. 
# The use of f-strings in the above example would look like this
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
# output: On the Moon, you would weigh about 1/6 of your weight on Earth. 

# round() 
# if you want to represent the value 1/6 as a percentage with one decimal place, you can directly use the round() function 
print(round(100/6, 1))
# output: 16.7
# with f-strings 
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")
# output: On the Moon, you would weigh about 16.7% of your weight on Earth. 


# *************************************************************************


# Example 1: 
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
# The above code relies on everything after the colon (:) being a temperature. 
# The string is split into :, which generates a list of two elements. 
# Using [-1] in the list returns the last element which, in this example, is the temperature.
# output:
# ['Mars average temperature', ' -60 C']
# ' -60 C'

# Example 2:
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split('. ')
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)
# output: The highest daylight temperature of the Moon is 127 C.


# run: python string-usage.py 