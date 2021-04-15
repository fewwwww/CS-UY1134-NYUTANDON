def keep_positives(lst):
    lst[:] = [number for number in lst if number > 0]


lst = [1, -1]
keep_positives(lst)
print(lst)
