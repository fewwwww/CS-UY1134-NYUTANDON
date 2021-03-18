def partition(lst):
    smaller_list, greater_list = [], []
    first_element = lst[0]
    for number in lst[1:]:
        # first element is not considered
        if number < first_element:
            smaller_list.append(number)
        else:
            # number > first_element
            greater_list.append(number)
    return smaller_list + [first_element] + greater_list
# O(n)
