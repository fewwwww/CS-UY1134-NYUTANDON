from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        # start with 1 because each char in it at least exist once
        occurCount = 1
        # avoid indexing out of range
        for i in range(len(orig_str)-1):
            # if char is different from next one
            if orig_str[i] != orig_str[i+1]:
                self.data.add_last((orig_str[i - 1], occurCount))
                # set count back to one
                occurCount = 1
            else:
                occurCount += 1
        # consider the case that it only have one item
        if len(orig_str) >= 1:
            self.data.add_last((orig_str[-1], occurCount))

    def __add__(self, other):
        concatStr = CompactString("")
        # p is the pointer.
        p = self.data.header.next
        # while data is not empty
        while p.next.data is not None:
            concatStr.data.add_last(p.data)
            # move pointer forward
            p = p.next
        if p.data[0] == other.data.header.next.data[0]:
            concatStr.data.add_last((p.data[0], p.data[1] +
                                    other.data.header.next.data[1]))
            # let pointer skip one step
            p = other.data.header.next.next
        else:
            concatStr.data.add_last(p.data)
            p = other.data.header.next
        while p.data is not None:
            concatStr.data.add_last(p.data)
            p = p.next
        return concatStr

    def __lt__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next
        # continue to move pointer when they are not identical
        while p1.data == p2.data and p1.data is not None:
            p1 = p1.next
            p2 = p2.next
        if p1.data is None and p2.data is not None:
            return True
        elif p1.data is None and p2.data is None:
            return False
        elif p1.data is not None and p2.data is None:
            return False
        if p1.data[0] == p2.data[0]:
            if p1.data[1] > p2.data[1]:
                if p2.next.data is None:
                    return False
                return p1.data[0] < p2.next.data[0]
            else:
                if p1.next.data is None:
                    return True
                return p1.next.data[0] < p2.data[0]
        return p1.data[0] < p2.data[0]

    def __le__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next
        # continue to move pointer when they are not identical
        while p1.data == p2.data and p1.data is not None:
            p1 = p1.next
            p2 = p2.next
        if p1.data is None and p2.data is not None:
            return True
        elif p1.data is None and p2.data is None:
            return True
        elif p1.data is not None and p2.data is None:
            return False
        if p1.data[0] == p2.data[0]:
            if p1.data[1] > p2.data[1]:
                if p2.next.data is None:
                    return False
                return p1.data[0] < p2.next.data[0]
            else:
                if p1.next.data is None:
                    return True
                return p1.next.data[0] < p2.data[0]
        return p1.data[0] < p2.data[0]

    def __gt__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next
        # continue to move pointer when they are not identical
        while p1.data == p2.data and p1.data is not None:
            p1 = p1.next
            p2 = p2.next
        if p1.data is None and p2.data is not None:
            return False
        elif p1.data is None and p2.data is None:
            return False
        elif p1.data is not None and p2.data is None:
            return True
        if p1.data[0] == p2.data[0]:
            if p1.data[1] > p2.data[1]:
                if p2.next.data is None:
                    return True
                return p1.data[0] > p2.next.data[0]
            else:
                if p1.next.data is None:
                    return False
                return p1.next.data[0] > p2.data[0]
        return p1.data[0] > p2.data[0]

    def __ge__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next
        # continue to move pointer when they are not identical
        while p1.data == p2.data and p1.data is not None:
            p1 = p1.next
            p2 = p2.next
        if p1.data is None and p2.data is not None:
            return False
        elif p1.data is None and p2.data is None:
            return True
        elif p1.data is not None and p2.data is None:
            return True
        if p1.data[0] == p2.data[0]:
            if p1.data[1] > p2.data[1]:
                if p2.next.data is None:
                    return True
                return p1.data[0] > p2.next.data[0]
            else:
                if p1.next.data is None:
                    return False
                return p1.next.data[0] > p2.data[0]
        return p1.data[0] > p2.data[0]

    def __repr__(self):
        returnStr = ''
        for node in self.data.__iter__():
            tempStr = node[0] * node[1]
            returnStr += tempStr
        return returnStr
