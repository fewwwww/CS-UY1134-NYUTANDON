def max_value_and_count(lst, low, high):
    if low == high:
        return [lst[high], 1]
    else:
        current_max = max_value_and_count(lst, low+1, high)
        # current_max is [max_value, occurences]
        if lst[low] > current_max[0]:
            current_max[0], current_max[1] = lst[low], 1
        elif lst[low] == current_max[0]:
            current_max[1] += 1
        return current_max
