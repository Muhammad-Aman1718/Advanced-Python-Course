# def add():

# def prnt():
#     print("Hello World")


# def add(num1: int, num2: int):   # Formal parameter
#     add = a + b
#     # print(add)
#     return add


# a = 3
# b = 5

# # add = a +
# p = add(a, b)   # Actual parameter
# print(p)


def arrfunc(arr: list[int]):
    # for i in arr:
    #     print(i, end=" ")
    arr.sort()
    return arr


arr: list[int] = [1, 5, 2, 3, 4, 6]


print(arrfunc(arr))
