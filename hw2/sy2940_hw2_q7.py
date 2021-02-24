def findChange(lst01):
    left, right = 0, len(lst01) - 1
    middle = right // 2
    while lst01[middle] != 1 or lst01[middle - 1] != 0:
        if(lst01[middle] == 1):
            right = middle - 1
        else:
            left = middle + 1
        middle = (left + right) // 2
    return middle
