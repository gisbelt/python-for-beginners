# Create a list 
# To create a list, assign a sequence of values to a variable. 
# Each value is separated by a comma and enclosed in square brackets ([]).
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# You can access any item in a list by enclosing the index in square brackets []. 
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

# You can also change values in a list using an index. 
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])
# Output: Mars is also known as Red Planet 

# The length of a list 
# The following code creates a variable, number_of_planets. 
# The code assigns that variable with the number of elements in the planets list (8).
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
# Output: There are 8 planets in the solar system 

# Incorporation of values into lists 
# Python lists are dynamic: you can add and remove items after creating them. 
# To add an element to a list, use the method .append(value) 
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
# Output: There are actually 9 planets in the solar system. 

# Deleting list values 
# You can remove the last item in a list by calling the .pop() method on the list variable: 
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# Use of negative indexes 
# Indices start at zero and go upwards. Negative indexes start at the end of the list and go backwards. 
# an index of -1 returns the last element of a list. An index of -2 returns the second to last. 
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])
# Output 
# The last planet is Neptune
# The penultimate planet is Uranus

# Search for a value in a list 
# To determine where a value is stored in a list, use the “index” method of the list.
# This method looks for the value and returns the index of that element in the list. 
# If no match is found, it returns “-1”.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
# Output: Jupiter is the 5 planet from the sun 

#************************************************************************************************************

# Working with numbers in lists 
# Storing numbers in lists 
# In the example below, you can find out the weight of a double-decker bus on different planets by obtaining the value from the list: 
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")
# Output 
# On Earth, a double-decker bus weighs 124054 N
# On Mercury, a double-decker bus weighs 46892.4 N

# Using min() and max() with lists 
# max() returns the largest number and min() returns the smallest. 
# The following code calculates the minimum and maximum weights in the solar system using these functions: 
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")
# Output 
# On Earth, a double-decker bus weighs 124054 N
# The lightest a bus would be in the solar system is 46768.35 N
# The heaviest a bus would be in the solar system is 292767.44 N

#************************************************************************************************************

# List segmentation 
# Important: A segmentation creates a new list. It does not modify the current list. 
# A segmentation uses square brackets, but instead of a single element, it has the initial and final indexes.  
# When segmentation is used, a list is created that starts at the initial index and ends before the final index (and does not include it). 
# The list of planets has eight elements. 
# Earth is the third in the list. 
# To show the planets before Earth, use a segmentation to get the elements starting with 0 and ending with 2:
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth) # Output: ['Mercury', 'Venus']
# To get all the planets after Earth, start at the third and go to the eighth:
planets_after_earth = planets[3:8]
print(planets_after_earth) # Output: ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# If you don't place the stop index in the segmentation, Python assumes that you want to go to the end of the list 
planets_after_earth = planets[3:]
print(planets_after_earth) # Output: ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# List combination
# Important: A segmentation creates a new list. It does not modify the current list. 
# To join two lists, you must use the other operator (+) with two lists to return a new list. 
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output: The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto'] 

# List sorting 
# Important: The use of sort modifies the current list. 
# To sort a list, use the .sort() method of the list. 
# Python sorts a list of strings in alphabetical order and a list of numbers in numerical order:
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output: The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe'] 
regular_satellite_moons.sort(reverse=True) # To sort a list in reverse order
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
# Output: The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']

#************************************************************************************************************

# Exercise: 
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
user_planet = input("Please enter the name of the planet (with a capital letter to start)")
planet_index = planets.index(user_planet)
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])
# Remember that the starting index is included when you're using a slice. 
# As a result, you'll have to add 1 to the value. Add the code to display the planets farther from the sun. 
print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])


# run: python lists.py 