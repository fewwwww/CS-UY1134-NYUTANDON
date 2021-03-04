def find_duplicates(lst):
    res, n = [], len(lst)
    for i in range(n):
        if lst[abs(lst[i])] < 0:
            res.append(abs(lst[i]))
        else:
            lst[abs(lst[i])] = -lst[abs(lst[i])]
    return res
