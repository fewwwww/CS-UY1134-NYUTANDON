from LinkedBinaryTree import LinkedBinaryTree


class EmptyTree(Exception):
    pass


def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise EmptyTree("Empty binary tree")
    return subtree_min_and_max(bin_tree.root)


def subtree_min_and_max(root):
    # if root.left and root.right are all None
    if not root.left and not root.right:
        return (root.data, root.data)
    # if root.left and root.right are all not None
    if root.left and root.right:
        left = subtree_min_and_max(root.left)
        right = subtree_min_and_max(root.right)
        return (min(left[0], right[0], root.data), max(left[1], right[1], root.data))
    # if root.left is None and root.right is not None:
    elif not root.left and root.right:
        right = subtree_min_and_max(root.right)
        return (min(right[0], root.data), max(right[1], root.data))
    # if root.left is not None and root.right is None:
    else:
        left = subtree_min_and_max(root.left)
        return (min(left[0], root.data), max(left[1], root.data))
