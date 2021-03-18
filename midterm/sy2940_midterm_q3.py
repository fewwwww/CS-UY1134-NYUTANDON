def keep_positives(lst):
    lst[:] = [number for number in lst if number > 0]
