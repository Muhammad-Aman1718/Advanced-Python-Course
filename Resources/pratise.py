# s = {1, 2, 3}
# s.add(4)  # {1,2,3,4}
# print(s)
# s.update([5, 6])  # {1,2,3,4,5,6}
# print(s)
# s.remove(2)  # removes 2, KeyError if missing
# print(s)
# s.discard(99)  # safe remove, no error if missing
# print(s)
# elem = s.pop()  # removes & returns an arbitrary element
# print(elem)
# # s.clear()  # empty the set
# # len(s)  # size
# # 1 in s  # membership test True/False
# # u = s.copy()

# # print(u)
# # print(s)


a = {2, 3, 4, 1}
b = {3, 4, 5, 6}

print(a | b)  # union -> {1,2,3,4,5,6}
print(a & b)  # intersection -> {3,4}
print(b - a )  # difference -> {1,2}
print(a ^ b)  # symmetric difference -> {1,2,5,6}

# a.discard(5)
# print(a)

# a.pop()
print(a)

# forzen = frozenset(a)



# print(forzen)
