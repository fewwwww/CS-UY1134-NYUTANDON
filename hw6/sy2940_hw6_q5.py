from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(lst1_node, lst2_node, srt_lnk_lst1, srt_lnk_lst2):
        if lst1_node.data is None and lst2_node.data is not None:
            mergedLst = DoublyLinkedList()
            while lst2_node.data is not None:
                mergedLst.add_last(lst2_node.data)
                lst2_node = lst2_node.next
        elif lst1_node.data is not None and lst2_node.data is None:
            mergedLst = DoublyLinkedList()
            while lst1_node.data is not None:
                mergedLst.add_last(lst1_node.data)
                lst1_node = lst1_node.next
        else:
            if lst1_node.data < lst2_node.data:
                mergedLst = merge_sublists(lst1_node.next, lst2_node,
                                           srt_lnk_lst1, srt_lnk_lst2)
                mergedLst.add_first(lst1_node.data)
            else:
                mergedLst = merge_sublists(lst1_node, lst2_node.next,
                                           srt_lnk_lst1, srt_lnk_lst2)
                mergedLst.add_first(lst2_node.data)
        return mergedLst

    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next,
                          srt_lnk_lst1, srt_lnk_lst2)
