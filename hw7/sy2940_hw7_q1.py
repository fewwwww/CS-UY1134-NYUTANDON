def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        minVal = root
        maxVal = root
        if root.left is not None:
            leftRoute = subtree_min_and_max(root.left)
            minVal = min(minVal, leftRoute[0])
            maxVal = max(maxVal, leftRoute[1])
        if root.right is not None:
            rightRoute = subtree_min_and_max(root.right)
            minVal = min(minVal, rightRoute[0])
            maxVal = max(maxVal, rightRoute[1])
        return (minVal, maxVal)
    if bin_tree.root is None:
        raise Exception("Empty binary tree")
    return subtree_min_and_max(bin_tree.root)