def remove_all(lst, value):
    pointer, n = 0, len(lst)
    for i in range(n):
        if lst[i] != value:
            lst[pointer] = lst[i]
            pointer += 1
    for val in range(pointer, n):
        lst.pop()
