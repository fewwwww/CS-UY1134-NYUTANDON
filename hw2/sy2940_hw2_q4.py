def e_approx(n):
    e, div = 1, 1
    for i in range(1, n+1):
        div /= i
        e += div
    return e

