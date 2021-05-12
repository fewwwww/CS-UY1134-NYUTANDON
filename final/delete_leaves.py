def delete_leaves(root):
    # if node is none, return and break recursion
    if root is None:
        return
    # if node has left
    if root.left is not None:
        # this can keep the second layer of tree
        if root.left.left is None and root.left.right is None:
            root.left = None
    if root.right is not None:
        if root.right.left is None and root.right.right is None:
            root.right = None
    delete_leaves(root.left)
    delete_leaves(root.right)
