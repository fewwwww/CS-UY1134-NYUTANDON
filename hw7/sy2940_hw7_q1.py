# from LinkedBinaryTree import LinkedBinaryTree


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


def is_size_tree(bin_tree):
    result = is_size_tree_helper(bin_tree.root)
    return result[0]


def is_size_tree_helper(root):
    if not root.left and not root.right:
        return (root.data == 1, 1)
    if root.left and root.right:
        left = is_size_tree_helper(root.left)
        right = is_size_tree_helper(root.right)
        return (left[0] and right[0] and root.data == left[1] + right[1] + 1, 
                left[1] + right[1] + 1)
    elif not root.left and root.right:
        right = is_size_tree_helper(root.right)
        return (right[0] and root.data == right[1] + 1, 
                right[1] + 1)
    else:
        left = is_size_tree_helper(root.left)
        return (left[0] and root.data == left[1], 
                left[1] + 1)