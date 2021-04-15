from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    copiedLst = DoublyLinkedList()
    for node in lnk_lst:
        copiedLst.add_last(node)
    return copiedLst


def deep_copy_linked_list(lnk_lst):
    copiedLst = DoublyLinkedList()
    for node in lnk_lst:
        if isinstance(node, DoublyLinkedList):
            copiedLst.add_last(deep_copy_linked_list(node))
        else:
            copiedLst.add_last(node)
    return copiedLst
