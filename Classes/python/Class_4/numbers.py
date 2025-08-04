# Python Numbers and Boolean

# Boolean
# True and False
a = True
b = False

print(a)
if b:
    print("this is true")
else:
    print("this is false")


# Numbers

print(type(8) == int)


complexNumber = 2 + 3j

print(int(complexNumber.real))
print((complexNumber.imag))


print(round(0.52))  # 0  Round to nearest integer
print(round(0.52, 1))  # 0.5
print(round(0.5243676, 3))  # 0.524


age = 25  # age = int(input("Enter your age: "))

if age >= 20 and age <= 30:  # Check if age is between 20 and 30
    print("eligible for test")
else:
    print("sorry! you did not enter this website")


condition = True
name = "Roger"
if condition == True:
    print("The condition")
    print("was True")
elif name == "Roger":
    print("Hello Roger")
else:
    print("The condition")
    print("was False")
