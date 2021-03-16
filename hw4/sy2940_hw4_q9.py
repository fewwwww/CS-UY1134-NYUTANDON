def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    permutation_lst = []
    for i in range(high - low + 1):
        for sub_lst in permutations(lst, low + 1, high):
            sub_lst.insert(i, lst[low])
            permutation_lst.append(sub_lst)
    return permutation_lst
