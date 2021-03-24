# ADD BINARY NUMBER
# def add_binary(a, b):
#     a, b, c = a[::-1], b[::-1], []
#     i, j = 0, 0
#     nxt = 0
#     while i < len(a) or j < len(b) or nxt:
#         n_a = int(a[i]) if i < len(a) else 0
#         n_b = int(b[j]) if j < len(b) else 0
#         nxt = (n_a + n_b + nxt) // 2
#         val = (n_a + n_b + nxt) % 2
#         c.append(str(val))
#         i, j = i + 1, j + 1
#     return ''.join(c)
#
#
# print(add_binary('11', '1'))


# COMPLEX NUMBER
# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         return Complex(self.a + other.a, self.b + other.b)
#
#     def __sub__(self, other):
#         return Complex(self.a - other.a, self.b - other.b)
#
#     def __mul__(self, other):
#         return Complex(self.a*other.a-self.b*other.b, self.b*other.a+self.a*other.b)
#
#     def __repr__(self):
#         if self.b > 0:
#             return '{0}+{1}i'.format(self.a, self.b)
#         else:
#             return '{0}{1}i'.format(self.a, self.b)
#
#     def __iadd__(self, other):
#         self.a += other.a
#         self.b += other.b
#
#
# a = Complex(1,2)
# b = Complex(2,3)
# print(a)
# print(b)
# print(a+b)
# print(a-b)
# print(a*b)


# CAN CONSTRUCT
# def can_construct(word, letter):
#     word, letter = list(word), list(letter)
#     for i in word:
#         try:
#             letter.remove(i)
#         except:
#             return False
#     return True
#
#
# print(can_construct("apples", "aples"))


# BINARY SEARCH
# def binary_search(lst, val):
#     left = 0
#     right = len(lst)-1
#     while left <= right:
#         mid = (left+right)/2
#         if val == lst[mid]:
#             return mid
#         elif val < lst[mid]:
#             right = mid
#         elif val > lst[mid]:
#             left = mid
#     return None


lst = [1, 5, 3, 2, 6, 7, 4]
# selection
for i in range(len(lst)-1):
    minI = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[minI]:
            minI = j
    lst[i], lst[minI] = lst[minI], lst[i]
print(lst)
lst = [1, 5, 3, 2, 6, 7, 4]
# insertion
for i in range(1, len(lst)):
    val = lst[i]
    j = i-1
    while j >= 0 and lst[j] > val:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = val
print(lst)
lst = [1, 5, 3, 2, 6, 7, 4]


def mergeSort(lst):
    def merge(left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result

    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left, right)
