# # Using lambda
# sq = lambda x: x**2
# print(sq(3))


# # Using def
# def sqdef(x):
#     return x**2


# print(sqdef(3))


class Solution:
    def largest(self, arr, x):
        # code here
        for i in range(len(arr)):
            if arr[i] == x:
                return i
            else:
                return -1


obj = Solution()
arr = [1, 2, 3, 4]
x = 3
print(obj.largest(arr, x))
