def two_sum(srt_lst, target):
    left, right = 0, len(srt_lst) - 1
    while left < right:
        s = srt_lst[left] + srt_lst[right]
        if s == target:
            return (left, right)
        elif s < target:
            left += 1
        else:
            right -= 1
    return None
