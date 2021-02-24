def e_approx(n):
    e, div = 1, 1
    for i in range(1, n):
        e += 1/div
        div *= i
    return e
