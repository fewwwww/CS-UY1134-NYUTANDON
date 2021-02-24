def factors(num):
    r = int(num ** 0.5)
    for i in range(1, r + 1):
        if num % i == 0:
            yield i
    for j in range(r - 1, 0, -1):
        if num % j == 0:
            yield num // j
