def sumA(n):
    if n == 0:
        return 0
    return (n-1)**2 + sumA(n-1)


def sumB(n):
    return sum([k * k for k in range(1, n)])


def sumC(n):
    res = 0
    for i in range(1, n):
        if i % 2 == 1:
            res += i**2
    return res


def sumD(n):
    return sum(k ** 2 for k in range(1, n) if k % 2 == 1)
