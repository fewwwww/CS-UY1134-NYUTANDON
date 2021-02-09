def shift(lst, k, direction="left"):
    if direction == "left":
        lst[:k] = lst[:k][::-1]
        lst[k:] = lst[k:][::-1]
        lst.reverse()
    elif direction == "right":
        lst.reverse()
        lst[:k] = lst[:k][::-1]
        lst[k:] = lst[k:][::-1]
