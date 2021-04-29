def is_height_balanced(bin_tree):
    if bin_tree.root is None:
        raise Exception("Empty bin_tree")

    def is_sub_balanced(root):
        if root is None:
            return (True, 0)
        leftRoute = is_sub_balanced(root.left)
        rightRoute = is_sub_balanced(root.right)
        height = max(leftRoute[1], rightRoute[1]) + 1
        if (not leftRoute[0] or not rightRoute[0]) or abs(leftRoute[1] -
                                                          rightRoute[1]) > 1:
            return (False, height)
        return (True, height)
    return is_sub_balanced(bin_tree.root)[0]