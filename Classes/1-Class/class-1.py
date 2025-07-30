# Purposes:

# Brief overview of Python: High-level, interpreted, and general-purpose language.
# Uses of Python: Web development, automation, data science, AI, and more.
# Discuss Python's popularity due to its simplicity and large community support.

# input

# Input Built-in Function
# The input() function allows user input from the console.
a = input("Enter a number: ")  # By default, input returns a string

# Print is used to display output to the console.
# The print() function outputs the specified message to the console.
print("This is string:", a)

# type conversion
b = int(a)  # Convert string to integer
c = float(a)  # Convert string to float
d = bool(a)  # Convert string to boolean

# Type method is used to check the type of a any variable

print(type(a))  # Display the type of variable a
print(type(b))  # Display the type of variable b
print(type(c))  # Display the type of variable c
print(type(d))  # Display the type of variable d
print("this is string", a, b, c)
print("this is number", b)
print("this is float number", c)
print("this is boolean", d)


# Variables# Variables are used to store data values.
# In Python, variables do not need explicit declaration to
a = 10
b = 20.5
c = "Hello"
d = True

# Variables can be reassigned to different data types.

# Example of variable reassignment
a = "This is now a string"
# Example of variable reassignment
b = 42
# Example of variable reassignment
c = 3.14
# Example of variable reassignment
d = "False"

print("This is integer:", a)
print("This is float:", b)
print("This is string:", c)
print("This is boolean:", d)


# for i in range(1, 11):
#     print("This is number:", i)  # this is indentation

# Indentation is used to define the scope of loops, functions, and conditionals in Python.

# Examples
def print_numbers():
    for i in range(1, 11):
        print("This is number:", i)
print_numbers()  # Function call to execute the loop








# Data Types
# int, float, str, bool, list, tuple, set, dict

a = 10
f = 20.5
s = "Hello"
l = [1, 2, 3, 4, 5]
t = (1, 2, 7)
complex = 3 + 4j


# Operators
# Arithmetic Operators
# +, -, *, /, //, %, **
a = 3
b = 7

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a**b)
