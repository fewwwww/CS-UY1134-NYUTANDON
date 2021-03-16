def appearances(s, low, high):
    if low == high:
        return {s[low]: 1}
    dict_mapping = appearances(s, low + 1, high)
    if s[low] not in dict_mapping:
        dict_mapping[s[low]] = 1
        return dict_mapping
    dict_mapping[s[low]] += 1
    return dict_mapping
