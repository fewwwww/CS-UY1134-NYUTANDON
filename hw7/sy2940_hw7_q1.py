def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise Exception("Empty bin_tree")

    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return (root.data, root.data)
        elif root.left is not None and root.right is None:
            leftRoute = subtree_min_and_max(root.left)
            return (min(leftRoute[0], root.data), max(leftRoute[1], root.data))
        elif root.left is None and root.right is not None:
            rightRoute = subtree_min_and_max(root.right)
            return (min(rightRoute[0], root.data), max(rightRoute[1], root.
                                                       data))
        else:
            # if both right and left are not none
            leftRoute = subtree_min_and_max(root.left)
            rightRoute = subtree_min_and_max(root.right)
            return (min(leftRoute[0], rightRoute[0], root.data),
                    max(leftRoute[1], rightRoute[1], root.data))
    return subtree_min_and_max(bin_tree.root)