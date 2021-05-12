from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue


def alternating_colors_by_levels(bin_tree):
    level = 0
    queue = ArrayQueue()
    queue.enqueue(bin_tree.root)
    queue.enqueue(None)
    while not queue.is_empty():
        node = queue.dequeue()
        if node is None:
            level += 1
            queue.enqueue(None)
            continue
        if level % 2 == 0:
            print((node.data, 'blue'), end=" ")
        else:
            print((node.data, 'red'), end=" ")
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)