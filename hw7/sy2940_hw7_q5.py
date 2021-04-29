from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    def create_expression_tree_helper(prefix_exp_lst, start_pos):
        exp = prefix_exp_lst[start_pos]
        if exp not in ["+", "-", "*", "/"]:
            root = LinkedBinaryTree.Node(int(exp))
            return (root, start_pos + 1)
        left = create_expression_tree_helper(prefix_exp_lst, start_pos + 1)
        right = create_expression_tree_helper(prefix_exp_lst, left[1])
        root = LinkedBinaryTree.Node(exp, left[0], right[0])
        return (root, right[1])
    prefix_lst = prefix_exp_str.split()
    return LinkedBinaryTree(create_expression_tree_helper(prefix_lst, 0)[0])


def prefix_to_postfix(prefix_exp_str):
    exp_tree = create_expression_tree(prefix_exp_str)
    postfix_exp = " ".join(str(node.data) for node in exp_tree.postorder())
    return postfix_exp
