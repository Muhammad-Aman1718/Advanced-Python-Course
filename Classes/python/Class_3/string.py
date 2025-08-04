b = "fdjslkajflkd"  # This is a single-line string

a = """  
jfdklsajflkjdsalf
gjsgfd
ngfjsf
gjslkj

"""  # This is a multi-line string
print(a)

name = "Roger"
name += " is a good dog"
print(name)  # Roger is a good dog
str()


a = 90
print(type(a))  # <class 'int'>
b = str(a)
print(type(b))  # <class 'str'>


print("Roger is " + str(8) + " years old")  # Roger is 8 years old


name = input("enter your name : ")
user2 = input("enter your name : ")

print(name.lower(), user2)  # lowercase
print(name.upper(), user2)  # uppercase


print(
    "this is string methods", dir(str)
)  # Dir presents the methods available for the str class
print(
    "this is number methods", dir(int)
)  # Dir presents the methods available for the int class
print(
    "this is boolean methods", dir(bool)
)  # Dir presents the methods available for the bool class


a = 'am"an'
# e = "nd"

print(a)


a = "roger"

print(a[2])  # Accessing the third character
print(a[-2])  # Accessing the second-to-last character
print(a[0:6])  # Slicing the string from index 0 to 5
