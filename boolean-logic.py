# "if" instruction
a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print(b)
print(b)
# output: 55

# "else" instruction
c = 27
d = 93
if c >= d:
    print(c)
else:
    print(d)    
# output: 93

# "elif" instruction
e = 27
f = 93
if e <= f:
    print("e is less than or equal to f")
elif e == f:
    print("e is equal to f")
# output: e is less than or equal to f

g = 27
h = 93
if g < h:
    print("g is less than g")
elif g > h:
    print("g is greater than g")
else:
    print ("g is equal to h")
# output: g is less than g

# indenting the body of an “if”, "else", "elif" statement
# Any code following a test expression that is not indented will always be executed. 
# Note also that an “if” block can only have one “else” block, but it can have several “elif” blocks. 

#************************************************************************************************************

# nested conditional logic 
# indent the internal conditions and everything at the same indentation level will be executed in the same code block
i = 16
j = 25
k = 27
if i > j:
    if j > k:
        print ("i is greater than j and j is greater than k")
    else:
        print ("i is greater than j and less than k")
elif i == j:
    print ("i is equal to j")
else:
    print ("i is less than j")
# output: i is less than j

#************************************************************************************************************

# "or" operator
# For the whole expression to evaluate to “True”, at least one of the subexpressions must be “true”. 
l = 23
m = 34
if l == 34 or m == 34:
    print("or operator: ", l + m)
# output: or operator:  57

# "and" operator   
# Both conditions of the test expression must be met for the entire test expression to evaluate to True. In any other case, the test expression is “False”.
n = 23
o = 34
if n == 34 and n == 34:
    print ("and operator: ", n + o)


# run: python boolean-logic.py 