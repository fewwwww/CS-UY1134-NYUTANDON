def fibs(n):
    first, second = 1, 1
    for i in range(n):
        yield first
        first, second = second, first + second
