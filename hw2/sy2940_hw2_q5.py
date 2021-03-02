def split_parity(lst):
    a, b = 0, 0
    for num in lst:
        if num % 2 == 1:
            lst[a], lst[b] = lst[b], lst[a]
            a += 1
            b += 1
        else:
            b += 1
    return lst
