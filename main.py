# LAB 1


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
