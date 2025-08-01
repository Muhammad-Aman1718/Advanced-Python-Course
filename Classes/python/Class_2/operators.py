# Operators

# Arithmetic
# +, -, *, /, %, //, **


a = 10
b = 4

print("This is Addition :", a + b)
print("This is subtraction :", a - b)
print("This is multiple :", a * b)
print("This is division :", a / b)
print("This is floor division :", a // b)
print("This is modulus :", a % b)
print("This is exponentiation :", a**b)


# Conditional Operators

a = 10
b = 4

print("This is greater than :", a > b)
print("This is less than :", a < b)
print("This is equal to :", a == b)
print("This is not equal to :", a != b)
print("This is greater than or equal to :", a >= b)
print("This is less than or equal to :", a <= b)


# LOgical Operators
# and, or, not

a = True
b = False

print("This is logical AND:", a and b)
print("This is logical OR:", a or b)
print("This is logical NOT:", not a)
print("this is nnot b", not b)


# Bitwise Operators
# &, |, ^, ~, <<, >>

a = 10  # 1010 in binary
b = 4   # 0100 in binary


print("Bitwise AND:", a & b)  # 0000 in binary
print("Bitwise OR:", a | b)   # 1110 in binary
print("Bitwise XOR:", a ^ b)  # 1110 in binary
print("Bitwise NOT:", ~a)     # Inverts all bits   -(a + 1)
print("Left Shift:", a << 1)  # Shifts bits to the left   10100
print("Right Shift:", a >> 1) # Shifts bits to the right   01010


# Compound Operators
# +=, -=, *=, /=, %=, //=, **=

a = 15
b = 4


for i in range(1, 11):
    a += b
    print("This is Addition with compound operator:", a)
    print("This is number:", i)


a += b  # a = a + b
print("This is Addition with compound operator:", a)
b -= 2  # b = b - 2
print("This is Subtraction with compound operator:", b)

a *= b  # a = a * b

print("This is Multiplication with compound operator:", a)
b /= 2  # b = b / 2
print("This is Division with compound operator:", b)

a %= b  # a = a % b
print("This is Modulus with compound operator:", a)

a //= b  # a = a // b
print("This is Floor Division with compound operator:", a)
a **= b  # a = a ** b
print("This is Exponentiation with compound operator:", a)

# const
