# List is a collection of items that can be of different types, including numbers, strings,

dogs = ["Roger", "Syd"]
number = [1, 4, 6, 3, 5, 2]  # Length  6
multipleValues = ["zain", 2, True]  # List can store multiple values


print(dogs)
print(number)
print(multipleValues)


number = [1, 4, 6, 3, 5, 2]
# List is mutable, meaning you can change its content without changing its identity.
# Lists are ordered collections, meaning the items have a defined order, and that order will not change unless you explicitly reorder them.
# Start 0  to 5   memory wise store

print(number.index(3))  # Returns the index of the first occurrence of the value 3 in the list
print(number[0])  # Accessing the first element of the list
print(number[0:6])  # Slicing the list to get elements from index 0 to 5

number.append(10)  # Adding an element to the end of the list
number.append(43)
number.remove(435)  # Removing an element from the list
number.insert(2, 100)  # Inserting an element at a specific index
number.pop(2)  # Removing the last element from the list
number.extend([12, 8439, 435])  # Extending the list with multiple elements

print(number)


number.sort() # Sorting the list in ascending order

print(len(number.sort())) # Returns the length of the sorted list, which is 0 because sort() returns None
print(number)  


# dynamically type


# Python is a dynamically typed language, meaning that variable types are determined at runtime.# This allows for greater flexibility, as variables can change types during execution.
# For example, a variable can initially hold an integer and later be assigned a string without any type declaration.
# # Python does not require explicit type declarations for variables, allowing for more flexible and concise code.


# Statically Typed

# Statically Typed languages require explicit declaration of variable types at compile-time.
# This means that the type of a variable is known and checked before the program runs.
# Examples of statically typed languages include Java, C++, and Rust.

number = [1, 4, 6, 3, 5, 2]  # Length  6

str = "zain"
number.sort()
for i in str:  # Iterating through each character in the string
    print(i)
